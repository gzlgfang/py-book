VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   2340
   ClientLeft      =   108
   ClientTop       =   432
   ClientWidth     =   3624
   LinkTopic       =   "Form1"
   ScaleHeight     =   2340
   ScaleWidth      =   3624
   StartUpPosition =   3  '����ȱʡ
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   1332
      Left            =   12960
      TabIndex        =   0
      Top             =   1200
      Width           =   2772
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
Dim mw(100), tb(100), tc(100), pc(100), zc(100), hv(100), chv(100), xubfwc
Dim ttb, ttc, tpc, thv, fxubfwc, tmw
n = Val(InputBox("�����������Ԫ��Ŀ"))
p = Val(InputBox("�����м����Ԫ��Ŀ"))
q = Val(InputBox("�����������Ԫ��Ŀ"))
num = 0
m = Val(InputBox("ѵ��ģʽ����"))
'�����ļ�����������֪ģʽ�Ե������������
Open "xuxi.dat " For Input As #1
For i = 1 To 79  '79Ϊ�����ļ�����������Ŀ
Input #1, mw(i), tb(i), tc(i), pc(i), zc(i), hv(i)
Next i
Close #1
'���ݶ�����ɣ���ʼ���й�һ������
tmw = 0
ttb = 0
ttc = 0
tpc = 0
thv = 0
For i = 1 To m
    tmw = tmw + mw(i) ^ 2
    ttb = ttb + tb(i) ^ 2
    ttc = ttc + tc(i) ^ 2
    tpc = tpc + pc(i) ^ 2
    thv = thv + hv(i) ^ 2
Next i
    tmw = Sqr(tmw)
    ttb = Sqr(ttb)
    ttc = Sqr(ttc)
    tpc = Sqr(tpc)
    thv = Sqr(thv)

'ѡ�񱾴�ѵ����������ݶԽ��о����һ������
For i = 1 To m
           a(i, 1) = tb(i) / ttb
           a(i, 2) = tc(i) / ttc
           a(i, 3) = pc(i) / tpc
           Y(i, 1) = hv(i) / thv
Next i

'���ɳ�ʼ����Ȩ������ֵ����ǰ���ͨ�ó�����ͬ
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
'��ʼѵ��ѧϰ
100
   For k = 1 To m
       eer(k) = 0
       'ģʽ˳����
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
            
            '����洫��
            d(t) = (Y(k, t) - c(k, t)) * c(k, t) * (1 - c(k, t))
         Next t
               
        For j = 1 To p
            e(k, j) = 0
            For t = 1 To q
                e(k, j) = e(k, j) + d(t) * v(j, t)
            Next t
            e(k, j) = e(k, j) * b(j) * (1 - b(j))
        Next j
        '��������Ȩ����ֵ
        For t = 1 To q
            For j = 1 To p
                 v(j, t) = v(j, t) + 0.5 * d(t) * b(j)
            Next j
            r(t) = r(t) - 0.5 * d(t)
         Next t
        For j = 1 To p
            For i = 1 To n
                 w(i, j) = w(i, j) + 0.5 * e(k, j) * a(k, i)
            Next i
            thta(j) = thta(j) - 0.5 * e(k, j) ' //ǰ���"0.5"��ѧϰϵ��������(0,1)֮�����
        Next j
 num = num + 1                      ' //ͳ��ѵ������
   If num / 2000000 = Int(num / 2000000 + 0.5) Then  '//ѵ�������ﵽ200���ʱ��ӡ
       Print "num="; num, "ee="; ee                '//��ǰȫ�����
   Else
   End If
Next k
If num >= 60000000 Then GoTo 200   ' //ѵ����������Ԥ������������ѧϰ

'����ȫ�����
ee = 0
For k = 1 To m
    eer(k) = 0
    For t = 1 To q
      eer(k) = eer(k) + (Y(k, t) - c(k, t)) ^ 2
    Next t
    ee = ee + eer(k)
Next k

'ȫ������ж�
If ee < 0.0005 Then
'������������ӡȨֵ����ֵ���������
 GoTo 200
Else
End If
'������δ��������������
GoTo 100
'��ӡȨֵ����ֵ
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
 Print "ȫ�����="; ee; "��ѵ������="; num
 '//�ļ���¼����
Open "g:Ȩֵ����ֵ4.dat" For Output As #1
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
Write #1, "ȫ�����="; ee; "��ѵ������="; num
250
Print "�Ƿ���Ҫ����������죬������y��������no "
       tt = InputBox("")
       If tt = "y" Then
          GoTo 300
       Else
         GoTo 400
       End If
300 '�����������

   For i = 1 To n
        X(i) = Val(InputBox("�����" & i & "�������"))
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
       Print "�Ƿ������Ҫ������죬������y��������no "
       tt = InputBox("")
       If tt = "y" Then GoTo 250

400  'ѵ�����������
xubfwc = 0
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
    chv(k) = c(k, t) * thv      '//����������Ǳ���������ֵ��ע�ⷴ��һ������
    Next t
    xubfwc = xubfwc + Abs((chv(k) - hv(k)) / hv(k))   '//���ƫ���ۼӼ���
 Next k
 xubfwc = 100 * xubfwc / m
 Print "ѵ������԰ٷ����="; xubfwc
Write #1, "ѵ������԰ٷ����="; xubfwc
500      '��ѵ�����������
fxubfwc = 0
For k = m + 1 To 79    '//"79"Ϊ�����ļ��е��������������ɸ��ݾ�������������޸�
           a(k, 1) = tb(k) / ttb
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
    chv(k) = c(k, t) * thv
    Next t
    fxubfwc = fxubfwc + Abs((chv(k) - hv(k)) / hv(k))
 Next k
 fxubfwc = 100 * fxubfwc / (79 - m)
 Print "��ѵ������԰ٷ����="; fxubfwc
Write #1, "��ѵ������԰ٷ����="; fxubfwc
Close #1
 End Sub
Public Function fnf(X)
 fnf = 1 / (1 + Exp(-X))
End Function

'

