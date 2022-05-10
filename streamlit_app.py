import streamlit as st

import pandas as pd

import requests

import snowflake.connector

from urllib.error import URLError

st.title('My Mom\'s New Healthy Diner')

st.header('Breakfast Favorites')

st.text('🥣 Omega 2 & Blueberry Oatmeal')

st.text('🥗 Kale, Spinach & Rocket Smoothie')

st. text('🐔 Hard-Boiled Free-Range Egg')

st.text('🥑 🍞 Avocado Toast')

st.header('🍌 🍓 Build Your Own Fruit Smoothie 🥝 🍇')


file_loc = 'https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'

#import pandas

my_fruit_list = pd.read_csv(file_loc)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Add multi selector picker so thaty users can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
st.dataframe(fruits_to_show)


# Define a function to get data

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  # take the json version and normalize it
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  # Retun value
  return fruityvice_normalized
  
  
# New Section to Display Fruityvice api response
st.header('Fruityvice Fruit Advice!')

# If-Then construct
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    #Output the normalized version on the screen as a table
    st.dataframe(back_from_function)
      
except URLError as e:
  st.error()


#Snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
# Add a button to add fruit load list
if st.button("Get Fruit Load List"):
  # import snowflake.connector
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.header("The fruit load list contains:")
  st.dataframe(my_data_rows)


# Allow the end user to add a fruit to the list
# Define function ot add fruit
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return ('Thanks for adding', new_fruit)
  

add_my_fruit = st.text_input('What fruit would you like to add?')
if st.button("Add a fruit to the List"):
  # import snowflake.connector
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.write(back_from_function)

# Don't run anything past here until we troubleshoot
st.stop()

