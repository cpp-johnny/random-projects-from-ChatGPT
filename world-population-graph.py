import matplotlib.pyplot as plt

# Set the x and y values for the graph
x = [1900, 1950, 2000, 2050]
y = [1.65, 2.55, 6.1, 9.7]

# Create the line chart
plt.plot(x, y)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population (billions)')
plt.title('World Population')

# Show the graph
plt.show()
