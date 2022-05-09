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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add multi selector picker so thaty users can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
st.dataframe(fruits_to_show)


# New Section to Display Fruityvice api response
st.header('Fruityvice Fruit Advice!')

# Get Fruit input
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

#Output the normalized version on the screen as a table
st.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)




