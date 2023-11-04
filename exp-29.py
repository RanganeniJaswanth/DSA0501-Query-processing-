import matplotlib.pyplot as plt

# Programming languages and their popularity
languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#']
popularity = [30, 25, 20, 15, 10]  # You can replace these values with your data

# Define different colors for the bars
colors = ['blue', 'green', 'red', 'purple', 'orange']

# Create a bar chart
plt.figure(figsize=(10, 6))  # Set the figure size
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Show the chart
plt.show()
