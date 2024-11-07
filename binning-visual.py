#Binning
import numpy as np
def bin_boundaries(bins):
    boundary_bins = []
    for bin in bins:
        lower_bound = int(bin[0])
        upper_bound = int(bin[-1])
        boundary_bins.append([lower_bound if abs(x - lower_bound) <= abs(x - upper_bound) else upper_bound for x in bin])
    return boundary_bins

def binning_by_mean(bins):
    mean_bins = []
    for bin in bins:
        mean_value = np.mean(bin)
        mean_bins.append([float(mean_value)] * len(bin))  
    return mean_bins

def binning_by_median(bins):
    median_bins = []
    for bin in bins:
        median_value = np.median(bin)
        median_bins.append([float(median_value)] * len(bin))  
    return median_bins

def create_bins(data, num_bins):
    sorted_data = sorted(data)
    bins = np.array_split(sorted_data, num_bins)
    return sorted_data, bins

def main():
    data = [7, 9, 13, 15, 18, 19, 20, 23, 29, 31, 36, 39, 41, 45]
    num_bins = 3
    sorted_data, bins = create_bins(data, num_bins)
    mean_binned = binning_by_mean(bins)
    median_binned = binning_by_median(bins)
    boundaries_binned = bin_boundaries(bins)

    print("\nOriginal Dataset:", data)
    print("Sorted Dataset:", sorted_data)
    print("\nInitial Bins:")
    for i, bin in enumerate(bins, 1):
        print(f"Bin {i}: {bin.tolist()}")
   
    print("\nBinning by Mean:")
    for i, bin in enumerate(mean_binned, 1):
        print(f"Bin {i}: {bin}")
   
    print("\nBinning by Median:")
    for i, bin in enumerate(median_binned, 1):
        print(f"Bin {i}: {bin}")
   
    print("\nBinning by Boundaries:")
    for i, bin in enumerate(boundaries_binned, 1):
        print(f"Bin {i}: {bin}")

if __name__ == "__main__":
    main()

#visualization 
import matplotlib.pyplot as plt

def plot_bar_chart(data):
    labels = [f"Element {i+1}" for i in range(len(data))]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, data, color='blue')
    plt.xlabel('Chocolates')
    plt.ylabel('Values')
    plt.title('Bar Chart of Data')
    plt.show()

def plot_histogram(data):
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=5, color='green', edgecolor='black')
    plt.xlabel('Value Range')
    plt.ylabel('Frequency')
    plt.title('Histogram of Data')
    plt.show()

def main():
    data = [5, 15, 10, 20, 25, 30, 35, 40, 45, 50]

    print("\nCreating Bar Chart...")
    plot_bar_chart(data)
   
    print("\nCreating Histogram...")
    plot_histogram(data)

if __name__ == "__main__":
    main()
