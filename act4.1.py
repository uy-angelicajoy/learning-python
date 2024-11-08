# list of favorite foods
# list = ['adobo', 'sinigang', 'fries', 'chicken', 'cookies']
# ans = int (input(f"Enter an index from 0 to 4: {} "))
# print (ans)

index = int (input("Enter an index from 0 to 4: "))

list = ['adobo', 'sinigang', 'fries', 'chicken', 'cookies']
print (list[index])

list = ['adobo', 'sinigang', 'fries', 'chicken', 'cookies']
list.remove()
print (list)

fruits = ["Strawberries", "Spinach", "Kale"]
vegetables = ["Tomatoes", "Celery", "Potatoes"]
food = [fruits, vegetables]
print(food[0][2])

# DRY - Don't Repeat Yourself

for number in range(5):
    if number == 3:
        print ("_")
        break
    print(number)

message = "Starting loop"
while message != "exit":
    print(message)
    message = input("Enter your message: ")
   
print("Loop Ended")

def greet():
    print("Hello World!")
greet()

message = "Hello World!"
def greet():
    message = "Hi There!"
    print(message)

greet()
print(message)


def greet():
    global message
    message = "Hello World!"

greet()
print(message)

message = "Hello World!"
def greet():
    # global message
    message = "Hi There!"
    print(message)

greet()
print(message)

def celsius_to_fahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

celsius = celsius_to_fahrenheit(36)
print(celsius)

def get_message ():
    return "Hello World"
print (get_message())

counter = 0
def get_count ():
    counter = 2
    counter += 1
print (get_count())