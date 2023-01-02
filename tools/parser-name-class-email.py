def extract_info(filename):
    # Initialize variables to store the name, class, and email
    name = None
    class_ = None
    email = None
    
    # Open the file and read through it line by line
    with open(filename, 'r') as f:
        for line in f:
            # Check if the line starts with "Name: "
            if line.startswith('Name: '):
                # Extract the name from the line
                name = line.split(': ')[1].strip()
            # Check if the line starts with "Class: "
            elif line.startswith('Class: '):
                # Extract the class from the line
                class_ = line.split(': ')[1].strip()
            # Check if the line starts with "Email: "
            elif line.startswith('Email: '):
                # Extract the email from the line
                email = line.split(': ')[1].strip()
    
    # If no name was found, return an error message
    if name is None:
        return "Error: No name found in file."
    # If no class was found, set class_ to [no class]
    if class_ is None:
        class_ = '[no class]'
    # If no email was found, set email to [no email]
    if email is None:
        email = '[no email]'
    
    # Return the extracted information as a tuple
    return (name, class_, email)

# To use this function, you would pass it the name of the file you want to read. For example:
info = extract_info('student_info.txt')
print(info)


