import pandas as pd

# Sample sales_data DataFrame (replace this with your actual data)
data = {
    'Item': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C'],
    'Sale': [100, 150, 200, 50, 120, 80, 180, 30]
}

sales_data = pd.DataFrame(data)

# Create a pivot table to find the maximum and minimum sale values for each item
pivot_table = sales_data.pivot_table(index='Item', values='Sale', aggfunc=['max', 'min'])

# Rename the columns for clarity
pivot_table.columns = ['Max Sale', 'Min Sale']

# Display the pivot table
print(pivot_table)
