from plot_radiation_temperature import *

filename1 = 'm01_1400kcal.xy'
filename2 = 'ori_1400kcal.xy'

def main():
    tmp = readFile(filename1)
    x,y = orgData(tmp)
    
    plot_data1 = []
    for i,v in enumerate(x):
        plot_data1.append([x[i], y[i]])
    plot_data1.sort()
    plot_data1 = np.array(plot_data1)
    
    tmp = readFile(filename2)
    x,y = orgData(tmp)
    
    plot_data2 = []
    for i,v in enumerate(x):
        plot_data2.append([x[i], y[i]])
    plot_data2.sort()
    plot_data2 = np.array(plot_data2)
    
    plt.plot(plot_data1[:, 0], plot_data1[:, 1], 'bo-', label = u'去鼻子')
    plt.plot(plot_data2[:, 0], plot_data2[:, 1], 'ro-', label = u'原始设计')
    plt.xlabel(u'水平方向 [m]')
    plt.ylabel(u'烟气温度 [K]')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    
if __name__ == '__main__':
    main()