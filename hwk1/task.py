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

    ### SOLUTIONS START HERE

    def solve(self):
        ### Solution returning goes here
        return [0]

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
