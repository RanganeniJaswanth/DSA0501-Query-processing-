import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create a figure with multiple subplots
plt.figure(figsize=(12, 4))

# Create the first subplot
plt.subplot(131)  # 1 row, 3 columns, 1st subplot
plt.plot(x, y1, label='sin(x)')
plt.title('Sine Function')
plt.legend()

# Create the second subplot
plt.subplot(132)  # 1 row, 3 columns, 2nd subplot
plt.plot(x, y2, label='cos(x)')
plt.title('Cosine Function')
plt.legend()

# Create the third subplot
plt.subplot(133)  # 1 row, 3 columns, 3rd subplot
plt.plot(x, y3, label='tan(x)')
plt.title('Tangent Function')
plt.legend()

# Adjust the layout to prevent overlapping
plt.tight_layout()

# Display the plots
plt.show()
