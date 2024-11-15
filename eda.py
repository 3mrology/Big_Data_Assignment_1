# eda.py
import pandas as pd
import sys
import subprocess

def eda_insights(file_path):
    data = pd.read_csv(file_path)

    insights = []
    avg_age = data['Age'].mean()
    insights.append(f"The average age of customers is {avg_age:.2f}.\n")

    max_income = data['Annual Income (k$)'].max()
    insights.append(f"The maximum annual income is {max_income}k$.\n")

    spend_score_mean = data['Spending Score (1-100)'].mean()
    insights.append(f"The average spending score is {spend_score_mean:.2f}.\n")

    for i, insight in enumerate(insights, 1):
        with open(f'eda-in-{i}.txt', 'w') as file:
            file.write(insight)

    print("EDA insights saved.")

    subprocess.run(['python3', 'vis.py', file_path])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        eda_insights(sys.argv[1])
    else:
        print("Please provide the file path for EDA.")
