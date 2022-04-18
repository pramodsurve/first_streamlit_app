import streamlit as st

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')

st.text('🥣 Omega 2 & Blueberry Oatmeal')

st.text('🥗 Kale, Spinach & Rocket Smoothie')

st. text('🐔 Hard-Boiled Free-Range Egg')

st.text('🥑 🍞 Avocado Toast')

st.header('🍌 🍓 Build Your Own Fruit Smoothie 🥝 🍇')


import pandas as pd

file_loc = 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

my_fruit_list = pd.read_csv(file_loc)

st.dataframe(my_fruit_list)

