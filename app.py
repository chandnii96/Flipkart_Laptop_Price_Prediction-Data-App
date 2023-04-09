import streamlit as st
from PIL import Image
from matplotlib import image
import os
import pickle

#Title of the home page
st.header(":blue[Laptop Price Prediction App]")


#subheader
st.write('By: :blue[Chandni Kumari]')

#Adding image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "laptop.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)


st.markdown(":lightblue[Connect with me ]")



st.write(":blue[LinkedIn]:(https://www.linkedin.com/in/chandniikumari/)")

st.write(":green[GitHub]:(https://github.com/chandnii96)")

st.write(":red[Instagram]:(https://www.instagram.com/chand__nii/ )")

btn_click = st.button("Click me")

if btn_click == True:
    st.subheader(" Hello BUDDY:grinning:")
    st.header("Learn-Explore-Develop")
    



