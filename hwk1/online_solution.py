# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
p = []

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
    
def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<
    tsk = Task()
    tsk.colors = colors
    tsk.measurements = measurements
    tsk.motions = motions
    tsk.sensor_right = sensor_right
    tsk.p_move = p_move

    p = tsk.solve()
    return p
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
