'''
Q - Create a function which will take the 3 values from the user,
which are length of the triangle.  side1, side2, side2
'''

side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

def triangle(side1,side2,side3):
    if side1== side2 ==side3:
        return "Eqilateral Triangle"
    elif side1==side2 or side1==side3 or side2==side3:
        return "Isosceles Triangle"
    elif side1!=side2!=side3:
        return "Sceles Triangle"
    else:
        return None

triangle1 = triangle(side1,side2,side3)



print(triangle1)