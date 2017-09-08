# 利用Matplotlib绘制甘特图
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import datetime

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

def getDays(year, month, day):
    targetDay = datetime.date(year, month, day)
    dayCount = targetDay - datetime.date(year - 1, 12, 31)
    return dayCount.days

task = (
        u'生物质炉排炉',          # id = 0
        u'山东潍坊',              # id = 1
        u'沈阳大辛',              # id = 2
        u'小型焚烧炉',            # id = 3
       )
y = np.arange(len(task))

fig, ax = plt.subplots()

today = (2017, 9, 5)

start = (
         (2017,  1,  1),
         (2017,  4, 21),
         (2017,  8, 15),
         (2017,  8, 30),
        )

end = (
       (2017, 6, 30),
       today,
       today,
       today,
)

color = ('salmon', 'royalblue')
state = (
         color[1],
         color[0],
         color[0],
         color[0],
)

for i,v in enumerate(start):
    ax.plot((getDays(start[i][0], start[i][1], start[i][2]), getDays(end[i][0], end[i][1], end[i][2])), (i, i), state[i], linewidth=30)


ax.set_xticks([1, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365])
ax.set_xticklabels([u'1月', u'2月', u'3月', u'4月', u'5月', u'6月', u'7月', u'8月', u'9月', u'10月', u'11月', u'12月', u'1月'])
ax.set_yticks(y)
ax.set_yticklabels(task)

ax.set_title('2017研发任务情况')

plt.ylim([-1, len(task)])
plt.xlim([1, 365])

plt.text(280, -0.8, u'红色：还在进行', ha='left', color='salmon')
plt.text(280, -0.5, u'蓝色：已完结', ha='left', color='royalblue')

for i,v in enumerate(start):
    x_center = (getDays(start[i][0], start[i][1], start[i][2]) + getDays(end[i][0], end[i][1], end[i][2]))/2.0
    plt.text(x_center, i-0.03, u'%d月%d日--%d月%d日' % (start[i][1], start[i][2], end[i][1], end[i][2]), ha='center', color='black')

plt.grid(linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig('2017.pdf', dpi=300)
plt.show()
