Countries API - Data Engineering Project:

I am building an ETL pipeline to ingest data from the REST Countries API. I will process the data and load it into a database for further analysis. I will use Docker for containerization, Airflow for pipeline orchestration and Postgres as my database.

I began by downloading Docker Desktop to use as neccesary along the way.

Next, I created a folder on my desktop: DE_Countries, for my VSCode files. 

I. EXTRACT DATA FROM THE API
I wrote a python script to make GET requests from the API and downloaded the data, the script handles exceptions and errors appropriately and logs all activites.
After running my script, a new file named country_data.json was created which contained the data from the REST countries API.

II. TRANSFORMED/CLEANED THE DATA
I now moved on to cleaning the data the information into a friendlier format to work with using a python script: cleaning.py. A cleaned.json file was created and I moved on to preparing my database to load it in using sqlshell/postgresql.

CREATE DATABASE countryinfo;

III. LOADED THE CLEANED DATA INTO POSTGRESQL DB
Next I built a python script to load the cleaned data: loader.py. After some debugging, the data was successfully loaded into the PostgreSQL Db using a python script.
