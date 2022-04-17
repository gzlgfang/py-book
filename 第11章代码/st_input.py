#st_input.py
import numpy as np
import streamlit as st
st.sidebar.title("输入输出演示")
n = st.number_input("请输入一个需要处理的数", value=10, step=1, max_value=100,min_value=0,format="%d")
# st.button("三角函数")
# st.button("自然对数")
# st.button("求平方和")
# st.button("求立方和")
if st.sidebar.button("三角函数"):
   st.write(np.sin(n))
elif  st.sidebar.button("自然对数"):
   st.write(np.log(n))
elif  st.sidebar.button("求平方和",key=3):
   st.write(sum(i**2 for i in range(1,n+1)))
elif  st.sidebar.button("求立方和",key=4):
   st.write(sum(i**3 for i in range(1,n+1)))