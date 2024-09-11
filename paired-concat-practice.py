# Concatenation Practice


# Work with your assigned partner
# Each person in your team should take turns writing the code to create and display longer strings
# Check your partner's code for spelling, capitalization, and coding errors
# Correct any bugs in your code

# Part 1
# Create variables to store your first, middle, and last name
# Have Python print a message that contains your concatenated full name, i.e., your combined first, middle and last names
first_name = input("Enter your first name:\n")
middle_name = input("Enter your middle name:\n")
last_name = input("Enter your last name:\n")

print(first_name.capitalize()+" "+middle_name.capitalize()+" "+last_name.capitalize())


# Part 2
# Assume you're building a Space Invaders game
# Use concatenation to create and display a custom welcome message that includes the player's first name

print("Welcome "+first_name.capitalize()+" to Space Invaders!")

# Part 3
# Use concatenation to build and display a string that includes your first name, last name, and the year you were born
year = input("What year were you born in?\n")

print(first_name.capitalize()+" "+last_name.capitalize()+" was born in "+str(year)+".")


# Part 4
# Use concatenation to create and display a sentence that says which country in the world
# you would visit if money were no object

country = input("What is a country that you'd like to visit in the future?\n")

print(first_name.capitalize()+" would like to visit "+country.capitalize()+" in the future.")