import numpy as np
from sko.SA import SA
from sko.PSO import PSO
from sko.DE import DE
from sko.GA import GA
from scipy.optimize import fmin_bfgs,minimize

import time

class OPT:
    def __init__(self,funcstr,xstr,constrain_eqstr="",constrain_uneqstr="",lb=[0,0],ub=[1,1]):

        self.func=self.GetFunc(funcstr,xstr)
        self.xstr = xstr.split(',')  # 自变量名字
        self.n_dim = len(self.xstr)
        self.ConstrainInital(constrain_eqstr, 0)
        self.ConstrainInital(constrain_uneqstr, 1)
        self.lb=lb
        self.ub=ub



    def GetFunc(self,parameterstr, xstr):
            parameterstr = parameterstr.replace(" ", "")


            parameters = []
            i = 0  # 参数个数计数
            for p in parameterstr.splitlines():
                p = p.strip()
                if not p:
                    continue

                temp = p.split('=')
                parameters.append(temp)
                i = i + 1

            def Objective(x):
                para = []
                for idx in range(len(parameters)):
                    ret = parameters[idx][1]
                    if self.xstr != ['x']:  # 单变量不用替换
                        for m, zibianliang in enumerate(self.xstr):  # 自变量替换
                            ret = ret.replace(zibianliang, "x[" + str(m) + "]")
                    for k in range(idx):  # 检查当前语句有没有用到上一些语句中定义的参数
                        ret = ret.replace(parameters[k][0], "para[" + str(k) + "]")  # 文本处理后的待执行指令

                    para.append(eval(ret))

                return para[idx]  # 最后一个“参数”就是我们要返回的函数值

            return Objective

    def getf(self,str):
        def f(x):
            return eval(str)
        return f

    def ConstrainInital(self,constrain_str,type):
        ret = []
        if(constrain_str!=""):
            constrain_str= constrain_str.replace(" ", "")
            parts=constrain_str.splitlines()

            for idx in range(len(parts)):
                line=parts[idx]
                for k in range(self.n_dim):
                    line=line.replace(self.xstr[k],"x["+str(k)+"]")
                print(line)
                ret.append(self.getf(line))

        if(type==0):
            self.eq_condition=ret
        else:
            self.uneq_condition=ret


    def GARun(self,size_pop=50,max_iter=800,precision=1e-7,prob_mut=0.001):


        start = time.time()
        ga = GA(func=self.func, n_dim=self.n_dim, size_pop=size_pop, prob_mut=prob_mut,max_iter=max_iter, lb=self.lb,
                ub=self.ub, precision= precision, constraint_ueq=self.uneq_condition, constraint_eq=self.eq_condition)
        best_x, best_y = ga.run()

        print('遗传算法：best_x:', best_x, '\n', 'best_y:', best_y)

        end = time.time()
        print("用时：" + str(end - start))
        self.CheckConstrain(best_x)
        print('------------------------------------------------------------')



    def PSORun(self,pop=100,max_iter=150,lb=[0,0],ub=[1,1],w=0.8,c1=0.5,c2=0.5):

        time_start = time.time()

        pso = PSO(func=self.func, n_dim=self.n_dim, pop=pop, max_iter=max_iter, lb=self.lb, ub=self.ub, w=w, c1=c1, c2=c2,constraint_ueq=self.uneq_condition,constraint_eq=self.eq_condition)
        pso.run()



        print('粒子群算法:best_x is ', pso.gbest_x, 'best_y is', pso.gbest_y)
        time_end = time.time()
        print("耗时：" + str(time_end - time_start))
        self.CheckConstrain(pso.gbest_x)

        print('------------------------------------------------------------')


    def DERun(self,size_pop=50,max_iter=800,prob_mut=0.001,F=0.5):
        time_start = time.time()
        de = DE(func=self.func, n_dim=self.n_dim, size_pop=size_pop, max_iter=max_iter, lb=self.lb, ub=self.ub,
                constraint_eq=self.eq_condition, constraint_ueq=self.uneq_condition,prob_mut=prob_mut,F=F)

        best_x, best_y = de.run()

        print('差分进化算法:best_x is ', best_x, 'best_y is', best_y)

        time_end = time.time()
        print("耗时：" + str(time_end - time_start))
        self.CheckConstrain(best_x)
        print('------------------------------------------------------------')



    def SARun(self,x0=[1,1],T_max=100,T_min=1e-9,L=300,max_stay_counter=150):
        time_start = time.time()

        sa = SA(func=self.func, x0=x0, T_max=T_max, T_min=T_min, L=L, max_stay_counter=max_stay_counter,constrain_eq=self.eq_condition,constrain_ueq=self.uneq_condition)


        best_x, best_y = sa.run()

        print('模拟退火算法:best_x is ', best_x, 'best_y is', best_y)

        time_end = time.time()
        print("耗时：" + str(time_end - time_start))
        self.CheckConstrain(best_x)
        print('------------------------------------------------------------')

    def BFGSRun(self,x0):
        return fmin_bfgs(func,x0)




    def CheckConstrain(self,x):
        Q_eq=0
        Q_uneq=0
        for i in range(len(self.eq_condition)):
            Q_eq+=self.eq_condition[i](x) ** 2
        print(Q_eq)

        for i in range(len(self.uneq_condition)):
            print(self.uneq_condition[i](x))







    # condition=(lambda x:x[0]-x[1],lambda x:x[1]-500,lambda x:-(3600-12*x[0]),lambda x:-(3200-8*x[1]))
    # eq_condition = [lambda x: x[0] + k1 * x[0] * x[4] - 1,
    #                 lambda x: x[1] - x[0] + k2 * x[1] * x[5],
    #                 lambda x: x[2] + x[0] + k3 * x[2] * x[4] - 1,
    #                 lambda x: x[3] - x[2] + x[1] - x[0] + k4 * x[3] * x[5],)
    # uneq_condition = (lambda x: x[4] ** 0.5 + x[5] ** 0.5 - 4]
    #
    # def func2(x0):
    #     x1, x2, x3, x4, x5, x6 = x0
    #     return -x4
from PyQt5.QtCore import QThread
class Thread(QThread):
    def __init__(self,opt,type):
        super(Thread,self).__init__()
        self.opt=opt
        self.type=type
    def run(self):#type=0:GA,type=1:PSO


        if (self.type == 0):
            self.opt.GARun()
        elif (self.type == 1):
            self.opt.PSORun()





if __name__ == '__main__':
    from scipy.optimize import fsolve
    import sys


    from PyQt5.QtWidgets import QApplication
    app=QApplication(sys.argv)
    uneq_condition = ""
    eq_condtion=""


    from numpy import log10



    fstr="f(x)=(9.81*4.5+3820/950-(y*35/0.04+1+0.5)*x**2*0.5)**2+(1/(y)**0.5-2*log10(0.04/0.0002)-1.14+2*log10(1+9.35*(0.04/0.0002)*0.00124/((0.04*x*950)*y**0.5)))**2"


    opt = OPT(fstr, "x,y",lb=[0,0], ub=[10,0.1],constrain_eqstr=eq_condtion,constrain_uneqstr=uneq_condition)
    for i in range(5):
        opt.DERun()
        opt.GARun()

    # thread_GA=Thread(opt,0)
    # thread_GA.start()



    sys.exit(app.exec_())





    # eq_condition = "x1+ 0.09755988*x1*x5-1\nx2-x1+ 0.0965842812*x2*x6\nx3+x1+ 0.0391908*x3*x5-1\nx4-x3+x2-x1+ 0.038798891999999995*x4*x6"
    # uneq_condition = "x5**0.5+x6**0.5-4"






