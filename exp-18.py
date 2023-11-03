import pandas as pd

# Sample DataFrame
data = {
    'School Code': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'C', 'C'],
    'Class': ['Math', 'Math', 'Science', 'Science', 'Math', 'Science', 'Math', 'Math', 'Science'],
    'Score': [85, 90, 78, 88, 92, 84, 89, 75, 80]
}

df = pd.DataFrame(data)

# Group the DataFrame by 'School Code' and 'Class'
grouped = df.groupby(['School Code', 'Class'])

# Iterate through the groups and print each group
for (school, class_), group in grouped:
    print(f'School: {school}, Class: {class_}')
    print(group)
    print()
