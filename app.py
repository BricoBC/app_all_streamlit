import streamlit as st

st.title('Proyecto para explicar todos los comandos.')
st.markdown('- Display text') # see *


st.sidebar.radio('Select one:', [3, 4])
# Or use "with" notation:
# with st.sidebar:
#   st.radio('Select one:', [1, 2])