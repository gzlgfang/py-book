import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# uploaded_files = st.file_uploader("Choose a excel file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      stf="g:/"+uploaded_file.name
#      DF = pd.read_csv(stf) 
#      # bytes_data = uploaded_file.read()
#      # st.write("filename:", uploaded_file.name)
#      # st.write(bytes_data)
     
     
#      #DF = pd.read_excel(stf, "Sheet1", na_filter=False, index_col=0)  # 共有31个城市坐标
#      # city_x = np.array(DF["x"])  # 数据分配
#      # city_y = np.array(DF["y"])
#      # st.write(city_x) 
#      st.write(DF)
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for uploaded_file in uploaded_files:
#      bytes_data = uploaded_file.read()
#      st.write("filename:", uploaded_file.name)
#      st.write(bytes_data)     
global n
n=0
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     # bytes_data = uploaded_file.getvalue()
     # st.write(bytes_data)

     # To convert to a string based IO:
     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     # st.write(stringio)

     # To read file as string:
     # string_data = stringio.read()
     # st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
     array_d=np.array(dataframe)
     arr=np.array([[3,4,5],[7,8,9],[12,14,17]])
     ar_sum=sum(sum(array_d))
     st.write("ar-sum=",ar_sum)
     ss=0
     for i in range(10):
         ss=ss+array_d[i,0]
     st.write(ss)
     st.write(array_d)
     st.write(arr)
     st.markdown(arr)
     st.write(array_d[:,1])
     st.write(array_d[3,1])
     st.write(array_d[5,1])
     st.write(array_d[3,0])
     st.write(array_d[5,0])

     list1=list(array_d[:,1])
     st.write(list1)
     st.write(dataframe.values[(3,1)])
     st.write(dataframe.values[(5,1)])
     x=dataframe.values[(1,1)]+dataframe.values[(2,1)]+dataframe.values[(3,1)]
     st.write(x)
     st.header("有关一字开头的成语学习")
     st.text("本软件由方利国开发，发现错误之处请联系lgfang@scut.edu.cn,不胜感谢")
     st.subheader("第1题")
     str_test=["下面有关一字的四个词组，哪个不是成语:",
          '一成不变', '一个不剩', '一夫当关','一蹴而就']

     #select=st.radio("下面有关一字的四个词组，哪个不是成语:",
          #('一成不变', '一个不剩', '一夫当关','一蹴而就'),horizontal=True)#前面题目，后面4个选项
     select=st.radio(str_test[0],
          (str_test[1], str_test[2], str_test[3],str_test[4]),horizontal=True)#前面题目，后面4个选项

     if select == '一个不剩':  #这里填正确答案
          n=n+1

     st.subheader("第2题")
     select=st.radio("关于成语《一窍不通》解释正确的是:",
          ('只有一窍不通', '有一半不通', '有九窍不通','没有一窍是通的'),horizontal=True)
     if select == '没有一窍是通的':
          n=n+1

     st.subheader("第3题")
     select=st.radio("成语《一望无垠》中的<垠>的发音正确的是:",
          ('yin第四声', 'yin第二声', 'gen第四声','gen第二声'),horizontal=True)
     if select == 'yin第二声':
          n=n+1

     st.subheader("第4题")
     select=st.radio("成语《一丝不苟》中的<苟>的含义正确的是:",
          ('认真', '小心', '谨慎','马虎'),horizontal=True)
     if select == '马虎':
          n=n+1


     st.subheader("第5题")
     select=st.radio("下面不是成语《一诺千金》近义词的是:",
          ('一言为定', '一言九鼎', '季布一诺','轻诺寡信'),horizontal=True)
     if select == '轻诺寡信':
          n=n+1

     st.subheader("第6题")
     select=st.radio("成语《一蹴而就》近义词是:",
          ('一事无成', '一蹴不振', '一举成功','欲速不达'),horizontal=True)
     if select == '一举成功':
          n=n+1

     st.subheader("第7题")
     select=st.radio("下面四字词是正确成语的是:",
          ('一张一池', '一张一弛', '一张一也','一长一弛'),horizontal=True)
     if select == '一张一弛':
          n=n+1

     st.subheader("第8题")
     select=st.radio("下面不是成语《一叶知秋》近义词的是:",
          ('秋风落叶', '一叶报秋', '见微知著','尝鼎一脔'),horizontal=True)
     if select == '秋风落叶':
          n=n+1

     st.subheader("第9题")
     select=st.radio("成语《一暴十寒》中的<暴>的含义正确的是:",
          ('爆炸', '曝晒', '爆裂','火爆'),horizontal=True)
     if select == '曝晒':
          n=n+1


     st.subheader("第10题")
     select=st.radio("比喻彼此一样，没有什么差别并用作贬义的成语是:",
          ('一心一意', '一团和气', '一波三折','一丘之貉'),horizontal=True)
     if select == '一丘之貉':
          n=n+1


     if n>8:
     #st.write("恭喜您答对",n,"题,是个一字成语大行家")
          str_n=str(n)
          sstr="恭喜您答对" + str_n + "题,是个一字成语大行家"
          st.subheader(sstr)
     elif n>=6:
     #st.write("恭喜您答对",n,"题,本次成绩不错，还有提升空间")  
          str_n=str(n)
          sstr="恭喜您答对" + str_n + "题,本次成绩不错，还有提升空间"
          st.subheader(sstr)

     elif n<=5:
          #st.write("本次答对",n,"题,成绩不理想，请多多学习") 
          str_n=str(n)
          sstr="本次只答对" + str_n + "题,成绩不理想，请多多学习"
          st.subheader(sstr)
