import json

def read_data_from_file():
    with open('country_data.json', 'r') as f:
        data = json.load(f)
    return data

def clean_data(data):
    cleaned_data = []
    for country in data:
        # Extracting necessary fields and handling missing data
        name = country['name']['common']
        capital = country.get('capital', 'Unknown')
        area = country.get('area', 0) or 0
        population = country.get('population', 0) or 0
        region = country.get('region', 'Unknown')
        subregion = country.get('subregion', 'Unknown')
        
        # Extracting languages and currencies, which will be stored in different tables
        languages = list(country.get('languages', {}).values())
        currencies = list(country.get('currencies', {}).values())
        
        cleaned_country = {
            'name': name,
            'capital': capital,
            'area': area,
            'population': population,
            'region': region,
            'subregion': subregion,
            'languages': languages,
            'currencies': currencies,
        }

        cleaned_data.append(cleaned_country)

    return cleaned_data

def write_cleaned_data_to_file(data):
    with open('cleaned_country_data.json', 'w') as f:
        json.dump(data, f)

def main():
    raw_data = read_data_from_file()
    cleaned_data = clean_data(raw_data)
    write_cleaned_data_to_file(cleaned_data)

if __name__ == '__main__':
    main()