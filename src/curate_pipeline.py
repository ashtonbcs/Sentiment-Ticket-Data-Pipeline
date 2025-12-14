from datetime import datetime
import pandas as pd
from .database import engine, curated_tickets
from .config import PIPELINE_VERSION
from .ingest import load_Csv_to_DF
from .nlp_labeling import (infer_topic, infer_sentiment, urgency, priority)
from sqlalchemy.dialects.sqlite import insert as sqlite_insert


def run_pipeline(filename: str):
    df = load_Csv_to_DF(filename)
    df["sentiment"] = df["message_text"].apply(infer_sentiment)
    df["topic"] = df["message_text"].apply(infer_topic)
    df["urgency"] = df.apply(lambda row: urgency(row["message_text"], row["sentiment"]),axis=1)
    df["priority"] = df["urgency"].apply(priority)
    df["ingestion_time"] = datetime.utcnow().replace(microsecond=0)
    df["pipeline_version"] = PIPELINE_VERSION

    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["created_at"] = df["created_at"].apply(
        lambda x: x.to_pydatetime() if not pd.isna(x) else None
    )

    df["ingestion_time"] = df["created_at"].apply(
        lambda x: x if isinstance(x, datetime) else x.to_pydatetime()
        if hasattr(x, "to_pydatetime") else x
    )

    records = df.to_dict(orient="records")

    stmt = sqlite_insert(curated_tickets).prefix_with("OR IGNORE")
    with engine.begin() as conn:
        conn.execute(stmt, records)

    print(f"Inserted {len(records)} new tickets. Any not inserted were duplicates.")