import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularity')
plt.title('Popularity of Programming Languages')
plt.gca().invert_yaxis()  # Reverse the order to have the most popular at the top
plt.show()
