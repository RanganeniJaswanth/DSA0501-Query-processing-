import pandas as pd

# Create a sample DataFrame
data = {'Column1': ['Hello World', 'This is a test', 'Python is great']}
df = pd.DataFrame(data)

# Define the substring you want to find
substring = 'is'

# Find the index of the substring in the 'Column1' of the DataFrame
# This will return a Series with the index of the first occurrence of the substring in each row
index_series = df['Column1'].str.find(substring)

# Display the index Series
print(index_series)
