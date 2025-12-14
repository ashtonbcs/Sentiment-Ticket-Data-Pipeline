import sys

from src.curate_pipeline import run_pipeline

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_pipeline.py <path_to_csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    run_pipeline(filepath)