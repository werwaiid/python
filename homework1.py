#1
ans1 = input("Is it rainy outside?").lower()
if ans1 == "yes":
    ans2 = input("Is it windy outside?").lower()
    if ans2 == "yes":
        print("It's too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy yor day")

#2
name = input("Enter your name in lowercase").title()
surname = input("Enter your surname in lowercase").title()
print(name + " " + surname)

#3
stroka = input("Enter the 1st line of the poem")
print(len(stroka))
s1 = int(input("Enter the starting position"))
s2 = int(input("Enter the ending position"))
print(stroka[s1:s2])

#4
name = input("Enter your name")
if len(name) < 5:
    surname = input("Enter your surname")
    print (name.upper(), surname.upper())
else:
    print(name.lower())

#5
import math
chislo = int(input("Enter number greater than 500"))
print(round(math.sqrt(chislo), 2))

#6
import math
figura = input("Choose: circle, triangle or rectangle")
if figura == "circle":
    radius = float(input("Enter radius of the circle"))
    print("The area of the circle is equal to", math.pi*radius*radius)
if figura == "triangle":
    a = float(input("Enter first side of the triangle"))
    b = float(input("Enter second side of the triangle"))
    c = float(input("Enter third side of the triangle"))
    polyp = (a+b+c)/2
    print("The area of the triangle is equal to",math.sqrt(polyp*(polyp - a)*(polyp - b)*(polyp - c)))
if figura == "rectangle":
    a = float(input("Enter first side of the rectangle"))
    b = float(input("Enter seconf side of the rectangle"))
    print("The area of the circle is equal to",a*b)    
               
