def invert(dictionary):
    return {key: value for value, key in dictionary.items()}


s = {"a": 1, "b": 2, "c": 3}
print(invert(s))