# --------------------------------------------------------
# Name: Randy Easton
# Date: 6/1/2025
# Assignment: On the Wall + Flowchart(s) Module 1.3
# --------------------------------------------------------
# Purpose:
# Countdown function that prints lyrics of "X bottles of beer on the wall"
# from user-specified number down to 0, including custom final message.
# --------------------------------------------------------
def countdown(start):
    """
    Prints the 'Bottles of Beer' countdown song from `start` down to 0.
    """

    n = start
    while n != 1: # Prints Plural Verses
        print(n,"bottles of beer on the wall,",n,"bottles of beer.")
        n -=1
        print("Take one down and pass it around,",n,"bottles of beer on the wall.\n")
    if n ==1: # Prints Singular Verse
        print(n, "bottle of beer on the wall,", n, "bottle of beer.")
        n -= 1
        print("Take one down and pass it around,", n, "bottles of beer on the wall.\n")
    if n == 0: # Prints end-of-song message
        return "Time to buy more bottles of beer!"

def main():
    # Main function to control program flow
    while True: # Loo[ for asking for input
        try:
            bottles = int(input("Hey! How many bottles of beer are on the wall?: "))
            if bottles < 1: # Validates input
                print("Please enter a whole number greater than 0.")
            else:
                countdown(bottles)
                break
        except ValueError:
            print("Oops! Please enter a whole number only.")

if __name__ == "__main__":
    main()