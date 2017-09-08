import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'  


eps = 1.0e-6
filename1 = 'm01_1400kcal_rad.xy'
filename2 = 'ori_1400kcal_rad.xy'

def orgData(data):
    tmp_x = []
    for i,v in enumerate(data):
        if v.split('\t')[0] not in tmp_x:
            tmp_x.append(v.split('\t')[0])
    tmp_x.sort()
            
    ny = []
    y = []
    for i,v in enumerate(tmp_x):
        ny.append(0)
        y.append(0)
        
    for i,v in enumerate(data):
        j = tmp_x.index(v.split('\t')[0])
        ny[j] += 1
        y[j] += float(v.split('\t')[1])
        
    for i,v in enumerate(y):
        y[i] = v/ny[i]
        
    x = []
    for i,v in enumerate(tmp_x):
        x.append(float(v))
        
    return x,y
    

def readFile(filename):
    f = open(filename, 'r')
    lines  = f.readlines()
    f.close()
    
    tmp = []
    for i,v in enumerate(lines):
        if '(' in v or ')' in v or v.strip() == '':
            pass
        else:
            tmp.append(v.strip())
              
    return tmp
    
def writeFile(filename_out, x, y):
    f = open(filename_out, 'w')
    for i,v in enumerate(x):
        f.write('%f,%f\n' % (x[i], y[i]))
    f.close()
    
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
    plt.xlim(0, 12)
    plt.ylim(800, 1400)
    plt.xlabel(u'炉排长度 [m]')
    plt.ylabel(u'辐射温度 [K]')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    

if __name__ == '__main__':
    main()
