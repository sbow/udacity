from uda_matrix import matrix

x = matrix([[1,0],[0,2]])
print (x.Cholesky()).CholeskyInverse()
#y = matrix([[0,0],[0,0]]).identity(2)
y = matrix([[]])
y.identity(2)
print y
print matrix([[]]).identity(2)

measurements = [1, 2, 3]

x = matrix([[0.], [0.]]) # initial state (location and velocity)
P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
u = matrix([[0.], [0.]]) # external motion
F = matrix([[1., 1.], [0, 1.]]) # next state function
H = matrix([[1., 0.]]) # measurement function
R = matrix([[1.]]) # measurement uncertainty
I = matrix([[1., 0.], [0., 1.]]) # identity matrix

print H*P.transpose() #+ R*H

s = matrix([[.1]])
print s*s
