import streamlit as st
import pandas as pd
import numpy as np

# Headings & Text
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a sub-header')
st.write('''This is a markdown.
Enjoy it!
''')


# Dislay data in Tables
data = {
  'Series_1':[1, 3, 4, 5, 7],
  'Series 2':[10, 30, 40, 100, 250]
}
df = pd.DataFrame(data)
st.write(df)


# Dislay data in Charts
st.line_chart(df)
st.area_chart(df)

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": np.random.randn(60),
        "col3": ["A"] * 20 + ["B"] * 20 + ["C"] * 20,
    }
)

st.bar_chart(chart_data, x="col1", y="col2", color="col3")


myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)