characters = input ("input: ")

occurrence = {}

for elements in characters:
    if elements in occurrence:
        occurrence [elements] += 1
    else:
        occurrence [elements] = 1
        
print ("output: " + str (occurrence))