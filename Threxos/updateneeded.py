import numpy as np
import pandas as pd
import streamlit_toggle as tog
import sklearn


# import streamlit as st

# st.title("IOT Webapp")
# st.markdown('''
# Welcome to threxos app

# -----
# # Bedroom light switch
# ### Click on the toggle icon to switch on the light
# ''')


# LED = tog.st_toggle_switch(label="LED", key="Key1", default_value=True, label_after=True,
#                            inactive_color='#D3D3D3', active_color="#11567f", track_color="#29B5E8")
# Zero_watts = tog.st_toggle_switch(label="Zero watts", key="Key2", default_value=False, label_after=True,
#                                   inactive_color='#D3D3D3', active_color="#11567f", track_color="#29B5E8")
# fan = tog.st_toggle_switch(label="Fan", key="Key3", default_value=True, label_after=True,
#                            inactive_color='#D3D3D3', active_color="#11567f", track_color="#29B5E8")
# AC = tog.st_toggle_switch(label="AC", key="Key4", default_value=False, label_after=True,
#                           inactive_color='#D3D3D3', active_color="#11567f", track_color="#29B5E8")


# # if LED:
# #     print('LED ON')
# # else:
# #     print('OFF')
