import streamlit as st
from datetime import datetime
import time

# streamlit  run "g:/st-app/st_ca_time.py"
# 用于存储时间戳的变量
if "time1" not in st.session_state:
    st.session_state.time1 = None
if "time2" not in st.session_state:
    st.session_state.time2 = None

# 按钮
if st.button("点击我"):
    # 如果time1是空的，记录第一次点击的时间
    if st.session_state.time1 is None:
        st.session_state.time1 = time.time()
        # datetime.now()
        # st.write("记录第一次点击的时间: ", st.session_state.time1)
    # 否则记录第二次点击的时间，并计算时间间隔
    elif st.session_state.time2 is None:
        st.session_state.time2 = time.time()
        # datetime.now()
        interval = st.session_state.time2 - st.session_state.time1
        # st.write("记录第二次点击的时间: ", st.session_state.time2)
        h = interval // 3600  ##计算小时
        h_s = interval % 3600
        m = h_s // 60  ##计算分钟
        s = h_s % 60  ##计算秒
        st.write("两次点击的时间间隔为: ", h, "小时", m, "分钟", s, "秒")
        # 重置时间记录，准备下一次计时
        st.session_state.time1 = None
        st.session_state.time2 = None
