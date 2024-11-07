import numpy as np
import random

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def calculate_mean(clusters, data):
    means = []
    for cluster in clusters:
        means.append(np.mean(data[cluster], axis=0))
    return means

def k_means(data, k):
    if data.ndim == 1:
        data = data[:, np.newaxis]

    print("1. Elements of data set:")
    print(data.tolist())

    print(f"\n2. Cluster size k={k}")
    centroids = data[random.sample(range(len(data)), k)]
    iteration = 0

    while True:
        print(f"\nIteration {iteration + 1}:")
        
        new_clusters = [[] for _ in range(k)]
        for i, point in enumerate(data):
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            new_clusters[closest_centroid].append(i)
        new_centroids = calculate_mean(new_clusters, data)

        if iteration == 0:
            print("\n3. Initial clusters:")
        else:
            print("\n4. Updated clusters:")

        for i, cluster in enumerate(new_clusters):
            print(f"Cluster {i + 1}: {data[cluster].tolist()}")

        print("\nMean of clusters:")
        print([float(mean[0]) for mean in new_centroids])

        if np.allclose(centroids, new_centroids):
            print("\n5. Clusters have stabilized. Final clusters and means:")
            for i, cluster in enumerate(new_clusters):
                print(f"Final Cluster {i + 1}: {data[cluster].tolist()}")
            print("Final Mean of clusters:")
            print([float(mean[0]) for mean in new_centroids])
            break

        centroids = new_centroids
        iteration += 1

data = np.array([11, 22, 33, 44, 55, 10, 20])
k = 2
k_means(data, k)
