import pandas as pd
import numpy as np

# Create a random DataFrame with 10 rows and 4 columns
data = np.random.randn(10, 4)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

# Define a function to apply color formatting
def highlight_numbers(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply the formatting function to the entire DataFrame
styled_df = df.style.applymap(highlight_numbers)

# Display the styled DataFrame
styled_df
