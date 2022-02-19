function nlp2021flg
clear all
clc
k0 = [0.01  0.01 ];         % 参数初值
lb = [0  0  ];                   % 参数下限 
ub = [100  100 ];    % 参数上限
C1 = [7.31185	1.88464	 0    	0 ];
C2 = [6.9822	2.2737	0	   0];
C3 = [6.5934	2.6423	0	   0 ];
C4 = [6.2231	3.0287	0   	0 ];
data1=...
[0	7.31185	1.88464	0    	0
1	6.8632	1.2719	0.4436	0.5488
2	6.6416	0.924	0.7367	0.8915
4	6.4409	0.7575	0.8653	1.0397];
data2=...
[0	6.9822	2.2737	0	   0
1	6.521	1.5196	0.4751	0.6769
2	6.2025	1.006	0.8378	1.1511
4	5.9112	0.807	1.0784	1.3857];

data3=...
[0	6.5934	2.6423	0	   0
1	5.9143	1.529	0.6559	0.9164
2	5.6045	1.0549	1.0119	1.4392
4	5.2802	0.7011	1.2785	1.7571];
data4=...
[0	6.2231	3.0287	0   	0
1	5.4561	1.6336	0.7682	1.2778
2	5.1018	1.0246	1.1125	1.8031
4	4.7369	0.7007	1.4452	2.123];

%data1=...
[0	7.31185	1.88464	0    	0
1	6.8632	1.2719	0.4436	0.5488
2	6.6416	0.924	0.7367	0.8915
4	6.4409	0.7575	0.8653	1.0397
6	6.2566	0.5653	1.0296	1.2299
8	6.1677	0.4478	1.0951	1.3541];
%data2=...
[0	6.9822	2.2737	0	   0
1	6.521	1.5196	0.4751	0.6769
2	6.2025	1.006	0.8378	1.1511
4	5.9112	0.807	1.0784	1.3857
6	5.8516	0.5579	1.1386	1.4911
8	5.658	0.4816	1.2493	1.6555];

%data3=...
[0	6.5934	2.6423	0	   0
1	5.9143	1.529	0.6559	0.9164
2	5.6045	1.0549	1.0119	1.4392
4	5.2802	0.7011	1.2785	1.7571
6	5.1936	0.5906	1.3844	1.8703
8	5.0079	0.5123	1.4729	1.955];
%data4=...
[0	6.2231	3.0287	0   	0
1	5.4561	1.6336	0.7682	1.2778
2	5.1018	1.0246	1.1125	1.8031
4	4.7369	0.7007	1.4452	2.123
6	4.664	0.5135	1.456	2.2629
8	4.5283	0.4719	1.6222	2.3084];



%format long
yexp1 =data1(:,2:5) 
yexp2 =data2(:,2:5)
yexp3 =data3(:,2:5)
yexp4 =data4(:,2:5)





% yexp: 实验数据[CA	CB	CC CD]
% 使用函数fmincon()进行参数估计
[k,fval,flag] = fmincon(@ObjFmc,k0,[],[],[],[],lb,ub,[],[],C1,C2,C3,C4,yexp1,yexp2,yexp3,yexp4);
fprintf('\n使用函数fmincon()估计得到的参数值为:\n')
fprintf('\tk1 = %.6f\n',k(1))
fprintf('\tk2 = %.6f\n',k(2))
fprintf('  The sum of the squares is: %.3e\n\n',fval)
tspan = [0 1 2 4 ];
%k=[0.2 0.3]
%k(2)=0.043
%k(1)=0.030
[t C] = ode45(@KDEs,tspan,C1,[],k);
disp(C)
disp(yexp1)
ty=yexp1(:,1)+yexp1(:,2)+yexp1(:,3)+yexp1(:,4)
plot(tspan,yexp1(:,1),'*b',tspan,yexp1(:,2),'vb',tspan,yexp1(:,3),'^b',tspan,yexp1(:,4),'+b',tspan,ty,'ob-','linewidth',2);
hold on;
plot(tspan,C(:,1),'r-',tspan,C(:,2),'k-',tspan,C(:,3),'m-',tspan,C(:,4),'g-','linewidth',2);% 绘图
xlabel('时间 (min)');
ylabel('浓度 (kmol/m^3)');
legend('A','B','C','D');grid on
figure




[t C] = ode45(@KDEs,tspan,C2,[],k);
disp(C)
disp(yexp2)
ty=yexp2(:,1)+yexp2(:,2)+yexp2(:,3)+yexp2(:,4)
plot(tspan,yexp2(:,1),'*b',tspan,yexp2(:,2),'vb',tspan,yexp2(:,3),'^b',tspan,yexp2(:,4),'+b',tspan,ty,'ob-','linewidth',2);
hold on;
plot(tspan,C(:,1),'r-',tspan,C(:,2),'k-',tspan,C(:,3),'m-',tspan,C(:,4),'g-','linewidth',2);% 绘图
xlabel('时间 (min)');
ylabel('浓度 (kmol/m^3)');
legend('A','B','C','D');hold on;grid on



[t C] = ode45(@KDEs,tspan,C3,[],k);
disp(C)
disp(yexp3)

figure
ty=yexp3(:,1)+yexp3(:,2)+yexp3(:,3)+yexp3(:,4)
plot(tspan,yexp3(:,1),'*b',tspan,yexp3(:,2),'vb',tspan,yexp3(:,3),'^b',tspan,yexp3(:,4),'+b',tspan,ty,'ob-','linewidth',2);
hold on;
plot(tspan,C(:,1),'r-',tspan,C(:,2),'k-',tspan,C(:,3),'m-',tspan,C(:,4),'g-','linewidth',2);% 绘图
xlabel('时间 (min)');
ylabel('浓度 (kmol/m^3)');
legend('A','B','C','D');hold on;grid on



[t C] = ode45(@KDEs,tspan,C4,[],k);
disp(C)
disp(yexp4)
figure
ty=yexp4(:,1)+yexp4(:,2)+yexp4(:,3)+yexp4(:,4)
plot(tspan,yexp4(:,1),'*b',tspan,yexp4(:,2),'vb',tspan,yexp4(:,3),'^b',tspan,yexp4(:,4),'+b',tspan,ty,'ob-','linewidth',2);
hold on;
plot(tspan,C(:,1),'r-',tspan,C(:,2),'k-',tspan,C(:,3),'m-',tspan,C(:,4),'g-','linewidth',2);% 绘图
xlabel('时间 (min)');
ylabel('浓度 (kmol/m^3)');
legend('A','B','C','D');hold on;grid on





% ------------------------------------------------------------------
function f = ObjFmc(k,C1,C2,C3,C4,yexp1,yexp2,yexp3,yexp4)
tspan = [0 1 2 4 ];
[t C] = ode45(@KDEs,tspan,C1,[],k);   
f1 = sum((C(:,1)-yexp1(:,1)).^2) + sum((C(:,2)-yexp1(:,2)).^2)+ sum((C(:,3)-yexp1(:,3)).^2+sum((C(:,4)-yexp1(:,4)).^2));

[t C] = ode45(@KDEs,tspan,C2,[],k);   
f2 = sum((C(:,1)-yexp2(:,1)).^2) + sum((C(:,2)-yexp2(:,2)).^2)+ sum((C(:,3)-yexp2(:,3)).^2+sum((C(:,4)-yexp2(:,4)).^2));

[t C] = ode45(@KDEs,tspan,C3,[],k);   
f3 = sum((C(:,1)-yexp3(:,1)).^2) + sum((C(:,2)-yexp3(:,2)).^2)+ sum((C(:,3)-yexp3(:,3)).^2+sum((C(:,4)-yexp3(:,4)).^2));

[t C] = ode45(@KDEs,tspan,C4,[],k);   
f4 = sum((C(:,1)-yexp4(:,1)).^2) + sum((C(:,2)-yexp4(:,2)).^2)+ sum((C(:,3)-yexp4(:,3)).^2+sum((C(:,4)-yexp4(:,4)).^2));

f=(f1+f2+f3+f4)/(4*24);

% ------------------------------------------------------------------


% ------------------------------------------------------------------
function dC =KDEs(t,C,k)
dCA=-k(2)*C(1)*C(2);
dCB =-k(1)*C(2)- k(2)*C(1) *C(2);
dCD =k(1)*C(2) + k(2)*C(1) *C(2);
dCC= k(2)*C(1) *C(2);
dC = [dCA; dCB; dCC; dCD]; 