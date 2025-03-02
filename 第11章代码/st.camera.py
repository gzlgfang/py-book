import streamlit as st
import streamlit as st
from PIL import Image
import numpy as np
#import cv2
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)


if picture is not None:


    # To read image file buffer as a PIL Image:
    img1 = Image.open(picture)
    
    # To convert PIL Image to numpy array:
    img_array1 = np.array(img1)

    
    bytes_data = picture.getvalue()
   # img2 = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # To read image file buffer with OpenCV:
   # img_array2 = np.array(img2)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array1))
    #st.write(type(img_array2))
    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array1.shape)
    #st.write(img_array2.shape)
    st.write(img_array1)
    st.write("second numpy data")
    #st.write(img_array2)
