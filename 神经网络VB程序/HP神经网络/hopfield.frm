VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   8220
   ClientLeft      =   48
   ClientTop       =   288
   ClientWidth     =   9192
   LinkTopic       =   "Form1"
   ScaleHeight     =   8220
   ScaleWidth      =   9192
   StartUpPosition =   3  '����ȱʡ
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   1092
      Left            =   5160
      TabIndex        =   0
      Top             =   5880
      Width           =   2772
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
Dim w(200, 200), H(200), thta(200) As Double
Dim UN(200), UN1(200), un2(200), Num, EN, EN1 As Double
Dim tt As String
Dim i, j, k
n = Val(InputBox("������Ԫ��Ŀ"))






'���ɳ�ʼ����Ȩ������ֵ
For i = 1 To n
    For j = i To n
        If j = i Then
            w(i, j) = 0
        Else
            w(i, j) = 3 * Rnd() - 1
            w(j, i) = w(i, j)
        End If
    Next j
    thta(i) = 5 * Rnd() - 1
Next i
'��ӡȨֵ����ֵ
For j = 1 To n
         For i = 1 To n
             Print "w("; i; j; ")="; Int(w(i, j) * 10000 + 0.5) / 10000;
        Next i
        'Print
 Next j
For j = 1 To n
Print "thta("; j; ")="; Int(10000 * thta(j) + 0.5) / 10000;
Next j
Print
400
'�����������Ԫ��ǰ���ֵ

For i = 1 To n
    UN(i) = Int(Rnd(n) + 0.5)
    Print UN(i);
Next i
Print




'��ʼ��������
EN = 0
 Num = 0

100   i = Int(n * Rnd() + 0.5)
   H(i) = 0
   For j = 1 To n
       If j <> i Then
          H(i) = w(i, j) * UN(j)
       Else
       End If
   Next j
   H(i) = H(i) - thta(i)
   If H(i) > 0 Then
      UN1(i) = 1
   Else
   UN1(i) = 0
   End If
   
   For j = 1 To n
        If j <> i Then
          UN1(j) = UN(j)
       Else
       End If
   Next j
   '��������
   EN1 = 0
   For i = 1 To n
       For j = 1 To n
       If j <> i Then
          EN1 = EN1 - 0.5 * w(i, j) * UN1(i) * UN1(j)
       Else
       End If
       Next j
  Next i
  For i = 1 To n
      EN1 = EN1 + thta(i) * UN1(i)
  Next i
       
 Num = Num + 1
'�ж�����
For i = 1 To n
       H(i) = 0
   For j = 1 To n
       If j <> i Then
          H(i) = w(i, j) * UN1(j)
       Else
       End If
   Next j
   H(i) = H(i) - thta(i)
   If H(i) >= 0 Then
      un2(i) = 1
   Else
   un2(i) = 0
   End If
 Next i
 For i = 1 To n
    If UN1(i) <> un2(i) Then
          GoTo 300
        Else
        End If
Next i
GoTo 200
'������δ��������������
300
For i = 1 To n
    UN(i) = UN1(i)
Next i
GoTo 100

 
200

Print "ȫ������="; EN1; "��ѵ������="; Num
Print "��ӡ�������״̬��Ԫ�����"
For i = 1 To n
   Print UN1(i);
Next i
Print
tt = InputBox("�Ƿ�ʼ��ģʽ���������롰y����n��")
If tt = "y" Then
GoTo 400
Else
End If
 

End Sub


