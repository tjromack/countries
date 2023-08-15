Countries API - Data Engineering Project:

I am building an ETL pipeline to ingest data from the REST Countries API. I will processe the data and load it into a database for further analysis. I will use Docker for containerization, Airflow for pipeline orchestration and Postgres as my database.

I began by downloading Docker Desktop to use as neccesary along the way.

Next, I created a folder on my desktop: DE_Countries, for my VSCode files. 

I. EXTRACT DATA FROM THE API
I wrote a python script to make GET requests from the API and downloaded the data, the script handles exceptions and errors appropriately and logs all activites.
After running my script, a new file named country_data.json was created which contained the data from the REST countries API.

II. TRANSFORMED/CLEANED THE DATA
I now moved on to cleaning the data the information into a friendlier format to work with using a python script: cleaning.py. A cleaned.json file was created and I moved on to preparing my database to load it in using sqlshell/postgresql.

CREATE DATABASE countryinfo;

III. LOADED THE CLEANED DATA INTO POSTGRESQL DB
Next I built a python script to load the cleaned data: loader.py. After many back and forths debugging I successfully loaded using a python script, the data into the PostgreSQL Db.




5. Pipeline Orchestration with Apache Airflow:

An important part of data engineering is automating and scheduling data pipelines. For this, you will use Apache Airflow.

Set up a new Airflow DAG (Directed Acyclic Graph) for your pipeline.
Define tasks for data extraction, transformation, and loading, using the Python scripts you wrote earlier.
Specify dependencies between the tasks to ensure they run in the correct order.
Set a schedule for your pipeline, such as running it once a day.
6. Document and Test your Pipeline:

It's crucial to thoroughly document and test your work.

Write clear comments and README files explaining how your pipeline works, how to run it, and how to troubleshoot common issues.
Run tests to ensure your pipeline works as expected. This could involve checking that the correct data has been loaded into the database, or intentionally introducing errors to ensure your error handling and logging works correctly.
7. Showcase Your Project:

Finally, upload your project to a public repository on GitHub. Ensure the repository is well-organized and includes clear instructions on how to set up and run your pipeline. Include your tests and their results, and any challenges you faced and how you overcame them. Your goal is to demonstrate that you can build a robust, professional-grade data pipeline.

This project should give you a good grounding in the fundamentals of data engineering, and is a great way to showcase a range of skills that are important in this field.


