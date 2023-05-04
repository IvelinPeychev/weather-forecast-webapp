import streamlit as st
import pandas as pd
import plotly.express as px

st.title('In Search for Happiness')

# Set dropdowns
x_axis = st.selectbox('Select the data for the X-axis', ('GDP', 'Happiness', 'Generosity'))
y_axis = st.selectbox('Select the data for the Y-axis ', ('GDP', 'Happiness', 'Generosity'))

# Set sun header
st.subheader(f'{x_axis} and {y_axis}')


def get_data(x, y):
    df = pd.read_csv('happy.csv')
    gdp = df['gdp'].squeeze()
    happiness = df['happiness'].squeeze()
    generosity = df['generosity'].squeeze()
    match x:
        case 'GDP':
            x = gdp
        case 'Happiness':
            x = happiness
        case 'Generosity':
            x = generosity

    match y:
        case 'GDP':
            y = gdp
        case 'Happiness':
            y = happiness
        case 'Generosity':
            y = generosity

    return x, y


# Assign the data values to the x and y-axis
x, y = get_data(x_axis, y_axis)

# Create the figure
figure = px.scatter(x=x, y=y, labels={'x': f'{x_axis}', 'y': f'{y_axis}'})
st.plotly_chart(figure)
