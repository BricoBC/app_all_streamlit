import streamlit as st
import numpy as np
import pandas as pd

st.title('Proyecto para explicar todos los comandos.')
st.markdown('- Display text') # see *

# --------------------- SIDEBAR ---------------------
st.sidebar.radio('Select one:', [3, 4])
# Or use "with" notation:
# with st.sidebar:
#   st.radio('Select one:', [1, 2])


# ------------------ COLUMNS ---------------
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")


# You can also use "with" notation:
# with col1:
#   st.radio('Select one:', [1, 2])


#----------- TABS --------
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
# tab1.write("this is tab 1")
# tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
  st.header('TAB 1: ')
  st.radio('Select one:', [1, 2])

with tab2:
  st.header('TAB 2: ')
  data = np.arange(15, dtype=np.int64).reshape(3, 5)
  st.line_chart(data)