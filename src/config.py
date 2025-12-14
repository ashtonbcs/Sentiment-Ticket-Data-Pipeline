import os


#Base directory = project root
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DIR = os.path.join(DATA_DIR, 'raw')


#SQLite database file in project root
DATABASE_URL = "sqlite:////opt/airflow/Data/tickets.db"

PIPELINE_VERSION = "v1"
