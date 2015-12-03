#!/usr/bin/env python

class Task():
    def __init__(self):
        self.colors = [['red', 'green', 'green', 'red' , 'red'],
                  ['red', 'red', 'green', 'red', 'red'],
                  ['red', 'red', 'green', 'green', 'red'],
                  ['red', 'red', 'red', 'red', 'red']]

        self.measurements = ['green', 'green', 'green' ,'green', 'green']


        self.motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
        self.sensor_right = 0.7
        self.p_move = 0.8

        self.p = []

    def uniform_distribution(self):
        # Get the size (1D or 2D):
        rows = len(self.colors)
        if isinstance(self.colors[0], list):
            # 2D
            cols = len(self.colors[0])
            scale = cols*rows
            self.p = [[1.0/scale]*cols for idx in range(rows)]
        else:
            # 1D
            cols = rows
            rows = 1
            self.p = [1.0/cols for idx in range(cols)]
        # return self.p        
        self.rows = rows
        self.cols = cols
            
    def sense1D(self, p, Z):
        s = 0
        for idx in xrange(self.cols):
            hit = (Z == self.colors[idx])
            prob = hit * self.sensor_right + (1. - hit) * (1. - self.sensor_right)
            p[idx] *= prob
        s = float('inf') if s == 0 else s
        for idx in xrange(self.cols):
            p[idx] = p[idx] / s

        return p

    def sense2D(self, p, Z):
        s = 0
        for idx in xrange(self.rows):
            for jdx in xrange(self.cols):
                hit = (Z == self.colors[idx][jdx])
                prob = hit * self.sensor_right + (1. - hit) * (1. - self.sensor_right)
                p[idx][jdx] *= prob
                s += p[idx][jdx]
        s = float('inf') if s == 0 else s
        
        for idx in xrange(self.rows):
            for jdx in xrange(self.cols):
                p[idx][jdx] = p[idx][jdx] / s
        return p

    def sense(self, Z):
        if self.rows == 1:
            self.p = self.sense1D(self.p, Z)
        else:
            self.p = self.sense2D(self.p, Z)
        return self.p
    
    def move1D(self, p, U):
        q = [0] * self.cols        
        for idx in xrange(self.cols):
            p[idx] = self.p_move*p[(idx - U) % self.cols] + (1 - self.p_move) * p[idx]
        return p

    def move2D(self, p, U):
        q = [[0] * self.cols for r in xrange(self.rows)]
        for idx in xrange(self.rows):
            for jdx in xrange(self.cols):
                q[idx][jdx] = self.p_move*p[(idx - U[0]) % self.rows][(jdx - U[1]) % self.cols] + (1 - self.p_move) * p[idx][jdx]
        p = q
        return p
            
    def move(self, U):
        if self.rows == 1:
            self.p = self.move1D(self.p, U)
        else:
            self.p =  self.move2D(self.p, U)
        return self.p
        
    def solve(self):
        # Solution goes here
        self.uniform_distribution()
        # Assuming number of measurements and steps is the same (steps)
        steps = len(self.measurements)
        for s in xrange(steps):
            self.move(self.motions[s])
            self.sense(self.measurements[s])
        return self.p
        

if __name__ == '__main__':
    tsk = Task()
    tsk.solve()
    s = 0
    for idx in xrange(tsk.rows):
        for jdx in xrange(tsk.cols):
            print '%.4f\t'%tsk.p[idx][jdx],
            s += tsk.p[idx][jdx]
        print ''

    print s
