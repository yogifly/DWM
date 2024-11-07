from itertools import combinations 
from collections import defaultdict 

def get_frequent_itemsets(transactions, min_support): 
    item_count = defaultdict(int) 

    for transaction in transactions: 
        for item in transaction: 
            item_count[item] += 1 

    frequent_itemsets = {frozenset([item]): count for item, count in item_count.items() if count >= min_support} 
    print("Single items and their support values:")
    for item, count in item_count.items():
        print(f"Item: {item}, Support: {count}")

    print("\nFrequent single itemsets (after filtering based on min support):")
    for itemset, count in frequent_itemsets.items():
        print(f"Frequent Itemset: {set(itemset)}, Support: {count}")

    all_frequent_itemsets = dict(frequent_itemsets) 
    k = 2

    while frequent_itemsets: 
        candidate_sets = defaultdict(int) 
        itemsets_list = list(frequent_itemsets.keys())
        for i in range(len(itemsets_list)): 
            for j in range(i + 1, len(itemsets_list)): 
                union_set = itemsets_list[i].union(itemsets_list[j]) 
                if len(union_set) == k: 
                    candidate_sets[union_set] = 0 

        for transaction in transactions: 
            transaction_set = frozenset(transaction) 
            for candidate in candidate_sets: 
                if candidate.issubset(transaction_set): 
                    candidate_sets[candidate] += 1 

        print(f"\nIteration {k-1}: Candidate sets and their support values:") 
        for itemset, count in candidate_sets.items(): 
            print(f"Candidate: {set(itemset)}, Support: {count}") 

        frequent_itemsets = {itemset: count for itemset, count in candidate_sets.items() if count >= min_support} 
        all_frequent_itemsets.update(frequent_itemsets) 

        print(f"\nIteration {k-1}: Frequent itemsets (after filtering):") 
        for itemset, count in frequent_itemsets.items(): 
            print(f"Frequent Itemset: {set(itemset)}, Support: {count}") 

        if not frequent_itemsets: 
            print(f"\nIteration {k-1}: No more frequent itemsets found.") 

        k += 1 

    return all_frequent_itemsets 

def print_association_rules(frequent_itemsets, min_confidence): 
    rules = [] 
    for itemset in frequent_itemsets: 
        if len(itemset) > 1: 
            for i in range(1, len(itemset)): 
                for subset in combinations(itemset, i): 
                    subset = frozenset(subset) 
                    if subset in frequent_itemsets: 
                        confidence = frequent_itemsets[itemset] / frequent_itemsets[subset] 
                        if confidence >= min_confidence: 
                            rules.append((subset, itemset.difference(subset), confidence)) 

    return rules 

transactions = [ 
    ['11', '12', '15'], 
    ['12', '14'], 
    ['12', '13'], 
    ['11', '12', '14'], 
    ['11', '13'], 
    ['12', '13'], 
    ['11', '13'], 
    ['11', '12', '13', '15'], 
    ['11', '12', '13'], 
] 

min_support = 2 
min_confidence = 0.6 

print(f"Number of transactions: {len(transactions)}") 
num_items = sum(len(transaction) for transaction in transactions) 
print(f"Number of items in transactions: {num_items}") 

frequent_itemsets = get_frequent_itemsets(transactions, min_support) 
print(f"\nFinal Frequent Item Set: {list(frequent_itemsets.keys())}") 

association_rules = print_association_rules(frequent_itemsets, min_confidence) 
print("\nAssociation Rules:") 
for rule in association_rules: 
    antecedent, consequent, confidence = rule 
    print(f"{set(antecedent)} -> {set(consequent)}, confidence: {confidence:.2f}")
