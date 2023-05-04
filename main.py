import streamlit as st
import plotly.express as px

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


def get_data(days):
    dates = ['2023-05-04', '2023-05-03', '2023-05-02']
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

# Create a graph
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperatures (C)'})
st.plotly_chart(figure)
