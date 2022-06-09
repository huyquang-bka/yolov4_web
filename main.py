from PIL import Image
import streamlit as st
import cv2

logo = Image.open("pikachu-logo-619ACB690E-seeklogo.com.png")
st.set_page_config(layout="wide", page_title="TEST BY HUY QUANG", page_icon=logo)
st.title("TEST BY HUY QUANG".upper())
st.sidebar.title("SIDE BAR")
st.sidebar.markdown("-" * 20)
imageLocation = st.empty()
cap = cv2.VideoCapture(r"C:\Users\Admin\Downloads\demo.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imageLocation.image(frame)
