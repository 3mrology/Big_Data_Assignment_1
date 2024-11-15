# dpre.py
import pandas as pd
import sys
import subprocess

def minimal_preprocessing(file_path):
    data = pd.read_csv(file_path)
    data.drop(data.columns[0], axis=1, inplace=True)
    data.drop_duplicates(inplace=True)  

    data.fillna(method='ffill', inplace=True)  
    if 'Gender' in data.columns:  
        data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

    data.to_csv('res_dpre.csv', index=False)
    print("Minimal preprocessing complete. Saved as res_dpre.csv.")

    subprocess.run(['python3', 'eda.py', 'res_dpre.csv'])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        minimal_preprocessing(sys.argv[1])
    else:
        print("Please provide the file path for data preprocessing.")
