'''Escape Sequence character: In Python, escape characters are used to represent certain special characters that are difficult or impossible to type directly in a string. These characters are preceded by a backslash (\) and enable you to insert characters like newlines, tabs, quotes, or even a backslash itself into a string. '''

# \n --> Newline – Moves the cursor to the next line.
print("Hello, World!\nWelcome to Python.")
# \t --> Tab – Adds a horizontal tab.
print("Name\tAge\tLocation")
# \\ --> Backslash – Inserts a literal backslash.
print("This is a backslash: \\")
# \' --> Single Quote – Inserts a single quote inside a single-quoted string.
print('It\'s a great day!')
# \" --> Double Quote – Inserts a double quote inside a double-quoted string.
print("He said, \"Hello!\"")
# \r --> Carriage Return – Moves the cursor to the beginning of the line.
print("Hello, World!\rHi")
# \b --> Backspace – Moves the cursor one position back, effectively deleting the last character.
print("Hello, World!\b")
# \f --> Form Feed – Moves the cursor to the next page.
print("Hello\fWorld!")
# \v --> Vertical Tab – Moves the cursor vertically.
print("Hello\vWorld!")
# \xhh --> Hexadecimal – Represents a character using hexadecimal value hh.
# Define a string with hexadecimal escape sequences
print("Hello \x48\x65\x6C\x6C\x6F")

