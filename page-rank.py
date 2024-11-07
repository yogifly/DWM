import string

def main():
    print("Program for Page Rank")
    it = int(input("Enter number of iterations: "))
    factor = float(input("Enter teleportation factor (between 0 and 1): "))
    n = int(input("Enter number of variables: "))

    store_list = {char: 1/n for char in string.ascii_lowercase[:n]}
    matrix = []
   
    print("Enter the adjacency matrix values row by row (space-separated 0s and 1s):")
    for i in range(n):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
   
    print("\nThe entered matrix is:")
    for row in matrix:
        print(row)
   
    print("\nInitial page ranks:")
    for key, value in store_list.items():
        print(f"{key}: {value:.4f}")

    for x in range(1, it + 1):
        print(f"\nIteration {x}:")
        for i in range(n):
            inbound_sum = 0
            contributions = []
           
            for j in range(n):
                if matrix[j][i] == 1: 
                    outbound_links = sum(matrix[j]) 
                    if outbound_links > 0:

                        contribution = store_list[string.ascii_lowercase[j]] / outbound_links
                        inbound_sum += contribution
                        contributions.append(f"PR({string.ascii_lowercase[j]})/{outbound_links} = {store_list[string.ascii_lowercase[j]]}/{outbound_links} = {contribution:.4f}")

            new_rank = (1 - factor) + factor * inbound_sum
            store_list[string.ascii_lowercase[i]] = new_rank

            print(f"\nCalculation for {string.ascii_lowercase[i]}:")
            print(f"PR({string.ascii_lowercase[i]}) = (1 - {factor}) + {factor} * ({' + '.join(contributions)})")
            print(f"PR({string.ascii_lowercase[i]}) = {1 - factor:.4f} + {factor} * {inbound_sum:.4f} = {new_rank:.4f}")

        print("\nUpdated page ranks:")
        for key, value in store_list.items():
            print(f"{key}: {value:.4f}")

    highest_node = max(store_list, key=store_list.get)
    highest_value = store_list[highest_node]
    print(f"\nThe node with the highest PageRank is '{highest_node}' with a value of {highest_value:.4f}.")

if __name__ == '__main__':
    main()
