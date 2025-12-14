import os
import pandas as pd
#from datetime import datetime
from .config import RAW_DIR

REQ_COLUMNS = ["ticket_id", "user_id", "created_at",
               "message_text", "channel", "agent_id"]
# Loading thr file and cleaning it. Includes striping extra space and accounting for missing data.
def load_Csv_to_DF(filename: str) -> pd.DataFrame:
    path = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(path)

    # Standardize the columns
    df.columns = [c.strip().lower() for c in df.columns]

    # Basic validation: check required columns exist
    missing = set(REQ_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Parse datetime
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")

    df["channel"] = df["channel"].fillna("unknown").replace("", "unknown")

    df["agent_id"] = df["agent_id"].replace("", None)

    df["message_text"] = df["message_text"].apply(
        lambda x: x if isinstance(x, str) and x.strip() != "" else None
    )

    return df