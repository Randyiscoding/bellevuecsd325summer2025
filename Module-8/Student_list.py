# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/9/2025
# Assignment: [Insert Assignment Name or Number Here]
# --------------------------------------------------------
# Purpose:
# [Brief one-sentence description of what the program does]
# --------------------------------------------------------
import json

def main():
    # Main function to control program flow
    with open('student.json', 'r') as student_data:
        student_list = dict(json.load(student_data))
    print(student_list)
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
