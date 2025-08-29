from math import pi, sqrt

def square(choice):
    side = int(input("\nEnter the side of the square: "))
    if(choice == 1):
        print("Circumference of Square is", 4*side)
        return
    elif(choice == 2):
        print("Area of Square is", side*side)
        return

def circle(choice):
    r = int(input("\nEnter the radius of the circle: "))
    if(choice == 3):
        print("Circumference of Circle is", 2*pi*r)
        return
    elif(choice == 4):
        print("Area of Circle is", pi*r*r)
        return

def rectangle(choice):
    l = int(input("\nEnter length of rectangle: "))
    b = int(input("Enter breadth of rectangle: "))
    if(choice == 5):
        print("Circumference of Rectangle is", 2*(l+b))
        return
    elif(choice == 6):
        print("Area of Rectangle is", l*b)
        return

def triangle(choice):
    side = int(input("\nEnter the side of the Triangle: "))
    if(choice == 7):
        print("Circumference of Triangle is", 3*side)
        return
    elif(choice == 8):
        h = sqrt((3*(side**2))/4)
        print("Area of Triangle is", h*side/2)
        return


print("MENU".center(40, '-'))
print("1. Calculate the circumference of square")
print("2. Calculate the area of square")
print("3. Calculate the circumference of circle")
print("4. Calculate the area of circle")
print("5. Calculate the circumference of rectangle")
print("6. Calculate the area of rectangle")
print("7. Calculate the circumference of Triangle")
print("8. Calculate the area of Triangle")
print("0. Exit")
print("".center(40, '-'))

while True:
    choice = int(input("\nEnter your choice: "))

    if choice in [1, 2]:
        square(choice)
        print()
    elif choice in [3, 4]:
        circle(choice)
        print()
    elif choice in [5, 6]:
        rectangle(choice)
        print()
    elif choice in [7, 8]:
        triangle(choice)
        print()
    elif choice == 0:
        print("Session over.")
        break
    else:
        print("Invalid choice!\n")