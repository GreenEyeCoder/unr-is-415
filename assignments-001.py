
"""

Create a list of 20 random elements, with values ranging from 1 to 100. Store all the 
multiples of 2, all the multiples of 3 and all the multiples of 6 in separate lists. If a 
number is a multiple of 6, it shouldn’t appear in the multiples of 2 or multiples of 3 lists. 
Print out all three multiples lists, as well as the list of remaining elements, that are not a 
multiple of any of the three. Output the results in ascending order. Feel free to use the 
inbuilt sorting functions


response from chat-gpt


import random

# generate a list of 20 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for i in range(20)]

# separate multiples of 2, 3, and 6 into separate lists
multiples_2 = [num for num in random_numbers if num % 2 == 0 and num % 6 != 0]
multiples_3 = [num for num in random_numbers if num % 3 == 0 and num % 6 != 0]
multiples_6 = [num for num in random_numbers if num % 6 == 0]

# store the remaining elements that are not a multiple of any of the three
remaining = [num for num in random_numbers if num % 2 != 0 and num % 3 != 0 and num % 6 != 0]

# sort all the lists in ascending order
multiples_2.sort()
multiples_3.sort()
multiples_6.sort()
remaining.sort()

# print the lists
print("Multiples of 2:", multiples_2)
print("Multiples of 3:", multiples_3)
print("Multiples of 6:", multiples_6)
print("Remaining numbers:", remaining)

"""


# my attempt

from random import randint

my_loop = 20

for i in range(my_loop):
	ranNum = randint(1,100)
	print(ranNum)
