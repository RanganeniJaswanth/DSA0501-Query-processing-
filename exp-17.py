import pandas as pd

# Sample DataFrame
data = {
    'School Code': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'C', 'C'],
    'Age': [25, 30, 24, 29, 26, 27, 31, 28, 32]
}

df = pd.DataFrame(data)

# Group the DataFrame by 'School Code'
grouped = df.groupby('School Code')

# Calculate mean, min, and max values of age for each school
result = grouped['Age'].agg(['mean', 'min', 'max'])

# Rename the columns for clarity
result = result.rename(columns={'mean': 'Mean Age', 'min': 'Min Age', 'max': 'Max Age'})

# Display the result
print(result)
