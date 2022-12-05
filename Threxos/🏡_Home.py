import streamlit_toggle as tog

import streamlit as st
st.set_page_config(layout="wide")

# the callback function for the button will add 1 to the
# slider value up to 10
st.title("IOT Webapp - Prod environment")
st.markdown('''
Welcome to threxos app

-----''')


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
def hall():
    col1, col2 = st.columns(2)

    with col1:
        st.write('Device')
        st.write('Fan')
        st.write('LED')
        st.write('Tubelight')
        st.write('Chandelier💡')

    with col2:
        st.write('Status')
        hfan1 = st.radio(label='Fan', options=('1', '2', '3', '2', '3', '2', '3', '2', '3', '2', '3'), key='hfan1',
                         label_visibility='collapsed', horizontal=True)
        # hfan1 = st.select_slider(
        #     label='Fan', key='hfan1', options=('1', '2', '3'), label_visibility='collapsed')
        hled1 = st.radio(label='led', options=("On", "Off"), key='hled1',
                         label_visibility='collapsed', horizontal=True)
        htubelight1 = st.radio(label='tubelight', options=("On", "Off"), key='htubelight1',
                               label_visibility='collapsed', horizontal=True)
        hchanderlier1 = st.radio(label='chandelier', options=("On", "Off"), key='hchandelier1',
                                 label_visibility='collapsed', horizontal=True)


# st.write(
#     '<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


def bedroom():
    col11, col12 = st.columns(2)
    with col11:
        st.write('Device')
    with col11:
        st.write('LED')
    with col12:
        st.write('Status')
        st.radio('LED status', ("On", "Off"), key='r1',
                 label_visibility='collapsed', horizontal=True)

    # with col21:
    #     st.write("#") #to add empty line in webapp
    with col11:
        st.write('Fan')
    with col12:
        st.radio('Fan status', ("On", "Off"), key='r2',
                 horizontal=True, label_visibility='collapsed')
    with col11:
        st.write('AC')
    with col12:
        st.radio('AC status', ("On", "Off"), key='r3',
                 label_visibility='collapsed', horizontal=True)


def bathroom():
    col11, col12 = st.columns(2)
    with col11:
        st.write('Device')
    with col11:
        st.write('Heater')
    with col12:
        st.write('Status')
        st.radio('Status', ("on", 'off'), key='r1',
                 label_visibility='collapsed', horizontal=True)

    col21, col22 = st.columns(2)
    # with col21:
    #     st.write("#") #to add empty line in webapp
    with col21:
        st.write('Hair dryer')
    with col22:
        st.radio('Status', options=("on", 'off'), key='r2',
                 horizontal=True, label_visibility='collapsed')


room = st.sidebar.selectbox('Select room', options=[
                            'Hall', 'Bedroom', 'Bathroom'], key='room',
                            label_visibility='collapsed')

if st.session_state['room'] == 'Hall':
    hall()
elif st.session_state['room'] == 'Bedroom':
    bedroom()
elif st.session_state['room'] == 'Bathroom':
    bathroom()
