# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/11/2025
# Assignment: Module 9: JSON and Application Programming Interfaces (APIs)
# --------------------------------------------------------
# Purpose:
# [Brief one-sentence description of what the program does]
# --------------------------------------------------------


import requests

def main():
    # Main function to control program flow
    OpenNotify = 'http://api.open-notify.org/'
    response = requests.get(OpenNotify)

    print(response.status_code)

    pass  # Replace with your code


# Function definitions go here
# Use descriptive names and explain any non-obvious logic
# Example:
def example_function():
    """
    Describe what this function does.
    """
    pass


# Program starts here
if __name__ == "__main__":
    main()
