import matplotlib.pyplot as plt

# Sample data: scores by group and gender
groups = ['Group A', 'Group B', 'Group C', 'Group D']
men_scores = [70, 75, 80, 85]
women_scores = [65, 78, 82, 88]

# Define the width of the bars
bar_width = 0.35

# Create a list of X positions for the bars
x = range(len(groups))

# Create the bar chart for men
plt.bar(x, men_scores, width=bar_width, label='Men', color='Green', align='center')

# Create the bar chart for women, shifted by bar_width
plt.bar([i + bar_width for i in x], women_scores, width=bar_width, label='Women', color='Orange', align='center')

# Set X-axis labels
plt.xlabel('Groups')
plt.xticks([i + bar_width/2 for i in x], groups)

# Set Y-axis label and title
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')

# Add a legend
plt.legend()

# Show the chart
plt.show()
