VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   7932
   ClientLeft      =   48
   ClientTop       =   288
   ClientWidth     =   7572
   LinkTopic       =   "Form1"
   ScaleHeight     =   7932
   ScaleWidth      =   7572
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   492
      Left            =   5160
      TabIndex        =   0
      Top             =   120
      Width           =   2052
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Dim a(100, 100), w(100, 100), v(100, 100), Y(100, 100), s(100), b(100) As Double
Dim thta(100), X(100), r(100), d(100), c(100, 100), num, l(100), e(100, 100) As Double
Dim tt As String
Dim i, j, k, t, eer(100), ee, kk, yy
Dim mw(100), tb(100), tc(100), pc(100), zc(100), hv(100), chv(100), xubfwc1, xubfwc2, ctb(100)
Dim ttb, ttc, tpc, thv, tzc, czc(100), fxubfwc1, fxubfwc2, tmw
n = Val(InputBox("输入输入层神经元数目"))
p = Val(InputBox("输入中间层神经元数目"))
q = Val(InputBox("输入输出层神经元数目"))
num = 0
m = Val(InputBox("训练模式数量"))
'数据文件读入输入已知模式对的输入输出数据

Open "xuxi.dat " For Input As #1
For i = 1 To 60 '79为数据文件中数据条数目
Input #1, mw(i), tb(i), tc(i), pc(i), zc(i), hv(i)
Next i
Close #1
tmw = 0
ttb = 0
ttc = 0
tpc = 0
thv = 0
tzc = 0
For i = 1 To m
    tmw = tmw + mw(i) ^ 2
    ttb = ttb + tb(i) ^ 2
    ttc = ttc + tc(i) ^ 2
    tpc = tpc + pc(i) ^ 2
    thv = thv + hv(i) ^ 2
    tzc = tzc + zc(i) ^ 2
Next i
    tmw = Sqr(tmw)
    ttb = Sqr(ttb)
    ttc = Sqr(ttc)
    tpc = Sqr(tpc)
    thv = Sqr(thv)
    tzc = Sqr(tzc)
For i = 1 To m
           a(i, 1) = mw(i) / tmw
           a(i, 2) = tc(i) / ttc
           a(i, 3) = pc(i) / tpc
           Y(i, 1) = tb(i) / ttb
           Y(i, 2) = zc(i) / tzc
               
Next i


'生成初始连接权数及阀值
For j = 1 To p
    For i = 1 To n
        w(i, j) = 2 * Rnd() - 1
      'Print w(i, j)
    Next i
    thta(j) = 2 * Rnd() - 1
    'Print thta(j)
Next j

For t = 1 To q
    For j = 1 To p
        v(j, t) = 2 * Rnd()
        'Print v(j, t)
    Next j
  r(t) = 2 * Rnd(j) - 1
    'Print r(t)
Next t

   
100
   For kk = 1 To m
       k = kk
       eer(k) = 0
       '模式顺传播
       For j = 1 To p
            s(j) = 0
            For i = 1 To n
               s(j) = s(j) + w(i, j) * a(k, i)
            Next i
            s(j) = s(j) - thta(j)
            b(j) = fnf(s(j))
                       
        Next j
         For t = 1 To q
            l(t) = 0
            For j = 1 To p
               l(t) = l(t) + v(j, t) * b(j)
            Next j
           l(t) = l(t) - r(t)
            'Print l(t)
            c(k, t) = fnf(l(t))
            
            '误差逆传播
            
            d(t) = (Y(k, t) - c(k, t)) * c(k, t) * (1 - c(k, t))
                                      
        Next t
               
        For j = 1 To p
            e(k, j) = 0
            For t = 1 To q
                e(k, j) = e(k, j) + d(t) * v(j, t)
            Next t
            e(k, j) = e(k, j) * b(j) * (1 - b(j))
        Next j
        '调整连接权及罚值
        For t = 1 To q
            For j = 1 To p
                 v(j, t) = v(j, t) + 0.5 * d(t) * b(j)
            Next j
            r(t) = r(t) - 0.5 * d(t)
        'Print "r(t)="; r(t)
          'tt = InputBox("")
        Next t
        For j = 1 To p
            For i = 1 To n
                 w(i, j) = w(i, j) + 0.5 * e(k, j) * a(k, i)
            Next i
            thta(j) = thta(j) - 0.5 * e(k, j)
        Next j
 num = num + 1
   If num / 300000 = Int(num / 300000 + 0.5) Then
       Print "num="; num, "ee="; ee
   Else
   End If
Next kk
If num >= 25000000 Then GoTo 200
'计算全局误差
ee = 0
For k = 1 To m
    eer(k) = 0
    For t = 1 To q
      eer(k) = eer(k) + (Y(k, t) - c(k, t)) ^ 2
    Next t
    ee = ee + eer(k)
Next k

'全局误差判断
If ee < 0.0001 Then
'网络收敛，打印权值及阀值并进入回响
 GoTo 200

Else
End If
'网络尚未收敛，继续计算
GoTo 100
'打印权值及阀值

200 For j = 1 To p
         For i = 1 To n
             Print "w("; i; j; ")="; w(i, j)
         Next i
        Print "thta("; j; ")="; thta(j)
        
 Next j
 For t = 1 To q
         For j = 1 To p
             Print "v("; j; t; ")="; v(j, t)
        Next j
        Print "r("; t; ")="; r(t)
 Next
 Print "全局误差="; ee; "总训练次数="; num
 '//文件记录数据
Open "g:权值及阀值9.dat" For Output As 1
For j = 1 To p
         For i = 1 To n
         Write #1, "w("; i; j; ")="; w(i, j)
         Next i
       Write #1, "thta("; j; ")="; thta(j)
Next j
For t = 1 To q
         For j = 1 To p
            Write #1, "v("; j; t; ")="; v(j, t)
        Next j
       Write #1, "r("; t; ")="; r(t)
 Next t
Write #1, "全局误差="; ee; "总训练次数="; num
GoTo 400
Print "是否需要单个网络回响，是输入y，否输入no”     "
       tt = InputBox("")
       If tt = "y" Then
          GoTo 300
       Else
         GoTo 400
       End If

300 '单个网络回响

   For i = 1 To n
        X(i) = Val(InputBox("输入第" & i & "输入变量"))
    Next i
For j = 1 To p
            s(j) = 0
            For i = 1 To n
               s(j) = s(j) + w(i, j) * X(i)
            Next i
            s(j) = s(j) - thta(j)
            b(j) = fnf(s(j))
Next j
For t = 1 To q
            l(t) = 0
            For j = 1 To p
               l(t) = l(t) + v(j, t) * b(j)
            Next j
           l(t) = l(t) - r(t)
            yy = fnf(l(t))
            Print "yy="; yy
Next t
       Print "是否继续需要网络回响，是输入y，否输入no”     "
       tt = InputBox("")
       If tt = "y" Then GoTo 300

400  '训练集网络回响
xubfwc1 = 0
xubfwc2 = 0
For k = 1 To m
    For j = 1 To p
            s(j) = 0
            For i = 1 To n
               s(j) = s(j) + w(i, j) * a(k, i)
            Next i
            s(j) = s(j) - thta(j)
            b(j) = fnf(s(j))
    Next j
    For t = 1 To q
            l(t) = 0
            For j = 1 To p
               l(t) = l(t) + v(j, t) * b(j)
            Next j
           l(t) = l(t) - r(t)
    c(k, t) = fnf(l(t))
    Next t
    ctb(k) = c(k, 1) * ttb
   czc(k) = c(k, 2) * tzc
    xubfwc1 = xubfwc1 + Abs((ctb(k) - tb(k)) / tb(k))
     xubfwc2 = xubfwc2 + Abs((czc(k) - zc(k)) / zc(k))
 Next k
 xubfwc1 = 100 * xubfwc1 / m
 xubfwc2 = 100 * xubfwc2 / m
 Print "训练集相对百分误差="; xubfwc1, xubfwc2
Write #1, "训练集相对百分误差="; xubfwc1, xubfwc2
500      '非训练集网络回响
fxubfwc1 = 0
fxubfwc2 = 0
For k = m + 1 To 60
           a(k, 1) = mw(k) / tmw
           a(k, 2) = tc(k) / ttc
           a(k, 3) = pc(k) / tpc
    
    
    For j = 1 To p
            s(j) = 0
            For i = 1 To n
               s(j) = s(j) + w(i, j) * a(k, i)
            Next i
            s(j) = s(j) - thta(j)
            b(j) = fnf(s(j))
    Next j
    For t = 1 To q
            l(t) = 0
            For j = 1 To p
               l(t) = l(t) + v(j, t) * b(j)
            Next j
           l(t) = l(t) - r(t)
    c(k, t) = fnf(l(t))
    Next t
   ctb(k) = c(k, 1) * ttb
   czc(k) = c(k, 2) * tzc
    fxubfwc1 = fxubfwc1 + Abs((ctb(k) - tb(k)) / tb(k))
    fxubfwc2 = fxubfwc2 + Abs((czc(k) - zc(k)) / zc(k))
 Next k

 fxubfwc1 = 100 * fxubfwc1 / (60 - m)
  fxubfwc2 = 100 * fxubfwc2 / (60 - m)
 Print "非训练集相对百分误差="; fxubfwc1, fxubfwc2
Write #1, "非训练集相对百分误差="; fxubfwc1, fxubfwc2; "m="; m
Close #1
 End Sub

Public Function fnf(X)
 fnf = 1 / (1 + Exp(-X))
End Function

