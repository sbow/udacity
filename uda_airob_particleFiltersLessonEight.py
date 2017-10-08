# LESSON 8 - Particle Filters
# Artificial Intelligenc for Robotics
# (self driving cars)
# udacity.com
# 2017/10/05
# Shaun Bowman

#   General Description:
#   Distribute throught world a bunch (thousands) of particles.
#   Each particle represents an x,y coordinate & a heading.
#   As robot moves / observes; discard particles that don't match
#   up with robots oberstaionts / measurements.
#   Whats lef is a set of particles that well represent the robots
#   position and heading. This is the postiior distribution of the 
#   robot. This is a method of localization. 
#   Particle filters are: Continous, multimodal, approximate, either
#   exponential or quadratic in scale (4d max, more Kalman filter
#   better), but easy to program

