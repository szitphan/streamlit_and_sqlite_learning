import streamlit as st
import pandas as pd
import numpy as np
import database as db

# Headings & Text
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a sub-header')
st.write('''This is a markdown.
Enjoy it!
''')


# Display a metric in big bold font
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

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


# myslider = st.slider('Celsius')
# st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)

df_db = pd.DataFrame(db.get_data('customer.db'))
st.write(df_db)

