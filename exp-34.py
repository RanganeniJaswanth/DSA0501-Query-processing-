import matplotlib.pyplot as plt
import random

# Number of data points (balls)
num_balls = 50

# Generate random data for X and Y positions
x_positions = [random.random() for _ in range(num_balls)]
y_positions = [random.random() for _ in range(num_balls)]

# Generate random data for the sizes of the balls
ball_sizes = [random.uniform(10, 100) for _ in range(num_balls)]

# Create a scatter plot with random positions and sizes
plt.scatter(x_positions, y_positions, s=ball_sizes, alpha=0.5)

# Set labels for the axes
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the plot
plt.title('Scatter Plot with Randomly Sized Balls')

# Display the plot
plt.show()
