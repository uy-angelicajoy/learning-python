d = { 'a': 1, 'b': 2, 'c': 3 }
list(d.items())
[('a', 1), ('c', 3), ('b', 2)]
[(value, key) for key, value in d.items()]
[(1, 'a'), (3, 'c'), (2, 'b')]