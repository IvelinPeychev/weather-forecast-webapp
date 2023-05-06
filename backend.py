import requests

API_KEY = '5ca8870b01b52893554e49bf96d0d2c2'


def get_data(place, forecasts_day=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecasts_day
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Tokyo', 3))