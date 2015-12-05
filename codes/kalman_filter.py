#!/usr/bin/env python

from matrix import Matrix

class Kalman():
    """
    Kalman filter
    TODO: documentation
    TODO: unittests
    TODO: FInish the thing!!!!
    """
    def __init__():
        print 'test'
        
    def filter(x, P):
        for n in range(len(self.measurements)):
            # prediction
            x = (self.F * x) + self.u
            P = self.F * P * self.F.transpose()
            
            # measurement update
            Z = Matrix([self.measurements[n]])
            y = Z.transpose() - (self.H * x)
            S = self.H * P * self.H.transpose() + self.R
            K = P * self.H.transpose() * S.inverse()
            x = x + (K * y)
            P = (self.I - (K * self.H)) * P
        return x,P    

        

