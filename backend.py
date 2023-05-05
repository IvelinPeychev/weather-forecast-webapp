import requests

API_KEY = '5ca8870b01b52893554e49bf96d0d2c2'

def get_data(place, forecasts_day=None, kind=None):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data



if __name__ == '__main__':
    print(get_data('Tokyo'))