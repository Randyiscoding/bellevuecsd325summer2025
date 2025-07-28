# --------------------------------------------------------
# Name: Randy Easton
# Date: 7/28/2025
# Assignment: Django Basics
# --------------------------------------------------------
# Purpose:
# Urls for the current DJango app
# --------------------------------------------------------

from django.urls import path
from . import views

urlpatterns = [path("", views.home, name="home")]
def main():
    # Main function to control program flow
    pass


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
