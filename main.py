import streamlit as st
import plotly.express as px
from backend import get_data

# Create a page with title
st.title('Weather Forecast for the Next Days')

# Create an input box
place = st.text_input('Place: ')

# Create a slider
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forcasted days')

# Create a dropdown
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))

# Create a sub header
st.subheader(f'{option} for the next {days} days in {place}')

d, t = get_data(place, days, option)


# Create a graph
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperatures (C)'})
st.plotly_chart(figure)
