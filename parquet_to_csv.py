import pandas as pd
import argparse
import os

def convert_parquet_to_csv(parquet_file, csv_file=None):
    if not os.path.isfile(parquet_file):
        raise FileNotFoundError(f"File not found: {parquet_file}")
    
    df = pd.read_parquet(parquet_file)

    if csv_file is None:
        csv_file = parquet_file.replace(".parquet", ".csv")

    df.to_csv(csv_file, index=False)
    print(f"✅ Converted to: {csv_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a Parquet file to CSV.")
    parser.add_argument("parquet_file", help="Path to the input Parquet file")
    parser.add_argument("--output", "-o", help="Optional: Path to the output CSV file")
    args = parser.parse_args()

    convert_parquet_to_csv(args.parquet_file, args.output)
