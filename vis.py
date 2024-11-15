import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import sys

def create_visualization(file_path):
    data = pd.read_csv(file_path)

    plt.scatter(data['Age'], data['Annual Income (k$)'], c=data['Spending Score (1-100)'], cmap='viridis')
    plt.xlabel('Age')
    plt.ylabel('Annual Income (k$)')
    plt.title('Age vs. Annual Income Colored by Spending Score')
    plt.colorbar(label='Spending Score (1-100)')
    plt.savefig('vis.png')
    print("Visualization saved as vis.png.")

    subprocess.run(['python3', 'model.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_visualization(sys.argv[1])
    else:
        print("Please provide the file path for visualization.")
