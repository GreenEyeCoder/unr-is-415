
"""

Create a list of 20 random elements, with values ranging from 1 to 100. Store all the 
multiples of 2, all the multiples of 3 and all the multiples of 6 in separate lists. If a 
number is a multiple of 6, it shouldn’t appear in the multiples of 2 or multiples of 3 lists. 
Print out all three multiples lists, as well as the list of remaining elements, that are not a 
multiple of any of the three. Output the results in ascending order. Feel free to use the 
inbuilt sorting functions

Joel DeRouchey Assignment #1 
IS 415 UNR
Feburary 7, 2023

"""

print(r"My attempt")

from random import randint


#Generate list of 20 random variables
my_loop = 20
rv = [] # empty list rv stands for random variables
for i in range(my_loop):
        ranNum = randint(1,100)
        rv.append(ranNum)

#multiples
reminders = [] # empty list

for i in [-1,2,3,6]:
        m = [] # empty list, m stands for multiples
        for j in range(my_loop):
                if  i == -1:
                    if  rv[j] % 2 != 0 \
                    and rv[j] % 3 != 0 \
                    and rv[j] % 6 != 0:
                        reminders.append(rv[j])
                if rv[j] % i == 0:
                        if i != 6:
                                if rv[j] % 6 !=0:
                                        m.append(rv[j])
                        else:
                                m.append(rv[j])
        m.sort()
        if i != -1:
            print(f"Muliples of {i}",m)

reminders.sort()
print(f"Remainders: {reminders}")





        
