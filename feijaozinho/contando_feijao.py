import streamlit as st
import cv2
import numpy as np

img_file_buffer = st.camera_input("Diga X")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (11, 11), 0)
    canny = cv2.Canny(blur, 30, 150,3)
    dilated = cv2.dilate(canny, (1, 1), iterations=0)

    cnt, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    rgb2 = cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

    st.image(rgb2)
    st.write(f"São {len(cnt)} feijões!")
