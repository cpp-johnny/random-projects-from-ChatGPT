import tkinter as tk

# Create the main window
window = tk.Tk()

# Create a counter variable
counter = 0

# Define a function that will be called when the button is clicked
def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=str(counter))

# Create the button
button = tk.Button(window, text="Click me!", command=increment_counter)
button.pack()

# Create the label
counter_label = tk.Label(window, text="0")
counter_label.pack()

# Start the main loop
window.mainloop()
