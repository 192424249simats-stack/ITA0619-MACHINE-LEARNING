from sklearn.tree import DecisionTreeClassifier, export_text

# Dataset
X = [
    ['Sunny', 'Hot', 'High', 'Weak'],
    ['Sunny', 'Hot', 'High', 'Strong'],
    ['Overcast', 'Hot', 'High', 'Weak'],
    ['Rain', 'Mild', 'High', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Strong'],
    ['Overcast', 'Cool', 'Normal', 'Strong'],
    ['Sunny', 'Mild', 'High', 'Weak'],
    ['Sunny', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'Normal', 'Weak'],
    ['Sunny', 'Mild', 'Normal', 'Strong'],
    ['Overcast', 'Mild', 'High', 'Strong'],
    ['Overcast', 'Hot', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'High', 'Strong']
]

y = ['No','No','Yes','Yes','Yes','No','Yes',
     'No','Yes','Yes','Yes','Yes','Yes','No']

# Convert categorical data to numbers
from sklearn.preprocessing import LabelEncoder

X = list(zip(*X))
encoders = []

for column in X:
    le = LabelEncoder()
    encoders.append(le)
    le.fit(column)

X_encoded = []
for row in zip(*X):
    X_encoded.append([
        encoders[i].transform([row[i]])[0]
        for i in range(4)
    ])

# Create ID3 Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_encoded, y)

# Display tree
print("Decision Tree:")
print(export_text(model, feature_names=
                  ['Outlook', 'Temperature', 'Humidity', 'Wind']))

# Classify new sample
sample = ['Sunny', 'Cool', 'High', 'Strong']

sample_encoded = [[
    encoders[i].transform([sample[i]])[0]
    for i in range(4)
]]

prediction = model.predict(sample_encoded)

print("\nNew Sample:", sample)
print("Prediction:", prediction[0])
