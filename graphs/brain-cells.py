import matplotlib.pyplot as plt

# Create some data points
time = [0, 1, 2, 3, 4, 5, 6, 7, 8]
brain_cells = [100, 75, 50, 25, 0, -25, -50, -75, -100]

# Plot the graph
plt.plot(time, brain_cells)

# Add labels and title
plt.xlabel('Time (hours)')
plt.ylabel('Brain cells (in mil)')
plt.title('Brain cells over time')

# Show the plot
plt.show()
