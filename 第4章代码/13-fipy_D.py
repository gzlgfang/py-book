import fipy as fp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

font1 = {"family": "Times New Roman"}

import matplotlib

matplotlib.use("TkAgg")


# 设置刻度线朝内
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
mpl.rcParams["ytick.right"] = True
mpl.rcParams["xtick.top"] = True
# 全局设置字体
mpl.rcParams["font.sans-serif"] = ["FangSong"]  # 保证显示中文字
mpl.rcParams["axes.unicode_minus"] = False  # 保证负号显示
mpl.rcParams["font.size"] = 16  # 设置字体大小
mpl.rcParams["font.style"] = "oblique"  # 设置字体风格，倾斜与否
mpl.rcParams["font.weight"] = "normal"  # "normal",=500，设置字体粗细

nx = 200
ny = nx
dx = 0.01
dy = dx
L = dx * nx
mesh = fp.Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)
u0 = fp.CellVariable(name="u值求解结果", mesh=mesh, value=0.0)
u = u0
D = 10.0
eq = fp.TransientTerm() == fp.DiffusionTerm(coeff=D)
valueTopLeft = 30
valueBottomRight = 100
valueBottomLeft = 100
X, Y = mesh.faceCenters
facesTopLeft = (mesh.facesLeft & (Y >= L)) | (mesh.facesTop & (X <= L))
facesBottomRight = (mesh.facesRight & (Y <= L)) | (mesh.facesBottom & (X >= L))
facesBottomLeft = (mesh.facesLeft & (Y <= L)) | (mesh.facesLeft & (X >= L))
u.constrain(valueTopLeft, facesTopLeft)
u.constrain(valueBottomRight, facesBottomRight)
u.constrain(valueBottomLeft, facesBottomLeft)

# viewer =fp.Viewer(vars=u0, datamin=0., datamax=100)
# viewer.plot()
timeStepDuration = 0.1
# 10 * 0.9 * dx**2 / (2 * D)
steps = 8
for step in range(steps):
    eq.solve(var=u, dt=timeStepDuration)
    # viewer.plot()
# plt.figure()
fig, ax = plt.subplots(2, 4, figsize=(20, 4), num="8个时间步长的u值分布")
norm = mpl.colors.Normalize(0, 100)
x = np.arange(nx) * dx  # 长度位置，归一处理，从0开始，共101个点
y = np.arange(nx) * dy
X, Y = np.meshgrid(x, y)
u0 = fp.CellVariable(name="solution variable", mesh=mesh, value=0.0)
for i in range(1, 9):  # i取值为1-8，不包含9
    eq.solve(var=u0, dt=timeStepDuration)
    arr = np.zeros(len(u0))
    for j in range(len(u0)):
        arr[j] = u0[j]
    ar = arr.reshape(nx, ny)
    p = ax[i // 5, i - i // 5 * 4 - 1].pcolor(
        X, Y, ar, cmap=mpl.cm.jet, norm=norm, shading="auto"
    )  # pcolor绘制
    ax[i // 5, i - i // 5 * 4 - 1].set_title("时间=" + str(int(i * 0.1 * 10) / 10))
    ax[i // 5, i - i // 5 * 4 - 1].set_xticks([0, 0.5, 1.0, 1.5, 2])  # 设置纵轴刻度
    ax[i // 5, i - i // 5 * 4 - 1].set_yticks(
        [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2]
    )
    ax[i // 5, i - i // 5 * 4 - 1].set_xlabel("x", font1)
    ax[i // 5, i - i // 5 * 4 - 1].set_ylabel("y", font1)
# plt.tight_layout()#和上面adjust语句功能相同
cb = plt.colorbar(p, ax=ax[i // 5, i - i // 5 * 4 - 1])
cb.set_label("温度")

plt.show()
