from datetime import datetime
from sqlalchemy import(
create_engine, MetaData, Table, Column,
String,Text, Integer, DateTime, Float
)
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
metadata = MetaData()

# Table which will harbor the curated data
curated_tickets = Table(
    "curated_tickets",
    metadata,
    Column("ticket_id", String, primary_key=True),
    Column("user_id", String, nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("message_text", Text),

    Column("channel", String(20), nullable=False),
    Column("agent_id", String),

    Column("sentiment", String(10)),
    Column("topic", String(50)),
    Column("urgency_score", Float),
    Column("priority", String(10), nullable=False),

    Column("ingestion_time", DateTime, nullable=False, default=datetime.utcnow),
    Column("pipeline_version", String(20), nullable=False),
)

# Creates the Database
def init_db():
    metadata.create_all(engine)