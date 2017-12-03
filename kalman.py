#   Shaun Bowman
#   2017/10/08
#   kalman.py
#   Purpose:    Implement 2D kalman filter following udacity code
#   Uses:   uda_matrix.py - simple math oveload for matricies (add,sub,mul,div)

from uda_matrix import matrix


def getNextStateAndPostDistro(x, measurements, P):
    x = []
    p = []


    return x,P

dt = 1

measurements = matrix([[0.      ,   0.  ],
                       [10.     ,   0.  ],
                       [20.     ,   0.  ],
                       [30.     ,   0.  ]])

x = matrix([[0.,      0.,     0.,     0.,]])
P = matrix([[0.,      0.,     0.,     0.,],
            [0.,   1000.,     0.,     0.,],
            [0.,      0.,  1000.,     0.,],
            [0.,      0.,     0.,  1000.,]])
u = matrix([[0., 0., 0., 0.]])
F = matrix([[   1.,     0.,      dt,    0],
            [   0.,     1.,      0.,   dt],
            [   0.,     0.,      1.,    0],
            [   0.,     0.,      0.,   dt]])
H = matrix([[   1.,     0.,      0.,    0],
            [   0.,     1.,      0.,    0]])
R = matrix([[   .1,     0.,],
            [   .0,     .1,]])
I = matrix([[]])
I.identity(4)

print (getNextStateAndPostDistro(x, measurements, P))
