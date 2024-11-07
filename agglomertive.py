import numpy as np 
from scipy.cluster.hierarchy import linkage, dendrogram 
import matplotlib.pyplot as plt 
import pandas as pd 
from scipy.spatial.distance import pdist, squareform 

# New Data points (values)
points = np.array([10, 15, 25, 30, 50, 60]) 
full_distances = np.abs(points[:, None] - points)
condensed_distances = squareform(full_distances)
labels = ['10', '15', '25', '30', '50', '60'] 

def print_matrix_and_clusters(matrix, step, labels, clusters): 
    df = pd.DataFrame(matrix, columns=labels, index=labels) 
    print(f"\nDistance matrix at step {step}:\n", df) 
    print(f"Clusters at step {step}:") 
    for i, cluster in enumerate(clusters): 
        print(f"Cluster {i+1}: {cluster}") 

def single_linkage_clustering(dist_matrix):
    global labels 
    n = dist_matrix.shape[0] 
    current_matrix = dist_matrix.copy() 
    step = 1 
    clusters = [[label] for label in labels] 
    
    while n > 1: 
        min_dist = np.inf 
        for i in range(len(current_matrix)): 
            for j in range(i + 1, len(current_matrix)): 
                if current_matrix[i, j] < min_dist: 
                    min_dist = current_matrix[i, j] 
                    cluster_a, cluster_b = i, j 

        print_matrix_and_clusters(current_matrix, step, labels, clusters) 
        
        new_cluster = np.minimum(current_matrix[cluster_a], current_matrix[cluster_b]) 

        new_matrix = np.zeros((n-1, n-1)) 
        indices = [x for x in range(len(current_matrix)) if x != cluster_a and x != cluster_b] 

        new_matrix[:-1, :-1] = current_matrix[np.ix_(indices, indices)] 
        new_matrix[-1, :-1] = new_matrix[:-1, -1] = new_cluster[indices]
        current_matrix = new_matrix 

        new_label = f"({labels[cluster_a]},{labels[cluster_b]})" 
        labels = [labels[i] for i in indices] + [new_label] 

        new_cluster_list = clusters[cluster_a] + clusters[cluster_b] 
        clusters = [clusters[i] for i in indices] + [new_cluster_list] 
        n -= 1 
        step += 1 

    print_matrix_and_clusters(current_matrix, step, labels, clusters) 

single_linkage_clustering(full_distances) 

Z = linkage(condensed_distances, method='single') 
plt.figure(figsize=(8, 6)) 
dendrogram(Z, labels=['10', '15', '25', '30', '50', '60']) 
plt.title('Single Linkage Dendrogram') 
plt.xlabel('Cluster') 
plt.ylabel('Distance') 
plt.show()
