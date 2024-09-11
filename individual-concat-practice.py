# Thayer Yang
# 11 SEP 2024
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in
city = input("What city do you live in?\n")
state = input("What state do you live in?\n")

print(city.capitalize()+", "+state.capitalize())


# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message
welcome_message = input("Give a welcoming message:\n")
first_name = input("Enter your first name:\n")

print(welcome_message.capitalize()+", "+first_name.capitalize())



# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age
age = input("How old are you?\n")

print(first_name.capitalize()+" is "+str(age)+" years old.")





# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches

height = input("How tall are you in inches? (1 ft = 12 inches)\n")
last_name = input('What is your last name?\n')

print(f"{first_name.capitalize()} {last_name.capitalize()} is {str(height)} inches tall.")