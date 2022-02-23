#Program that prints out a random fruit
#Author: Lais

import random
fruits = ['apple', 'banana', 'cherry']
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit:{} ".format(fruit))