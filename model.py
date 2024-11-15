# model.py
import pandas as pd
from sklearn.cluster import KMeans
import sys

def apply_kmeans(file_path, k=3):
    data = pd.read_csv(file_path)
    clustering_data = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    kmeans = KMeans(n_clusters=k, random_state=0)
    data['Cluster'] = kmeans.fit_predict(clustering_data)

    cluster_counts = data['Cluster'].value_counts().sort_index()
    with open('k.txt', 'w') as file:
        for cluster, count in cluster_counts.items():
            file.write(f"Cluster {cluster}: {count} records\n")

    print("K-means clustering complete. Cluster counts saved in k.txt.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        apply_kmeans(sys.argv[1])
    else:
        print("Please provide the file path for K-means clustering.")
