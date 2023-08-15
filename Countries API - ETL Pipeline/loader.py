import psycopg2
import json

def connect_to_db():
    conn = psycopg2.connect(
        dbname="countryinfo",
        user="postgres",
        password="trevorjames",
        host="localhost",
        port="5433"
    )
    return conn

def load_data():
    with open('cleaned_country_data.json') as f:
        data = json.load(f)
    return data

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            capital VARCHAR(100),
            area REAL,
            population INTEGER,
            region VARCHAR(100),
            subregion VARCHAR(100)
        );
        
        CREATE TABLE IF NOT EXISTS languages (
            id SERIAL PRIMARY KEY,
            country_id INTEGER,
            language VARCHAR(100),
            FOREIGN KEY(country_id) REFERENCES countries(id)
        );
        
        CREATE TABLE IF NOT EXISTS currencies (
            id SERIAL PRIMARY KEY,
            country_id INTEGER,
            name VARCHAR(100),
            symbol VARCHAR(10),
            FOREIGN KEY(country_id) REFERENCES countries(id)
        );
    ''')
    conn.commit()

def insert_country(cursor, country):
    cursor.execute('''
        INSERT INTO countries (name, capital, area, population, region, subregion) VALUES (%s, %s, %s, %s, %s, %s) 
        ON CONFLICT (name) DO NOTHING RETURNING id
    ''', (country['name'], ', '.join(country['capital']), country['area'], country['population'], country['region'], country['subregion']))
    
    result = cursor.fetchone()
    
    if result is None:
        cursor.execute("SELECT id FROM countries WHERE name = %s", (country['name'],))
        result = cursor.fetchone()

    return result[0]

def insert_language(cursor, country_id, language):
    cursor.execute('''
        INSERT INTO languages (country_id, language) VALUES (%s, %s)
        ON CONFLICT (language) DO NOTHING
    ''', (country_id, language))

def insert_currency(cursor, country_id, currency):
    cursor.execute('''
        INSERT INTO currencies (country_id, name, symbol) VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    ''', (country_id, currency.get('name', 'Unknown'), currency.get('symbol', 'Unknown')))

def load_to_db(conn, data):
    cursor = conn.cursor()
    for country in data:
        country_id = insert_country(cursor, country)
        for language in country['languages']:
            insert_language(cursor, country_id, language)
        for currency in country['currencies']:
            insert_currency(cursor, country_id, currency)
    conn.commit()

def main():
    conn = connect_to_db()
    data = load_data()
    create_tables(conn)
    load_to_db(conn, data)
    conn.close()

if __name__ == '__main__':
    main()