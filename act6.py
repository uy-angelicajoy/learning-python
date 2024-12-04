# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# pages = 0
# word_per_page = 0
# print(f"pages: {pages}, word_per_page: {word_per_page}")
# pages = int(input("Number of pages: "))
# print(f"pages after input: {pages}")
# word_per_page = int(input("Number of words per page: "))
# print(f"word_per_page after input: {word_per_page}")
# total_words = pages * word_per_page
# print(total_words)


def calculate_average (numbers):
    total = sum (numbers)
    average = total / len (numbers)
    return average

numbers = []
user_input = input ("Enter a number: ")
while user_input.isnumeric ():
    numbers.append (int(user_input))
    user_input = input ("Enter a number: ")
    
print ("Average: ", calculate_average (numbers))