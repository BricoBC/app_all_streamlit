import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame((
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
))

st.area_chart(df)
st.bar_chart(df)
st.line_chart(df)
# st.map(data=[(19.432688, -99.133209), (20.677162, -97.127186), (19.024181, -98.210968)], zoom=4)

st.scatter_chart(df)

# st.altair_chart(chart)
# st.bokeh_chart(fig)
# st.graphviz_chart(fig)
# st.plotly_chart(fig)
# st.pydeck_chart(chart)
# st.pyplot(fig)
st.vega_lite_chart(df)