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
      Left            =   1920
      TabIndex        =   0
      Top             =   3240
      Width           =   2052
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Dim a(20, 20), w(20, 20), v(20, 20), y(20, 20), s(20), b(20) As Double
Dim thta(20), x(20), r(20), d(20), c(20, 20), num, l(20), e(20, 20) As Double
Dim tt As String
Dim i, j, k, t, eer(20), ee, kk, yy
n = Val(InputBox("输入输入层神经元数目"))
p = Val(InputBox("输入中间层神经元数目"))
q = Val(InputBox("输入输出层神经元数目"))
num = 0
m = Val(InputBox("训练模式数量"))
'输入已知模式对的输入输出数据

For i = 1 To m
    For j = 1 To n
        a(i, j) = Val(InputBox("输入第" & i & "模式" & "第" & j & "输入变量"))
    Next j
    For j = 1 To q
        y(i, j) = Val(InputBox("输入第" & i & "模式" & "第" & j & "输出变量"))
    Next j
        
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

   
100  ee = 0
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
            
            d(t) = (y(k, t) - c(k, t)) * c(k, t) * (1 - c(k, t))
                                      
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
Next kk
'计算全局误差
ee = 0
For k = 1 To m
    eer(k) = 0
    For t = 1 To q
      eer(k) = eer(k) + (y(k, t) - c(k, t)) ^ 2
    Next t
    ee = ee + eer(k)
Next k

'全局误差判断
If ee < 0.005 Then
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
300 '网络回响

    For i = 1 To n
        x(i) = Val(InputBox("输入第" & i & "输入变量"))
      
    Next i
For j = 1 To p
            s(j) = 0
            For i = 1 To n
               s(j) = s(j) + w(i, j) * x(i)
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


 End Sub

Public Function fnf(x)
 fnf = 1 / (1 + Exp(-x))
End Function
