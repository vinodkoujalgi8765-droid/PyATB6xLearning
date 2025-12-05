import os

try:
    with open ('vinod.txt', 'r') as file:
        file.read()
except FileNotFoundError:
    print('Please check file is created before read')
    print("Not in readable format")
    print("Empty File")

finally:
    print('Closing file')
