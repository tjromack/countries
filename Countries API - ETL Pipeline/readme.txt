Countries API - Basic ETL Pipeline demonstrating work 

I. EXTRACT DATA FROM THE API
I wrote a python script to make GET requests from the API and downloaded the data, the script handles exceptions and errors appropriately and logs all activites.
After running the script, a new file named country_data.json was created which contained the data from the REST countries API.

II. TRANSFORMED/CLEANED THE DATA
Writing and executing a python script: cleaning.py. This script produces: cleaned.json, a file of formatted data prepared for loading into your preferred database.

CREATE DATABASE countryinfo;

III. LOADED THE CLEANED DATA INTO POSTGRESQL DB
Writing and executing: loader.py. This script loads the data into PostgreSQL.
