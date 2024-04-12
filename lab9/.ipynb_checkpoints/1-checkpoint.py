#Q1
import pandas as pd

# Load the dataset
df = pd.read_csv('training_titanic.csv')

# A. How many people survived the disaster?
survived_count = df['Survived'].sum()

# B. How many people died?
total_passengers = df['Survived'].count()
died_count = total_passengers - survived_count

# C. Calculate the survival rates as proportions (percentage)
survival_rate = (survived_count / total_passengers) * 100

# D. Males that survived vs males that passed away
males_survived = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
males_died = df[(df['Sex'] == 'male') & (df['Survived'] == 0)].shape[0]

# E. Females that survived vs Females that passed away
females_survived = df[(df['Sex'] == 'female') & (df['Survived'] == 1)].shape[0]
females_died = df[(df['Sex'] == 'female') & (df['Survived'] == 0)].shape[0]

# F. Does age play a role? Since it's probable that children were saved first.
# Assuming children are those under 18 years old
children_survived = df[(df['Age'] < 18) & (df['Survived'] == 1)].shape[0]
adults_survived = df[(df['Age'] >= 18) & (df['Survived'] == 1)].shape[0]

# Print the results
print(f"A. Number of people who survived: {survived_count}")
print(f"B. Number of people who died: {died_count}")
print(f"C. Survival rate: {survival_rate:.2f}%")
print(f"D. Males that survived vs males that passed away: {males_survived} survived, {males_died} died")
print(f"E. Females that survived vs females that passed away: {females_survived} survived, {females_died} died")
print(f"F. Children that survived: {children_survived}, Adults that survived: {adults_survived}")