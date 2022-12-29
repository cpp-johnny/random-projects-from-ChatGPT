import matplotlib.pyplot as plt
import numpy as np

# Set the range of x values
x = np.linspace(0, 2*np.pi, 100)

# Compute the y values for the sine function
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the sine curve
ax.plot(x, y)

# Add labels and show the plot
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()
