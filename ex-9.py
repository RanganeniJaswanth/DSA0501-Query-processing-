import pandas as pd

# Sample sales_data DataFrame (replace this with your actual data)
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Manager': ['M1', 'M1', 'M2', 'M2', 'M3', 'M3', 'M4', 'M4'],
    'Salesperson': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'Sale': [100, 150, 200, 50, 120, 80, 180, 30]
}

sales_data = pd.DataFrame(data)

# Create a pivot table to find the total sale amount region-wise, manager-wise, and salesperson-wise
pivot_table = sales_data.pivot_table(index=['Region', 'Manager', 'Salesperson'], values='Sale', aggfunc='sum')

# Reset the index to have separate columns for Region, Manager, and Salesperson
pivot_table = pivot_table.reset_index()

# Rename the column for clarity
pivot_table.rename(columns={'Sale': 'Total Sale Amount'}, inplace=True)

# Display the pivot table
print(pivot_table)
