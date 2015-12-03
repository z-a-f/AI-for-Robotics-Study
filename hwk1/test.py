#!/usr/bin/env python

import unittest
import testGeneric

import task

class testSolution(testGeneric.Test):
    def show(self,p):
        for i in range(len(p)):
            print p[i]
        
    
    def test_four_1(self):
        tsk = task.Task()
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'G'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R']
        tsk.motions = [[0,0]]
        tsk.sensor_right = 1.0
        tsk.p_move = 1.0
        p = tsk.solve() # colors,measurements,motions,sensor_right,p_move)

        expected = (
            [[0.0, 0.0, 0.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 0.0]])
        
        # self.show(p)

        self.assertAlmostEqual(expected, p)

    def test_four_2(self):
        tsk = task.Task()
        # test 2
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R']
        tsk.motions = [[0,0]]
        tsk.sensor_right = 1.0
        tsk.p_move = 1.0
        p = tsk.solve()
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.5, 0.5],
             [0.0, 0.0, 0.0]])

        self.assertAlmostEqual(correct_answer, p, 4)
        
    def test_four_3(self):
        tsk = task.Task()
        # test 3
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R']
        tsk.motions = [[0,0]]
        tsk.sensor_right = 0.8
        tsk.p_move = 1.0
        p = tsk.solve()
        correct_answer = (
            [[0.06666666666, 0.06666666666, 0.06666666666],
             [0.06666666666, 0.26666666666, 0.26666666666],
             [0.06666666666, 0.06666666666, 0.06666666666]])
        self.assertAlmostEqual(correct_answer, p, 4)
        
    def test_four_4(self):
        tsk = task.Task()
        # test 4
        tsk.colors = [['G', 'G', 'G'],
                      ['G', 'R', 'R'],
                      ['G', 'G', 'G']]
        tsk.measurements = ['R', 'R']
        tsk.motions = [[0,0], [0,1]]
        tsk.sensor_right = 0.8
        tsk.p_move = 1.0
        p = tsk.solve()
        print p
        correct_answer = (
            [[0.03333333333, 0.03333333333, 0.03333333333],
             [0.13333333333, 0.13333333333, 0.53333333333],
             [0.03333333333, 0.03333333333, 0.03333333333]])
        self.assertAlmostEqual(correct_answer, p, 4)
        
    def test_four_5(self):
        tsk = task.Task()
        # test 5
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R', 'R']
        tsk.motions = [[0,0], [0,1]]
        tsk.sensor_right = 1.0
        tsk.p_move = 1.0
        p = tsk.solve()
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.0, 1.0],
             [0.0, 0.0, 0.0]])
        self.assertAlmostEqual(correct_answer, p, 4)
        
    def test_four_6(self):
        tsk = task.Task()
        # test 6
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R', 'R']
        tsk.motions = [[0,0], [0,1]]
        tsk.sensor_right = 0.8
        tsk.p_move = 0.5
        p = tsk.solve()
        correct_answer = (
            [[0.0289855072, 0.0289855072, 0.0289855072],
             [0.0724637681, 0.2898550724, 0.4637681159],
             [0.0289855072, 0.0289855072, 0.0289855072]])
        self.assertAlmostEqual(correct_answer, p, 4)
        
    def test_four_7(self):
        tsk = task.Task()
        # test 7
        tsk.colors = [['G', 'G', 'G'],
                  ['G', 'R', 'R'],
                  ['G', 'G', 'G']]
        tsk.measurements = ['R', 'R']
        tsk.motions = [[0,0], [0,1]]
        tsk.sensor_right = 1.0
        tsk.p_move = 0.5
        p = tsk.solve()
        correct_answer = (
            [[0.0, 0.0, 0.0],
             [0.0, 0.33333333, 0.66666666],
             [0.0, 0.0, 0.0]])
        self.assertAlmostEqual(correct_answer, p, 4)
        
if __name__ == '__main__':
    unittest.main()
