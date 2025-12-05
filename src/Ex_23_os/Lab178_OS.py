import os

# with open ("intro.txt",'r') as file:
#     print(file.read())


#full_path = os.path.join("C:\Users\koujalgi\PycharmProjects\PyATB6xLearning\src\Ex_22Collection","intro.txt")

full_path = os.path.join(os.getcwd(),'intro.txt')
print(full_path)

print(os.getcwd())

file = open(full_path,'r')
print(file.read())