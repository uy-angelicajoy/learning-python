user = int (input ("Enter a number: "))

if user % 3 == 0 and user % 5 == 0:
    print ("Bigyan ng jacket!")
elif user % 5 == 0:
    print ("Horaaay")
elif  user %  3 == 0:
    print ("Hep! Hep!")
else:
    print (f"{user}Tawsan")