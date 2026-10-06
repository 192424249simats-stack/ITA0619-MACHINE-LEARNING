import csv

# Read data from CSV file
with open("training_data.csv", "r") as file:
    data = list(csv.reader(file))

# Remove header
header = data[0]
data = data[1:]

# Number of attributes
num_attributes = len(data[0]) - 1

# Initialize Specific boundary
S = ['0'] * num_attributes

# Initialize General boundary
G = [['?'] * num_attributes]


# Function to check whether hypothesis covers example
def covers(h, example):
    for i in range(num_attributes):
        if h[i] != '?' and h[i] != example[i]:
            return False
    return True


# Candidate-Elimination Algorithm
for example in data:

    attributes = example[:-1]
    target = example[-1]

    if target == "Yes":

        # Remove hypotheses from G that don't cover positive example
        G = [g for g in G if covers(g, attributes)]

        # Generalize S
        for i in range(num_attributes):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

    else:

        # Remove hypotheses from S that cover negative example
        if covers(S, attributes):
            for i in range(num_attributes):
                if S[i] == '?':
                    continue
                if S[i] == attributes[i]:
                    S[i] = '?'

        # Specialize G
        new_G = []

        for g in G:
            if covers(g, attributes):
                for i in range(num_attributes):
                    if g[i] == '?':
                        if S[i] != '?' and S[i] != '0':
                            new_h = g.copy()
                            new_h[i] = S[i]
                            new_G.append(new_h)
            else:
                new_G.append(g)

        G = new_G


# Display result
print("Specific Boundary (S):")
print(S)

print("\nGeneral Boundary (G):")
for g in G:
    print(g)
