import pandas as pd

# Create a dictionary with sample data
data = {
      'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['mumbai', 'hyderabad', 'banglore', 'america']
}

# Specify custom index labels
custom_index = ['Person1', 'Person2', 'Person3', 'Person4']

# Create a DataFrame with the dictionary and custom index labels
df = pd.DataFrame(data, index=custom_index)

# Display the DataFrame
print(df)
