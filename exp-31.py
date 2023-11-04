import matplotlib.pyplot as plt

# Sample data: scores by group and gender
groups = ['Group A', 'Group B', 'Group C', 'Group D']
men_scores = [70, 75, 80, 85]
women_scores = [65, 78, 82, 88]
error_men = [2, 3, 2, 4]  # Sample error bars for men
error_women = [3, 2, 3, 2]  # Sample error bars for women

# Define the width of the bars
bar_width = 0.35

# Create a list of X positions for the bars
x = range(len(groups))

# Create the stacked bar chart for men
plt.bar(x, men_scores, width=bar_width, label='Men', color='red', align='center', yerr=error_men, capsize=5)

# Create the stacked bar chart for women on top of men
plt.bar(x, women_scores, width=bar_width, label='Women', color='violet', align='center', yerr=error_women,
        bottom=men_scores, capsize=5)

# Set X-axis labels
plt.xlabel('Groups')
plt.xticks(x, groups)

# Set Y-axis label and title
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')

# Add a legend
plt.legend()

# Show the chart
plt.show()
