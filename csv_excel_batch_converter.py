import os
import glob
from pathlib import Path

import pandas as pd

INPUT_DIR = "input"
OUTPUT_DIR = "output"
ENCODINGS = ["utf-8-sig", "cp932", "utf-16"]

def get_csv_files():
    csv_path = os.path.join(INPUT_DIR, "*.csv")
    csv_files = glob.glob(csv_path)

    return csv_files

def read_csv_file(csv_file):
    

    for encoding in ENCODINGS:
        try:
            df = pd.read_csv(csv_file, encoding=encoding)
            print(f"Read with {encoding}: {csv_file}")
            return df

        except UnicodeDecodeError:
            print(f"Encoding failed: {encoding}")

    print(f"Failed to read: {csv_file}")
    return None

def make_output_path(csv_file):
    file_name = Path(csv_file).stem
    output_file = f"{file_name}.xlsx"
    output_path = os.path.join(OUTPUT_DIR, output_file)

    return output_path

def save_excel(df, output_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df.to_excel(output_path, index=False)

    print(f"Saved: {output_path}")

def convert_csv_to_excel(csv_file):
    df = read_csv_file(csv_file)

    if df is None:
        return

    if len(df) == 0:
        print(f"Empty file: {csv_file}")
        return

    output_path = make_output_path(csv_file)
    print(f"Rows: {len(df)}")

    save_excel(df, output_path)

def main():
    csv_files = get_csv_files()

    if len(csv_files) == 0:
        print("No CSV files found.")
        return

    for csv_file in csv_files:
        convert_csv_to_excel(csv_file)
        print()

if __name__ == "__main__":
    main()
    