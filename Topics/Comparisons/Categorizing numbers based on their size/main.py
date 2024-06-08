# You can get input from a user with the input() function
user_input = input()

# Convert the input to an integer so that you can perform comparisons
num = int(user_input)

# After this, you can perform comparisons. You will need to write an if-elif-else structure to check if the number is greater than 
# or equal to 100, less than 100 but greater than or equal to 50, or less than 50. Depending on the outcome, you will need to print 
# 'big number', 'medium number', or 'small number'. Remember, to compare numbers you use the comparison operators <, <=, >, >=, ==, and !=.

if num >= 100:
    print('big number')
elif num >= 50:
    print('medium number')
else:
    print('small number')
