import pandas as pd
from collections import Counter

data_dict = [
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "Yes"},
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "Sports", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Yellow", "Type": "Sports", "Origin": "Imported", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Imported", "Stolen": "No"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Imported", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Red", "Type": "SUV", "Origin": "Imported", "Stolen": "No"},
    {"Color": "Red", "Type": "Sports", "Origin": "Imported", "Stolen": "Yes"}
]

data = pd.DataFrame(data_dict)
print("Dataset:")
print(data)

total_count = len(data_dict)
print(f"\nNumber of rows in the dataset: {total_count}")

features = ["Color", "Type", "Origin"]
label = "Stolen"
X = {"Color": "Red", "Type": "SUV", "Origin": "Domestic"}
print(f"\nNew tuple for classification: {X}")

label_counts = Counter([item[label] for item in data_dict])
P_yes = label_counts["Yes"] / total_count
P_no = label_counts["No"] / total_count
print(f"\nPrior probability P(Stolen = Yes): {P_yes}")
print(f"Prior probability P(Stolen = No): {P_no}")

def calculate_likelihood(feature, value, outcome):
    outcome_count = sum(1 for item in data_dict if item[label] == outcome)
    feature_count = sum(1 for item in data_dict if item[label] == outcome and item[feature] == value)
    likelihood = feature_count / outcome_count
    print(f"P({feature} = {value} | Stolen = {outcome}): {likelihood}")
    return likelihood

likelihood_yes = P_yes
likelihood_no = P_no
print("\nConditional probabilities:")
for feature in features:
    likelihood_yes *= calculate_likelihood(feature, X[feature], "Yes")
    likelihood_no *= calculate_likelihood(feature, X[feature], "No")

posterior_yes = likelihood_yes / (likelihood_yes + likelihood_no)
posterior_no = likelihood_no / (likelihood_yes + likelihood_no)
classification = "Yes" if posterior_yes > posterior_no else "No"
print(f"\nPosterior probability of being Stolen = Yes: {posterior_yes}")
print(f"Posterior probability of being Stolen = No: {posterior_no}")
print(f"\nThe tuple X is classified as: {classification}")
