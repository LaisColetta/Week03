#Modify the program in 6 (randomFruit2.py) so that it uses a tuple ( ) not a list [ ]. 
#Author: Lais

import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
index = random.randint (0, len(fruits)-1)

fruit = fruits [index]
print ("A random fruit: {} ".format(fruit))
