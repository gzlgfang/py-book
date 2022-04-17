import streamlit as st
st.sidebar.write('CAD慕课导航栏')
add_selectbox = st.sidebar.radio("目录",("第1章", "第2章", "第3章","第4章"))
if add_selectbox=="目录":
      st.write("第1章、第2章、第3章、第4章") 
elif add_selectbox=="第1章": 
      video_file = open("g:/chapter1.mp4", "rb")
      video_bytes = video_file.read()
      st.video(video_bytes)

elif add_selectbox == "第2章":
      video_file = open("g:/chapter2.mp4", "rb")
      video_bytes = video_file.read()
      st.video(video_bytes)
      cm

elif add_selectbox == "第3章":
      video_file = open("g:/chapter3.mp4", "rb")
      video_bytes = video_file.read()
      st.video(video_bytes)

elif add_selectbox == "第4章":
        st.write("尚未完成，敬请期待")   
        








