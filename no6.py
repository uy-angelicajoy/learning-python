num = int (input("Enter  2 digit number: "))

ones = num % 10
tens = num // 10

digits = ones + tens
print ("sum of digits", digits)