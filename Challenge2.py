#Assignment:Write a program that
#declares several variables with different data types
#print the type of data they are Ex: int, float, boolean, string
#calculate the addition, subtraction, multiplication, and division of  two variables of the same type and print the result 
#Calculate the modulus of two of the variables, and tell me what it means.
import os

os.system('cls')

var1 = (input("give me an integer"))

try:
    var1=int(var1)
    print(type(var1))
    check=True
except ValueError:
    check=False
    print("That is not an integer")


var2 = (input("give me a float"))
try:
    var2=float(var2)
    print(type(var2))
    check=True
except ValueError:
    check=False
    print('That is not a float')

var3 = (input("give me a string"))
try:
    var3=str(var3)
    print(type(var3))
    check=True
except ValueError:
    check=False
    print('That is not a string')


var4=input("Give me an integer. This will be variable 4")

var5=input("Give me another integer. This will be variable 5.")

print("This is variable 4 plus variable 5")
a= (var4+var5)
print(a)
print("This is variable 4 minus variable 5")
b= (var4-var5)
print(b)
print("This is variable 4 multiplied by variable 5")
c= (var4*var5)
print(c)
print("This is variable 4 divided by variable 5")
d= (var4/var5)
print(d)
print("This is the modulus of variable 4")
e= (var4%2)
print(e)
print("This is the modulus of variable 5")
f= (var5%2)
print(f)