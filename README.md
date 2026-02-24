# Python-Exercises
Python exercises, algorithm challenges, and projects demonstrating coding proficiency and problem-solving
=======
# Character Input – Practice Python Exercise 01

This is my solution to **Exercise 1** from the [Practice Python](https://www.practicepython.org) beginner series.

## Original Exercise (Character Input)

> Create a program that asks the user to enter their name and their age. Print out a message that tells them the year they will turn 100 years old.

**Extras implemented in this version:**

1. Ask the user for **another number** — how many times they want the message repeated.
2. Print that many copies of the message, **each on a separate line**.

> Note from the site: For this exercise they expect a simple year calculation (not using `datetime`). For a dynamic version using current date see Exercise 39.

## Features of this implementation

- Takes user’s name
- Takes age with basic validation (positive integer between 1–99)
- Calculates the year the user turns 100 using `date.today().year`
- Asks how many times to repeat the message
- Prints the message the requested number of times (one per line)
- Clean function-based structure for better readability
- Simple input error handling (try/except + range check)

## How to run

```bash
# Make sure you have Python 3
python character_input.py
# or if you renamed the file:
python main.py

- Example Run:
Please Enter Your Name: Alex
Please Enter Your Age:  28
How Many Times You Want to Repeat Your Answer?  3

Hello Alex! You will be 100 years old in 2072!
Hello Alex! You will be 100 years old in 2072!
Hello Alex! You will be 100 years old in 2072!

