#Tuple, Dictionary, and Function Argument Types
dict = { "message": "Hello world!" }
dict["language"] = "english"
print(dict)
dict["message"] = "Hi There!"
print (dict)
dict = {}
print (dict)

if "message" in dict:
    print (dict["message"])


dict = { "message": "Hello world!" }
dict["message"] = "Hi There!"
print(dict)

dict = {
 "message": "Hello wordl!",
 "language": "english",
 "response": "Hi there!",
}

for key in dict:
  print(key)

for key in dict:
  print(dict[key])


for key in dict:
  print(f"{key} : {dict[key]}")

response = (200, 
            {'Content-Type' : 'application/json'},
            '{"name" : "Alice"}')
status_code, headers, body = response
print (type (status_code),  type (headers), type (body))

def sum(num1, num2=5, num3=10):
    return num1 + num2 +num3

print(sum(2, 13, 6))

def calculate(**kwargs):
    print(kwargs)

calculate(num_1=3, num_2=5, operator="+")

def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")

calculate(num_1=3, num_2=5, operator="+")


