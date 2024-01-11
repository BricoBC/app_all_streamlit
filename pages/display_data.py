import streamlit as st
import pandas as pd
import numpy as np

my_dataframe = pd.DataFrame((
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
))

st.dataframe(my_dataframe)
st.table(my_dataframe)
st.table(my_dataframe.iloc[0:2])
st.json({'foo':'bar','fu':'ba'})
st.metric('My metric', 42, 2)