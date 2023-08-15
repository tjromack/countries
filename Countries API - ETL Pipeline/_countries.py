import requests
import json

def get_country_data():
    # Specify the url
    url = "https://restcountries.com/v3.1/all"

    # Send HTTP request
    response = requests.get(url)

    # Raise exception if status code is not 200
    response.raise_for_status()

    # Parse response
    data = response.json()

    return data

def write_to_file(data):
    # Open a file for writing
    with open('country_data.json', 'w') as f:
        # Use json.dump to write data to file
        json.dump(data, f)

def main():
    data = get_country_data()
    write_to_file(data)

if __name__ == '__main__':
    main()