import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
xdata, ydata = [0,0,1,1,0], [0,1,1,0,0] # need to think of a way to put xdata and ydata in animate_plot
def transform_maker(rotation,scale_x,scale_y,translate,shear):
    lists = []
    n_iter = 20
    rotation /= n_iter
    scale_x = scale_x ** (1/n_iter)
    print("wow",scale_x)
    scale_y = scale_y ** (1/n_iter)
    translate[0] /=  n_iter
    translate[1] /= n_iter
    shear[0] /= n_iter
    shear[1] /= n_iter
    rot_matrix = np.matrix([[np.cos(rotation),np.sin(rotation),translate[0]],
                        [-(np.sin(rotation)),np.cos(rotation),translate[1]],
                       [0,0,1]])
    scale_matrix = np.matrix([[scale_x,scale_x*np.tan(shear[0]),0],
                              [scale_y*np.tan(shear[1]),scale_y,0],
                              [0,0,1]])
    matrix = rot_matrix*scale_matrix
    for i in range(n_iter):
        lists.append(matrix)
    return lists
def animate_plot(*args):
    fig, ax = plt.subplots()
    ln, = plt.plot([], [], 'r-')
    def init():
        ax.set_xlim(-4,4)
        ax.set_ylim(-4,4)
        return ln,

    def update(frame):
        global xdata,ydata
        #frame must be a set of matrices, maybe around 50 matrices?
        xdata = np.reshape(xdata,(1,-1))
        ydata = np.reshape(ydata,(1,-1))
        dummy_dim = np.ones(shape = (1,xdata.shape[1]))
        vector = np.concatenate((xdata,ydata,dummy_dim),axis = 0)
        vector = np.dot(frame,vector)
        xdata = vector[0] / vector[2]
        print(xdata)
        ydata = vector[1] / vector[2]
        ln.set_data(xdata,ydata)
        return ln,
    matrices_set = []
    for i in args: 
        assert len(i) == 7 ,"not enough parameters for the %d transformation\n.Usage: rotation ( radian),scale_x,scale_y,translate_x,translate_y,shear_x,shear_y" %(i)
        matrix = transform_maker(rotation=i[0],scale_x = i[1],scale_y =i[2],translate = [i[3],i[4]],shear=[i[5],i[6]]) # try changing the parameters here
        matrices_set += matrix
    ani = FuncAnimation(fig, update,frames=matrices_set,init_func=init, blit=True,repeat=False)
    plt.show()

if __name__ == '__main__':
    animate_plot((pi/2,1,1,1,1,0,0))

