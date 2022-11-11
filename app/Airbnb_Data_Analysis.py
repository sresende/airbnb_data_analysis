## To configure Streamlit 
## streamlit config show
import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
# Render the h1 block, contained in a frame of size 200x200.
#components.html("<html><body><h1>Hello, World</h1></body></html>", width=200, height=200)
st.title('               _ Data Analysis on Airbnb Listings _')
#st.subheader('Do you want you predict the price for your accomodation?')
from PIL import Image
image = Image.open('../images/Airbnb_Logo.png')
#image = Image.open('../images/airbnb2.gif')
#video_file = open('../images/airbnb2.gif', 'rb')
#video_bytes = video_file.read()

#st.video(video_bytes)

st.image(image, caption='Sunrise by the mountains')