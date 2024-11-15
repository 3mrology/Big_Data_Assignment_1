import pandas as pd
import subprocess
import time
import sys
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        data.to_csv('loaded_data.csv', index=False)
        time.sleep(1)
        subprocess.run(['python3', 'dpre.py', 'loaded_data.csv'])
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        load_data(sys.argv[1])
    else:
        print("Please provide the file path for dataset.")
