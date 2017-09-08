import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

### Input data ###

B = 750.0/24.0      # t/h
Q = 1600.0          # kcal/kg
LHV_list = [1500, 1400, 1300, 1200, 1000]       # kcal/kg, will be display by dash line, 1200 & 1000 must be include


###############################
### no need to modify below ###
###############################

### step 1: calculate points ###
MCR_y = B*1000/3600*Q*4.1868/1000       # MW 
npoints = 12+1
p = []
for i in range(npoints):
    p.append(0)
p[1] = (B, MCR_y)
p[2] = (B*Q/2400, MCR_y)
p[3] = (B*0.6, MCR_y*0.6*2400/Q)
p[4] = (p[1][0]*0.6, p[1][1]*0.6)
p[5] = (B*Q/1200*0.6, MCR_y*0.6)
p[6] = (B, MCR_y*1200/Q)
p[7] = (B*1.1, p[6][1]*1.1)
p[8] = (p[1][0]*1.1, p[1][1]*1.1)
p[9] = (p[2][0]*1.1, p[2][1]*1.1)
p[10] = (p[2][0]*1.2, p[2][1]*1.2)
p[11] = (p[1][0]*1.2, p[1][1]*1.2)
p[12] = (p[6][0]*1.2, p[6][1]*1.2)

###############################
### plot combustion diagram ###
###############################

fig = plt.figure()
plt.xlim(B*0.4, B*1.4)
plt.ylim(MCR_y*0.4, MCR_y*1.4)
plt.xlabel(u"垃圾处理量 [t/h]")
plt.ylabel(u"输入热量 [MW]")

### step 1: plot points ###
x = []
y = []
for i in range(1,7):
    x.append(p[i][0])
    y.append(p[i][1])

plt.plot(x,y,'bo')

x = []
y = []
for i in range(7,npoints):
    x.append(p[i][0])
    y.append(p[i][1])
plt.plot(x,y,'ro')

### step 2: plot dash line for different LHV ###
plt.plot((0,p[10][0]*1.03), (0,p[10][1]*1.03), 'k--', linewidth=0.5)
plt.plot((0,p[11][0]*1.03), (0,p[11][1]*1.03), 'k--', linewidth=0.5)
for i in LHV_list:
    plt.plot((0,B*1.2*1.03), (0,MCR_y*1.2*i/Q*1.03), 'k--', linewidth=0.5)


### step 3: other dash line ###
### horizental ###
plt.plot((0,p[ 4][0]), (p[ 4][1],p[ 4][1]), 'k--', linewidth=0.5)
plt.plot((0,p[ 1][0]), (p[ 1][1],p[ 1][1]), 'k--', linewidth=0.5)
plt.plot((0,p[ 8][0]), (p[ 8][1],p[ 8][1]), 'k--', linewidth=0.5)
plt.plot((0,p[11][0]), (p[11][1],p[11][1]), 'k--', linewidth=0.5)
### vertical ###
plt.plot((p[ 4][0],p[ 4][0]), (0,p[ 4][1]), 'k--', linewidth=0.5)
plt.plot((p[ 1][0],p[ 1][0]), (0,p[ 1][1]), 'k--', linewidth=0.5)
plt.plot((p[ 8][0],p[ 8][0]), (0,p[ 8][1]), 'k--', linewidth=0.5)
plt.plot((p[11][0],p[11][0]), (0,p[11][1]), 'k--', linewidth=0.5)


### step 4: shadow fill and dash line###
fp1 = (B*Q*0.6/1000, MCR_y*0.6)
fp2 = (B*Q*0.6/1000, MCR_y*0.6*1200/1000)
fp3 = (B*1.2, MCR_y*1.2*1000/Q)
fp4 = (B, MCR_y*1000/Q)
fp5 = (B*1.1, MCR_y*1.1*1000/Q)

y1 = (p[5][1],p[5][1])
y2 = (p[5][1],fp2[1])
plt.fill_between((p[5][0],fp1[0]), y2, y1, color='yellow', alpha=0.3)
y1 = (fp1[1],fp3[1])
y2 = (fp2[1],p[12][1])
plt.fill_between((fp1[0],fp3[0]), y2, y1, color='yellow', alpha=0.3)
plt.plot((p[5][0],fp1[0]), (p[5][1],fp1[1]), 'k--', linewidth=0.5)


### step 5: color line ###
### blue zone ###
plt.plot((p[1][0],p[2][0]), (p[1][1],p[2][1]), color='b', linewidth=2)
plt.plot((p[2][0],p[3][0]), (p[2][1],p[3][1]), color='b', linewidth=2)
plt.plot((p[3][0],p[4][0]), (p[3][1],p[4][1]), color='b', linewidth=2)
plt.plot((p[4][0],p[5][0]), (p[4][1],p[5][1]), color='b', linewidth=2)
plt.plot((p[5][0],p[6][0]), (p[5][1],p[6][1]), color='b', linewidth=2)
plt.plot((p[6][0],p[1][0]), (p[6][1],p[1][1]), color='b', linewidth=2)
### red zone ###
plt.plot((p[ 2][0],p[10][0]), (p[ 2][1],p[10][1]), 'r--', linewidth=2)
plt.plot((p[10][0],p[11][0]), (p[10][1],p[11][1]), 'r--', linewidth=2)
plt.plot((p[11][0],p[12][0]), (p[11][1],p[12][1]), 'r--', linewidth=2)
plt.plot((p[12][0],p[ 6][0]), (p[12][1],p[ 6][1]), 'r--', linewidth=2)
plt.plot((p[ 9][0],p[ 8][0]), (p[ 9][1],p[ 8][1]), 'r--', linewidth=2)
plt.plot((p[ 8][0],p[ 7][0]), (p[ 8][1],p[ 7][1]), 'r--', linewidth=2)

### step 6: text ###
### marker ###
for i in range(1,npoints):
    plt.text(p[i][0]-0.5, p[i][1], i, ha='right')
### load ###
plt.text(B*0.4+0.15, MCR_y*0.6+0.8, "%5.2fMW(60%%)" %(MCR_y*0.6), ha='left')
plt.text(B*0.4+0.15, MCR_y    +0.8, "%5.2fMW(100%%)"%(MCR_y)    , ha='left')
plt.text(B*0.4+0.15, MCR_y*1.1+0.8, "%5.2fMW(110%%)"%(MCR_y*1.1), ha='left')
plt.text(B*0.4+0.15, MCR_y*1.2+0.8, "%5.2fMW(120%%)"%(MCR_y*1.2), ha='left')
plt.text(B*0.6-0.15, MCR_y*0.4+0.8, "%5.2ft/h(60%%)" %(B*0.6), ha='left', rotation=90, wrap=True)
plt.text(B    -0.15, MCR_y*0.4+0.8, "%5.2ft/h(100%%)"%(B    ), ha='left', rotation=90, wrap=True)
plt.text(B*1.1-0.15, MCR_y*0.4+0.8, "%5.2ft/h(110%%)"%(B*1.1), ha='left', rotation=90, wrap=True)
plt.text(B*1.2-0.15, MCR_y*0.4+0.8, "%5.2ft/h(120%%)"%(B*1.2), ha='left', rotation=90, wrap=True)
### LHV ###
plt.text(p[10][0]*1.03, p[10][1]*1.03, "2400kcal/kg", ha='left')
plt.text(p[11][0]*1.03, p[11][1]*1.03, "%04dkcal/kg" % Q, ha='left')
for i in LHV_list:
    plt.text(B*1.2*1.03, MCR_y*1.2*i/Q*1.03, "%04dkcal/kg" % i, ha='left')
### others ###
plt.text(B*0.4*1.03, MCR_y*1.4*0.97, u"正常运行区域：1-2-3-4-5-6-1", ha='left', color='b')
plt.text(B*0.4*1.03, MCR_y*1.4*0.94, u"超负荷运行区域：1-2-10-11-12-6-1", ha='left', color='r')
plt.text(B*0.4*1.03, MCR_y*1.4*0.91, u"投入辅燃区域：黄色阴影区域", ha='left', color='y')


###########################
### plot and save image ###
###########################
plt.tight_layout()
plt.savefig('combustion_diagram_sample_for_low_LHV.png', dpi=300)
plt.show()