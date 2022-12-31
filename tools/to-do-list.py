# Define a ToDoList class
class ToDoList:
    def __init__(self):
        # Initialize an empty list to store the items
        self.items = []
        
    def add_item(self, item):
        # Add an item to the list
        self.items.append(item)
        
    def remove_item(self, item):
        # Remove an item from the list
        self.items.remove(item)
        
    def mark_done(self, item):
        # Mark an item as done
        index = self.items.index(item)
        self.items[index] = "DONE: " + item
        
    def print_list(self):
        # Print the list
        for item in self.items:
            print(item)

# Create a new to-do list
todo_list = ToDoList()

# Add some items to the list
while True:
    item = input("Enter a new item (or press Enter to stop adding items): ")
    if item == "":
        break
    todo_list.add_item(item)

# Print the list
print("Original list:")
todo_list.print_list()

# Mark items as done
while True:
    item = input("Enter the item to mark as done (or press Enter to stop marking items as done): ")
    if item == "":
        break
    todo_list.mark_done(item)

# Print the updated list
print("\nUpdated list:")
todo_list.print_list()
