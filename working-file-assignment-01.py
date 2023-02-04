
"""

Create a list of 20 random elements, with values ranging from 1 to 100. Store all the 
multiples of 2, all the multiples of 3 and all the multiples of 6 in separate lists. If a 
number is a multiple of 6, it shouldn’t appear in the multiples of 2 or multiples of 3 lists. 
Print out all three multiples lists, as well as the list of remaining elements, that are not a 
multiple of any of the three. Output the results in ascending order. Feel free to use the 
inbuilt sorting functions


response from chat-gpt

"""

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



# my attempt at this assignment

# generate a list of 20 random numbers between 1 and 100

listOfRandomNumbers=[] # empty list
duplicates = [] # empty list

for i in range(20):
	listOfRandomNumbers.append(random.randint(1, 100))
	
print(r'[IS 415 only]')

# print(f"list of random Numbers:{listOfRandomNumbers}")

listOfRandomNumbers = random_numbers

#multiples
remainingNumbers = []
for i in [-1,2,3,6]:
        m = [] # empty list, m stands for multiples
        for j in range(20):
                #using the iterator for assignments in list variables
                if listOfRandomNumbers[j] % i == 0:
                        if i != 6:
                                if listOfRandomNumbers[j] % 6 !=0:
                                        m.append(listOfRandomNumbers[j])
                        elif i == 6:
                                if listOfRandomNumbers[j] % 6 ==0:
                                        m.append(listOfRandomNumbers[j])
                        if i == -1:
                                if  listOfRandomNumbers[j] % 2 !=0 \
                                        and listOfRandomNumbers[j] % 3 !=0 \
                                        and listOfRandomNumbers[j] % 6 !=0:
                                        remainingNumbers.append(listOfRandomNumbers[j])
                        

        m.sort()
        if i != -1:
                print(f"Muliples of {i}: {m}")

remainingNumbers.sort()
print(f"Remaining number list:{remainingNumbers}")
print(f"List of duplicates that where selected: {duplicates}")


print(r'[IS 615 only]')

import random

# generate a list of 20 unique random numbers between 1 and 100
random_numbers = list(set([random.randint(1, 100) for i in range(20)]))

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
