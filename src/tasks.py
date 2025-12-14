from src.ingest import load_Csv_to_DF
from src.curate_pipeline import run_pipeline
from src.database import engine, curated_tickets

def task_ingest(filepath: str):
    return load_Csv_to_DF(filepath)
def task_curate(filepath: str):
    from src.curate_pipeline import run_pipeline
    run_pipeline(filepath)