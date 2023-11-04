import matplotlib.pyplot as plt
import random

# Number of data points
num_points = 50

# Generate random data for X and Y
x_data = [random.random() for _ in range(num_points)]
y_data = [random.random() for _ in range(num_points)]

# Create a scatter plot with empty circles
plt.scatter(x_data, y_data, marker='o', facecolor='none', edgecolor='b')

# Set labels for the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the plot
plt.title('Random Scatter Plot with Empty Circles')

# Display the plot
plt.show()
