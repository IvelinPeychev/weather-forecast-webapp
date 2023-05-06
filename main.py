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


if place:
    try:
        # Get the temperature or sky data
        filtered_data = get_data(place, days)

        if option == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperatures (C)'})
            st.plotly_chart(figure)

        elif option == 'Sky':
            sky_condition = [dict['weather'][0]['main'] for dict in filtered_data]
            images = {'Clear': 'images/clear.png',
                      'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png',
                      'Snow': 'images/snow.png'}
            image_paths = [images[condition] for condition in sky_condition]
            # Create a sky plot
            st.image(image_paths, width=115)
    except KeyError:
        st.write('This place does not exist')
