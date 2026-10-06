# FIND-S Algorithm

import csv

# Training data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initial hypothesis
h = ['0', '0', '0', '0', '0', '0']

print("Training Examples:")
for row in data:
    print(row)

# FIND-S algorithm
for example in data:
    if example[-1] == 'Yes':       # Consider only positive examples
        for i in range(len(h)):
            if h[i] == '0':
                h[i] = example[i]
            elif h[i] != example[i]:
                h[i] = '?'

print("\nMost Specific Hypothesis:")
print(h)
