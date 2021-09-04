#遗传算法
# 加载数据

load citys_data.mat
X=citys(:,:)
print
D=Distance(X);  %生成距离矩阵
N=size(D,1);    %城市个数
%% 遗传参数
ZQS=200;       %种群大小
MAXGEN=200;     %最大遗传代数
Pc=0.49;         %交叉概率
Pm=0.23;        %变异概率
GGAP=0.8;       %代沟
%% 初始化种群
GJ=InitZQ(ZQS,N);
%% 画出随机解的路径图
Drawway(GJ(1,:),X)
pause(0.001)
%% 输出随机解的路径和总距离
disp('初始种群中的一个随机值:')
OutputPath(GJ(1,:));
Rlength=PathLength(D,GJ(1,:));
disp(['总距离：',num2str(Rlength)]);
disp('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
%% 优化
gen=0;
figure;
hold on;box on
xlim([0,MAXGEN])
title('优化过程')
xlabel('代数')
ylabel('最优值')
ObjV=PathLength(D,GJ);  %计算路径长度
preObjV=min(ObjV);
while gen<MAXGEN
    %% 计算适应度
    ObjV=PathLength(D,GJ);  %计算路径长度
    % fprintf('%d   %1.10f\n',gen,min(ObjV))
    line([gen-1,gen],[preObjV,min(ObjV)]);pause(0.0001)
    preObjV=min(ObjV);
    FitnV=Fitness(ObjV);
    %% 选择
    SelCh=Select(GJ,FitnV,GGAP);
    %% 交叉操作
    SelCh=Recombin(SelCh,Pc);
    %% 变异
    SelCh=Mutate(SelCh,Pm);
    %% 逆转操作
    SelCh=Reverse(SelCh,D);
    %% 重插入子代的新种群
    GJ=Reins(GJ,SelCh,ObjV);
    %% 更新迭代次数
    suiji=gen;
    if suiji>100
        %if suiji/10==fix(suiji/10)
           NGJ=InitZQ(2,N);
          GJ=[GJ(1:end-2,:);NGJ];
        %end
    end    
    gen=gen+1 ;
  end
%% 画出最优解的路径图
ObjV=PathLength(D,GJ);  %计算路径长度
[minObjV,minInd]=min(ObjV);
Drawway(GJ(minInd,:),X)
%% 输出最优解的路径和总距离
disp('最优解:')
p=OutputPath(GJ(minInd,:));
disp(['总距离：',num2str(ObjV(minInd))]);
disp('-------------------------------------------------------------')
toc
%% 初始化种群
%输入：
% NIND：种群大小
% N：   个体染色体长度（这里为城市的个数）  
%输出：
%初始种群
function GJ=InitZQ(ZQS,N)
GJ=zeros(ZQS,N);%用于存储种群
for i=1:ZQS
    GJ(i,:)=randperm(N);%随机生成初始种群
end

%% 画路径函数
%输入
% Chrom  待画路径   
% X      各城市坐标位置

function Drawway(GJ,X)
GJ=[GJ GJ(1)];
figure
hold on
plot(X(GJ(:),1),X(GJ(:),2),'O-','color',[0.5,0,1]) %所有城市位置上画上“O"
plot(X(GJ(1),1),X(GJ(1),2),'rv','MarkerSize',10)
for i=1:size(X,1)
    text(X(i,1)-20,X(i,2)+60,num2str(i),'color',[1,0,0])
end 
text(X(GJ(1),1)+20,X(GJ(1),2)+150,'起点')
text(X(GJ(end-1),1)+20,X(GJ(end-1),2)+150,'终点')
A=X(GJ,:);
row=size(A,1);
for i=2:row
    [arrowx,arrowy] = dsxy2figxy(gca,A(i-1:i,1),A(i-1:i,2));%坐标转换
    annotation('textarrow',arrowx,arrowy,'HeadWidth',8,'color',[0,0,1]);
end
hold off

xlabel('横坐标')
ylabel('纵坐标')
title(' 轨迹图')
box on
grid on

% 计算城市i和城市j之间的距离
% 输入 zb 各城市的坐标,用zb(i,1:2)
% 输出 D 城市i和城市j之间的距离,用D(i,j)表示
function D=Distance(zb)
row=size(zb,1)   %   计算城市的数目
D=zeros(row,row);  %  产生两城市之间距离数据的空矩阵即零阵
  for i=1:row
      for    j=i+1:row 
             D(i,j)=sqrt((zb(i,1)-zb(j,1))^2+(zb(i,2)-zb(j,2))^2);
             D(j,i)=D(i,j);
      end      
  end

%% 输出路径函数
%输入：R 路径
function p=OutputPath(R)
R=[R,R(1)];
N=length(R);
p=num2str(R(1));
for i=2:N
    p=[p,'—>',num2str(R(i))];
end
disp(p)


% 计算轨迹GJ的长度     
function len=PathLength(D,GJ)
N=size(D,1);%   计算城市的数目
ZQS=size(GJ,1);
len= zeros(ZQS,1);
for i=1:ZQS
  for j=1:N-1
      len(i,1)=len(i,1)+D(GJ(i,j),GJ(i,j+1));
  end  
len(i,1)=len(i,1)+D(GJ(i,1),GJ(i,N));
end




%% 交叉操作
% 输入
%SelCh  被选择的个体
%Pc     交叉概率
%输出：
% SelCh 交叉后的个体
function SelCh=Recombin(SelCh,Pc)
NSel=size(SelCh,1);
for i=1:2:NSel-mod(NSel,2)
    if Pc>=rand %交叉概率Pc
        [SelCh(i,:),SelCh(i+1,:)]=intercross(SelCh(i,:),SelCh(i+1,:));
    end
end

%输入：
%a和b为两个待交叉的个体
%输出：
%a和b为交叉后得到的两个个体

function [a,b]=intercross(a,b)
L=length(a);
r1=randsrc(1,1,[1:L]);% 随机产生一个1：L的整数
r2=randsrc(1,1,[1:L]); % 随机产生一个1：L的整数
if r1~=r2
    a0=a;b0=b;
      if r1>r2 
          s=r2;e=r1;
      else
          s=r1;e=r2;
      end    
    
    for i=s:e
        a1=a;b1=b;
        a(i)=b0(i);
        b(i)=a0(i);
        x=find(a==a(i));
        y=find(b==b(i));
        i1=x(x~=i);
        i2=y(y~=i);
        if ~isempty(i1)
            a(i1)=a1(i);
        end
        if ~isempty(i2)
            b(i2)=b1(i);
        end
    end
end

%% 进化逆转函数
%输入
%SelCh 被选择的个体
%D     个城市的距离矩阵
%输出
%SelCh  进化逆转后的个体
function SelCh=Reverse(SelCh,D)
[row,col]=size(SelCh);
ObjV=PathLength(D,SelCh);  %计算路径长度
SelCh1=SelCh;
for i=1:row
    r1=randsrc(1,1,[1:col]);
    r2=randsrc(1,1,[1:col]);
    mininverse=min([r1 r2]);
    maxinverse=max([r1 r2]);
    SelCh1(i,mininverse:maxinverse)=SelCh1(i,maxinverse:-1:mininverse);
end
ObjV1=PathLength(D,SelCh1);  %计算路径长度
index=ObjV1<ObjV;
SelCh(index,:)=SelCh1(index,:);
%% 选择操作
%输入
%Chrom 种群
%FitnV 适应度值
%GGAP：代沟
%输出
%SelCh  被选择的个体
function SelCh=Select(Chrom,FitnV,GGAP)
NIND=size(Chrom,1);
NSel=max(floor(NIND*GGAP+.5),2);
ChrIx=Sus(FitnV,NSel);
SelCh=Chrom(ChrIx,:);
function SelCh=Select(Chrom,FitnV,GGAP)
NIND=size(Chrom,1);
NSel=max(floor(NIND*GGAP+.5),2);
ChrIx=Sus(FitnV,NSel);
SelCh=Chrom(ChrIx,:);
%% 适配值函数     
%输入：
%个体的长度（TSP的距离）
%输出：
%个体的适应度值

% 输入:
%FitnV  个体的适应度值
%Nsel   被选择个体的数目
% 输出:
%NewChrIx  被选择个体的索引号
function NewChrIx = Sus(FitnV,Nsel)
[Nind,ans] = size(FitnV);
cumfit = cumsum(FitnV);
trials = cumfit(Nind) / Nsel * (rand + (0:Nsel-1)');
Mf = cumfit(:, ones(1, Nsel));
Mt = trials(:, ones(1, Nind))';
[NewChrIx, ans] = find(Mt < Mf & [ zeros(1, Nsel); Mf(1:Nind-1, :) ] <= Mt);
[ans, shuf] = sort(rand(Nsel, 1));
NewChrIx = NewChrIx(shuf);

%% 变异操作
%输入：
%SelCh  被选择的个体
%Pm     变异概率
%输出：
% SelCh 变异后的个体
function SelCh=Mutate(SelCh,Pm)
[NSel,L]=size(SelCh);
for i=1:NSel
    if Pm>=rand
        R=randperm(L);
        SelCh(i,R(1:2))=SelCh(i,R(2:-1:1));
    end
end
%% 重插入子代的新种群
 %输入：
 %Chrom  父代的种群
 %SelCh  子代种群
 %ObjV   父代适应度
 %输出
 % Chrom  组合父代与子代后得到的新种群
function Chrom=Reins(Chrom,SelCh,ObjV)
NIND=size(Chrom,1);
NSel=size(SelCh,1);
[TobjV,index]=sort(ObjV);
Chrom=[Chrom(index(1:NIND-NSel),:);SelCh];



function FitnV=Fitness(len)
FitnV=1./len;
%   绘制箭头
function varargout = dsxy2figxy(varargin)
if length(varargin{1}) == 1 && ishandle(varargin{1}) ...
                            && strcmp(get(varargin{1},'type'),'axes')   
    hAx = varargin{1};
    varargin = varargin(2:end);
else
    hAx = gca;
end;
if length(varargin) == 1
    pos = varargin{1};
else
    [x,y] = deal(varargin{:});
end
axun = get(hAx,'Units');
set(hAx,'Units','normalized'); 
axpos = get(hAx,'Position');
axlim = axis(hAx);
axwidth = diff(axlim(1:2));
axheight = diff(axlim(3:4));
if exist('x','var')
    varargout{1} = (x - axlim(1)) * axpos(3) / axwidth + axpos(1);
    varargout{2} = (y - axlim(3)) * axpos(4) / axheight + axpos(2);
else
    pos(1) = (pos(1) - axlim(1)) / axwidth * axpos(3) + axpos(1);
    pos(2) = (pos(2) - axlim(3)) / axheight * axpos(4) + axpos(2);
    pos(3) = pos(3) * axpos(3) / axwidth;
    pos(4) = pos(4) * axpos(4 )/ axheight;
    varargout{1} = pos;
end
set(hAx,'Units',axun)
