# Get First number from user and store into another variable
num1 = int (input("Enter first number: "))

# Get Second number from user and store into another variable
num2 = int (input("Enter second number: "))

# Get Third number from user and store into another variable
num3 = int (input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print ("The highest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print ("The highest number is", num2)
else:
    print ("The highest number is", num3)