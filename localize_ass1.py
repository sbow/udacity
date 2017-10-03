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

def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    
    # >>> Insert your code here <<<

    for step in range(len(measurements)): # for each motion

        motion = motions[step]
        #print motion    
        #show(p)
        # Move probability, Measure probobility, Product, probability
        # Move - lose information, smooth probabilty
        # For each movement
        # loop through p, 
        s = [ [ p[i][j] for j in range( len(p[0]) ) ] for i in range( len(p))]
        #^deep copy of p, dont really need copy just 2D list of same dims.
        # avoids copy by referance ie: s = p here doesnt work for copying
        # elements below in the motion section
        # Traverse across columns
        if not(motion[1] == 0):
            for i in range(len(p)): #grab row
                for j in range(len(p[i])): #j column
                    j_elem = (j-motion[1]) % len(p[0]) # method for finding
                    # motion index, allows for roll-over
                    s[i][j] = p[i][j_elem]*p_move + p[i][j]*(1-p_move)  #copy
                    #move element & fail to move element w multply by prob
        # Traverse across rows (move up / down)
        if not(motion[0] == 0):
            for j in range(len(p[0])): #j column p[i][j]
                for i in range(len(p)):
                    i_elem = (i-motion[0]) % len(p)
                    s[i][j] = p[i_elem][j]*p_move + p[i][j]*(1-p_move)
        # Normalize - Dont need to do this for some reason.. maybe because P is
        # already normalized and p_move/not move is 1 based?
        show(s)
        #sum = 0.0
        #for i in range(len(p)):
        #    for j in range(len(p[0])):
        #        sum = sum + s[i][j]
        #for i in range(len(p)):
        #    for j in range(len(p[0])):
        #        s[i][j] = s[i][j] / sum
        #show(s)

        # Sense - gain information  NEED CONTENT
        for i in range(len(p)):
            for j in range(len(p[0])):
                if colors[i][j] == measurements[step]:
                    s[i][j] = s[i][j] * sensor_right
                else:
                    s[i][j] = s[i][j] * (1.0 -sensor_right)
        # Normalize
        sum = 0.0
        for i in range(len(p)):
            for j in range(len(p[0])):
                sum = sum + s[i][j]
        for i in range(len(p)):
            for j in range(len(p[0])):
                s[i][j] = s[i][j] / sum
        print 'location:'
        show(s)
        p = s

    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    
#############################################################
# For the following test case, your output should be 
# [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
#  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
#  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
#  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
# (within a tolerance of +/- 0.001 for each entry)

#Trial
#colors = [['G','G','G'],
#          ['G','R','G'],
#          ['G','G','G']]
#measurements = ['R','G','G','R','R'] # note: 2nd R is sensorerror
#motions = [[0,0],[-1,0],[0,-1],[1,0],[0,1]]

colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
