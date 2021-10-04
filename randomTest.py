#Ryan Taffe


import os, random
os.system('cls')
for i in range(10):
    randy = random.randint(3,5)
    print(randy)
    randy2= random.random()
    randy2 *=1000
    print(int(randy2))

fruits=["banana", "apple", "berries"]
print(fruits)
numbers=[1,2,3,6,5,7]
print(numbers)
#index = random.randint(0,2)
#print(fruits[index])
word= random.choice(fruits)
print(word)
num=random.choice(numbers)
print(num)

