import matplotlib.pyplot as plt

"""要绘制单个点，可使用方法scatter() 。向它传递一对 坐标和 坐标，它将在指
定位置绘制一个点："""

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=24)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()