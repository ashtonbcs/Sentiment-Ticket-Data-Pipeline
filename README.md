A CSV file containing support tickets is placed in the Data/raw directory
The Airflow DAG is triggered manually or scheduled

The pipeline loads and validates input data, applies NLP based labeling and inserts curated records into the SQLite database
Results are available immediately for querying or analytics

The pipeline is fully orchestrated with Apache Airflow and runs inside a Dockerized enviormnet which enables reproducible batch processing.
