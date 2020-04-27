import sys
import numpy as np
from numpy import pi
from numpy.linalg import eig
import matplotlib.pyplot as plt
sys.path.append("..")
from week2.exercise_C import matrix_animation
if __name__ == '__main__':
    xdata, ydata = [0,0,1,1,2,3], [0,1,1,0,2,1]
    wow = matrix_animation(xdata,ydata,[(0,1,1,2,1,0,0)]) # so it can be seen that translation may distort the eigen vector here in 2D space.
    matrix = wow.matrices_set[0]
    val,vec = eig(matrix)
    x1 = [vec[0,0],0]
    y1 = [vec[1,0],0]
    x2 = [vec[0,1],0]
    y2 = [vec[1,1],0]
    wow.add_points(x1,y1,'g-')
    wow.add_points(x2,y2,'b-')
    wow.animate_plot()