import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
class matrix_animation:
    def __init__(self,xdata,ydata,transformation,color='ro',fig=None,ax=None):
        self.xdata = [xdata]
        self.ydata = [ydata]
        matrices_set = []
        for order,i in enumerate(transformation): 
            print(len(i))
            assert len(i) == 7 ,"not enough parameters for the %d-th transformation\n.Usage: rotation ( radian),scale_x,scale_y,translate_x,translate_y,shear_x,shear_y" %(order+1)
            matrix = self.transform_maker(rotation=i[0],scale_x = i[1],scale_y =i[2],translate = [i[3],i[4]],shear=[i[5],i[6]]) # try changing the parameters here
            matrices_set += matrix
            print("ok")
        self.matrices_set = matrices_set
        print("fig,as is",fig,ax)
        if fig == None or ax == None:
            self.fig, self.ax = plt.subplots()
        else:
            self.fig, self.ax = fig,ax
        ln, = self.ax.plot([], [], 'ro')
        self.ln = [ln]
        self.ax.grid(b=True)

    def add_points(self,xdata,ydata,color):
        ln, = self.ax.plot([],[],color)
        self.ln.append(ln)
        self.xdata.append(xdata)
        self.ydata.append(ydata)     
        print(self.xdata)
    def init(self):
        self.ax.set_xlim(-4,4)
        self.ax.set_ylim(-4,4)
        print(self.ln)
        return self.ln

    def update(self,frame):
        #frame must be a set of matrices, maybe around 50 matrices?
        for i in range(len(self.ln)):
            print(i)
            self.xdata[i] = np.reshape(self.xdata[i],(1,-1))
            self.ydata[i] = np.reshape(self.ydata[i],(1,-1))
            dummy_dim = np.ones(shape = (1,self.xdata[i].shape[1]))
            vector = np.concatenate((self.xdata[i],self.ydata[i],dummy_dim),axis = 0)
            vector = np.dot(frame,vector)
            self.xdata[i] = vector[0] / vector[2]
            self.ydata[i] = vector[1] / vector[2]
            self.ln[i].set_data(self.xdata[i],self.ydata[i])
        return self.ln
    def transform_maker(self,rotation,scale_x,scale_y,translate,shear):
        lists = []
        n_iter = 20
        rotation /= n_iter
        scale_x = scale_x ** (1/n_iter)
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
    def animate_plot(self):
        ani = FuncAnimation(self.fig,self.update,frames=self.matrices_set,init_func=self.init, blit=True,repeat=False)
        plt.show()

if __name__ == '__main__':
    xdata, ydata = [0,0,1,1,0], [0,1,1,0,0] # need to think of a way to put self.xdata and ydata in animate_plot
    wow = matrix_animation(xdata,ydata,[(pi/2,1,1,1,1,0,0)])
    wow.animate_plot()

