import numpy as np
import matplotlib.pyplot as plt

# Generate sample data for three groups
np.random.seed(0)
group1_heights = np.random.normal(160, 10, 50)
group1_weights = np.random.normal(60, 5, 50)

group2_heights = np.random.normal(170, 10, 50)
group2_weights = np.random.normal(70, 5, 50)

group3_heights = np.random.normal(180, 10, 50)
group3_weights = np.random.normal(80, 5, 50)

# Create a scatter plot for each group
plt.scatter(group1_weights, group1_heights, label='Group 1', c='r', marker='o')
plt.scatter(group2_weights, group2_heights, label='Group 2', c='g', marker='s')
plt.scatter(group3_weights, group3_heights, label='Group 3', c='b', marker='^')

# Set labels and title
plt.xlabel('Weight (kg)')
plt.ylabel('Height (cm)')
plt.title('Scatter Plot of Weight vs. Height for Three Groups')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
