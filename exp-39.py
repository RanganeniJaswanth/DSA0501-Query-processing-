import pandas as pd

# Create a dictionary with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame with the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
