import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Eve'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']}
df = pd.DataFrame(data)

# Specify the column you want to swap the cases for
column_to_swap = 'City'

# Swap the cases of the specified column
df[column_to_swap] = df[column_to_swap].str.swapcase()

# Print the updated DataFrame
print(df)
