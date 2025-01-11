# import time

# def count(value):
#     print("Start counting")
#     for counter in range(value):
#         print(counter + 1)
#         time.sleep(1)
#     print("Finished")

# count(3)
# count(5)
# count(10)

import time
import threading

# def count(value):
#     print("Start counting")
#     for counter in range(value):
#         print(counter + 1)
#         time.sleep(1)
#     print(f"Finished thread {value}")

# thread_1 = threading.Thread(target=count, args=[3])
# thread_2 = threading.Thread(target=count, args=[5])
# thread_3 = threading.Thread(target=count, args=[10])

# thread_1.start()
# thread_2.start()
# thread_3.start()

# print("Finished all threads.")

# import time
# import threading

# def count(value):
#     print("Start counting")
#     for counter in range(value):
#         print(counter + 1)
#         time.sleep(1)
#     print("Finished")

# thread_1 = threading.Thread(target=count, args=[3])
# thread_2 = threading.Thread(target=count, args=[5])
# thread_3 = threading.Thread(target=count, args=[10])

# thread_1.start()
# thread_2.start()
# thread_3.start()

# thread_1.join()
# thread_2.join()
# thread_3.join()

# print("Finished all threads.")

try:
    file = open("my_file.txt")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("File does not exist.")