# October 2 2017
# Shaun Bowman - Udacity Course Notes - Aritificial Inteligence for Robotics -
# Lesson 4 - Kalman Filteres

# Gausian - location & measurement probililty distobution
# new variance = sigmasquare = (1 / ( 1/sigmaSqLocation + 1/signmaSqmeasurement))
# new mean = 1 / ( sigmaSqLoc + sigmaSqMeas ) * ( SigmaSqLoc*MeanMeas +
# SigmaSqMeas * MeanLoc )
# notes:
#   - mean will be between location & measurement
#   - variance willbe LESS than either (ie: better, more information)
def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

# Measurement update: bayes rule multiplication (new variance / mean, formula
# above)
# Motion update prediction: Total probability : addition.
#   ini: mean & var  (mu, sig)
#   move: mean & var
#   prediction: add 2 means, increased variance (lose information)
#   math:   varPositionPrediction = varInit+ varMove
#           meanPositionPrediction = meanInit + meanMove
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

print predict(10., 4., 12., 4.)

# quiz 19 - kalman filter code:
# note: motion here is defined as move to a specific location, not a delta from
# current location
# note2: first measurement totaly wipes out huge initial sigma, note:
 # measurement always gives better sigma (variance/stddevsq) than either
# prior variance's
# note3: difference between initial mu & first measurement is error in initial
# position estimate.
# note4: assigning a high sigma in initial measurement estimate HELPS accuracy
# of final result. Implys low weight to initial measurement
# note5: kalman filter is very good when measurement / motion / initial
# position can be described as guassian (bell shape, unimodal [1 hump])
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for i in range( len( measurements ) ):
    mu_meas, var_meas = update( mu, sig, measurements[i], measurement_sig)
    mu_move, sig_move = predict( mu_meas, var_meas, motion[i], motion_sig) #see
    # note above, motion[i] not motion[i] + mu_meas or motion[i] + mu
    mu = mu_move
    sig = sig_move
print [mu, sig]


# Excersice 21:
# Kalman filter practical note:
# in 2D, if you only have position measurements in time
# the kalman filter can be made to implicitly factor in velocity
# to predict where the item will be
# this is explaned in with a set of mu's and sigmas, called multivariate gaussians
#     [u_0]          <--- matrix of mu's, D rows
#     | . |
#u =  |.  |
#     |.  |   
#     [u_D]
#
#E =  [..........]   <--- matrix of variances, called covariance matrix
#     |.         |       D rows, D columns
#     |.         |
#     |.         |
#     |.         ]
#
#f(x) = (2*pi)^-0.5 * |E|^-0.5*exp(-0.5*transpose(x-u)*E^-1*(x-u) #describes 2D
# guassian distribution, can be drawn as contour lines around mean (x_0, y_0)
# note: if 2D guassian is slanted in x,y it means x&y are correlated
# so if you know something about x, it implies something about y
# Application: for 1D position measurements, invent 2nd dimetion for velocity

# Excersice 25
# Example: if you know a physical relationship like position equals prior
# position + velocity:  x' = x + x_dot*delta_t
# you can get the predicted position at the NEXT unobserved timestep by
# multiplying the mu/sigma of your current measurement position estimate by the guassian
# distrubution relating x_dot to x' ie for x_1, and relationship x' = x + x_dot
# the prior distrobution relating x' would be a slanted line centered through
# the following points: [x, x_dot] = [0,-1],[1,0],[2,1],[3,2] ect
# This is an example of using a measureable variable (x) to infer a non
# measureable variable (x_dot)
# Kalman Filter variables(ie: x, x_dot, their sigmas / mu's) are called "Kalman
# States"; and they are divided into 2 types "Observable & Hidden"
# Kalman Filter is very efficiant for problems when you need to estimate a
# hidden variable using observable variables.
# To design a kalman filter you need 2 things typically:
# State Transision Function: defines relationship between x', x & x_dot (ie: x'
# = x + x_dot; this is a matrix (typ square) (x',xdot') = (StateTransMtrx)*
# (x;xdot)
# Measurement Transision Function: defines relationships between "Z" and
# x,xdot, typically a column vector, Z = (MeasTransFunc)*(x;xdot) 
#
# example: new position = old position + vel&deltaT; new velocity = old
# velocity | state transision matrix = ( 1, 1; 0, 1 ) or x',xdot' = (1, 1;
# 0,1)*(x; xdot)
# measurement Z = old postion only (not velocity, ie: a camera image), the
# measuremente transision function equals (1, 0) or z = (1,0)*(x;xdot)

