import matplotlib
import numpy as np
from matplotlib import pyplot as plt


if __name__ == "__main__":
    #print("Hello world")
    #print(matplotlib.__version__)

    #print(plt.style.available)
    plt.style.use('seaborn')

    x = [0, 1, 2, 3, 4, 5, 6, 7]
    y = [1, 4, 5, 5, 6, 7, 8, 10]
    z = np.array(y)*7

    plt.scatter(x,y, s=100, c = x, cmap = 'Greens')

    #plt.plot(x, y, linestyle='--', label = 'All Devs')
    #plt.bar(x,z, linewidth=2, label = 'Python')

    plt.grid(True)
    plt.xlabel('Ages')
    plt.ylabel('Salary')
    plt.title('Random Data shown with MatPlotLib')
    plt.legend()
    plt.tight_layout()

    plt.savefig('plot.png')
    
    plt.show()
