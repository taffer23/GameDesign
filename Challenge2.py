#Assignment:Write a program that
#declares several variables with different data types
#print the type of data they are Ex: int, float, boolean, string
#calculate the addition, subtraction, multiplication, and division of  two variables of the same type and print the result 
#Calculate the modulus of two of the variables, and tell me what it means.
import os

os.system('cls')

print("Variable 1 is 17. This is the data type of variable 1")
var1= 17
print(type(var1))

print("Variable 2 is 1.5. This is the data type of variable 2")
var2=1.5
print(type(var2))

print("Variable 3 is sentence: This is a string. This is the data type of variable 3")
var3=("this is a string")
print(type(var3))

var4=input("Give me variable 4")

var5=input("Give me variable 5")

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