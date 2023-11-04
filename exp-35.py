import matplotlib.pyplot as plt

# Marks for Mathematics and Science for 10 students
math_marks = [85, 90, 78, 92, 88, 76, 94, 80, 89, 82]
science_marks = [88, 92, 75, 91, 87, 77, 93, 81, 90, 84]

# Create a scatter plot comparing the two subjects
plt.scatter(math_marks, science_marks, marker='o', color='b')

# Set labels for the axes
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')

# Set the title of the plot
plt.title('Scatter Plot of Mathematics vs. Science Marks')

# Display the plot
plt.show()
