from datetime import datetime
import sys
sys.path.insert(0, '/opt/airflow')
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.curate_pipeline import run_pipeline


def run_ticket_pipeline(**context):
    csv_path = context['dag_run'].conf.get('csv_path', '/opt/airflow/Data/raw/tickets_sample_airflow.csv')
    print(f"Processing CSV: {csv_path}")
    run_pipeline(csv_path)

with DAG(
    dag_id="nlp_ticket_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["nlp"],
    params={
        "csv_path": "/opt/airflow/data/raw/tickets_sample.csv"
    },
) as dag:
    run_task = PythonOperator(
        task_id="run_pipeline",
        python_callable=run_ticket_pipeline,
        provide_context=True,
    )