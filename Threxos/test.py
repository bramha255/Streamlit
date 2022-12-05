import time

import numpy as np
import pandas as pd
import streamlit_toggle as tog
from google.cloud import firestore
import streamlit as st
import streamlit_option_menu
st.set_page_config(page_title='Threxos',
                   page_icon='🔥', layout='wide')
# the callback function for the button will add 1 to the
# slider value up to 10
st.header('Dev environment')


# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")
# with st.container():
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Temperature", "70 °F", "1.2 °F")
#     col2.metric("Wind", "100000 mph", "-8%")
#     col3.metric("Humidity", "86%", "4%")
# with st.container():
#     c1, c2 = st.columns(2)
#     with c1:
#         st.write('LED')
#     with c2:
#         st.select_slider(label='s', label_visibility='collapsed',
#                          options=(1, 2, 3), key='1')
# st.write('------')
# with st.container():
#     with c1:
#         st.write('#')
#         st.write('LED')
#     with c2:
#         st.select_slider(label='s', options=(1, 2, 3),
#                          label_visibility='collapsed', key='2')
# with st.container():
#     with c1:
#         st.write('#')
#         st.write('LED')
#     with c2:
#         st.select_slider(label='s', options=(1, 2, 3),
#                          label_visibility='collapsed', key='3')

# def plus_one():
#     if st.session_state["slider"] < 10:
#         st.session_state.slider += 1
#     else:
#         pass
#     return


# # when creating the button, assign the name of your callback
# # function to the on_click parameter
# add_one = st.button("Add one to the slider", on_click=plus_one, key="add_one")

# # create the slider
# slide_val = st.slider("Pick a number", 0, 10, key="slider")

# def disable_other_checkboxes(*other_checkboxes_keys):
#     for checkbox_key in other_checkboxes_keys:
#         st.session_state[checkbox_key] = False


# option_1 = st.checkbox(
#     "Option_1",
#     key="op1",
#     on_change=disable_other_checkboxes,
#     args=("op2", "op3", "op4"),
# )
# option_2 = st.checkbox(
#     "Option_2",
#     key="op2",
#     on_change=disable_other_checkboxes,
#     args=("op1", "op3", "op4"),
# )
# option_3 = st.checkbox(
#     "Option_3",
#     key="op3",
#     on_change=disable_other_checkboxes,
#     args=("op2", "op1", "op4"),
# )
# option_4 = st.checkbox(
#     "Option_4",
#     key="op4",
#     on_change=disable_other_checkboxes,
#     args=("op2", "op3", "op1"),
# )

# st.write(option_1, option_2, option_3, option_4)
