from datetime import date

# Calculate the year when the user will turn 100
def calculate_year(age):
    return date.today().year + (100 - age)

# Print the message multiple times
def show_result(repeat, name, year):
    message = f"Hello {name}! You will be 100 years old in {year}!"
    for _ in range(repeat):
        print(message)

# Get a positive integer within optional bounds
def get_positive_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is None or value >= min_value) and (max_value is None or value <= max_value):
                return value
            print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid number!")

# Main program
name = input("Please Enter Your Name: ")
age = get_positive_int("Please Enter Your Age: ", 1, 99)
repeat = get_positive_int("How Many Times You Want to Repeat Your Answer? ", 1)

show_result(repeat, name, calculate_year(age))
