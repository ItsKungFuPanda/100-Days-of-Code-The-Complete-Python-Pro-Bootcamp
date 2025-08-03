#Install pyfiglet 
#pip install pyfiglet
import pyfiglet

# Text to print
text = input("Enter your name:)

# Create ASCII art
ascii_art = pyfiglet.figlet_format(text)

# Print the ASCII art
print(ascii_art)
