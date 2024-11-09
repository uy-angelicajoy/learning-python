def key_highest_value(d):
    if not d:
        return None  # Return None if the dictionary is empty
    return max(d, key=d.get)

my_dict = {'John': 80, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
print(key_highest_value(my_dict))  # Output: 'b'
