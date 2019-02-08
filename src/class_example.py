import numpy as np
# -----------------------
# diego domenzain
# Boise State University 
# fall 2017
# -----------------------
# this is a simple example of a class
# that inputs and outputs 
# numpy objects.
# -----------------------
# the class builds a matrix Lw 
# that can do two things:
#   . multiply by a vector u to get s
#   . solve for a vector s and get u
# 
# Lw * u = s
# -----------------------
class Lw():
    def __init__(self,n,p):
        super(Lw, self).__init__()
        self.mat = p * np.eye(n)
        
    def act_on(self,u):
        u = np.dot(self.mat,u)
        return u
    
    def solve_for(self,s):
        s = np.linalg.solve(self.mat, s)
        return s
# -----------------------------------------
# see it in action.
# in a terminal type: 
#       $ python class_example.py
# -----------------------------------------
u = np.ones((2,1))
L = Lw(2,3)
s = L.act_on(u)
u_ = L.solve_for(s)
print(s)