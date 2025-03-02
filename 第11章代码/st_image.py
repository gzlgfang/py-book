import streamlit as st
from PIL import Image

# st.image(image, caption='Sunrise by the mountains')

st.write("三列图片布置")
col1, col2, col3 = st.columns(3)

with col1:

    image1 = Image.open("g:/建筑.jpg")
    st.header("励悟楼")
    st.image(image1)

    with col2:
        # image2 = Image.open("g:/樱花.jpg")
        # image2 = Image.open("樱花.jpg")
        image2 = Image.open("g:/st-app/pic/樱花.jpg")
        # image2 = Image.open("g:/st-app/pic/1009.jpg")
        # image2 = Image.open("./pic/樱花.jpg")
        st.header("樱花")
        st.image(image2)

with col3:
    image3 = Image.open("g:/异木棉.jpg")
    st.header("异木棉")
    st.image(image3)

# streamlit run g:/st-app/st_image.py
