import numpy as np
from matplotlib import pyplot as plt

def initialize_point():
    x=np.random.randint(-15,15,size=(2,100))
    print(x)
    return x

def plot_point(x):
    for i in range(len(x)):
        plt.scatter(x[i,0],x[i,1])
    plt.show()

def plot_line(Feature_Vector,initial_point):
    k= Feature_Vector[1]/Feature_Vector[0] #k 斜率
    x = np.array([-15,15])
    y = x*k
    print(x)
    plt.plot(x,y,color='red')
    for i in range(initial_point.shape[1]):
        plt.scatter(initial_point[0,i],initial_point[1,i],color='blue')

        x1 = (k * (initial_point[1,i]) + initial_point[0,i]) / (k * k + 1);
        y1 = k * x1;
        print("x1 = ",format(x1))
        print("y1 = ",format(y1))
        plt.scatter(x1,y1)
    plt.show()



if __name__ == '__main__':
    initial_point=initialize_point()
    #未零均值化
    # plot_point(initial_point)
    cov_mat = np.cov(initial_point) #协方差矩阵
    print("cov_mat = ",format(cov_mat))
    Feature_Vector, Feature_Value = np.linalg.eig(cov_mat)
    print("feature_vector=",format(Feature_Vector))
    plot_line(Feature_Vector.real,initial_point)






