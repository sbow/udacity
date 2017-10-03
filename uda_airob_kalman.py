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


