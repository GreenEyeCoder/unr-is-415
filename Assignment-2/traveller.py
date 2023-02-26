'''Uses with Linux systems'''
'''Assignment #2'''
#!/usr/bin/env python

import random
import csv

'''Example Game variable'''

# exampleGame = [1,1,5,6,3,2,1,5,1,4,'p',6,6,5,5,3,6,1,6]



'''Files needed for game'''
ROAD_FILE = 'road.csv'
HEALTH_FILE = 'health.csv'

'''Actual Road'''
road = ['X','|','|','|','|','|','|','|','|','|']


def print_roadMap(road):
    '''Print road map'''

    for i in range(len(road)):
        print(road[i], end=" ")
    print()

with open(ROAD_FILE, 'w', encoding='UTF8', newline='') as f:
    '''New Game Road Record'''

    writer = csv.writer(f)
    writer.writerow(road)

with open(HEALTH_FILE,'w',encoding='UTF8',newline='') as f:
    '''New Game Health Status'''
    health = [100]
    writer = csv.writer(f)
    writer.writerow(health)

def read_road():
    '''Read file to determine game status'''

    with open(ROAD_FILE, 'r') as file:
        reader = csv.reader(file)
        return next(reader)

def write_road(road):
    '''Record Road map'''

    with open(ROAD_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(road)

def read_health():
    '''Determine health'''

    with open(HEALTH_FILE, 'r') as file:
        return int(file.read())

def write_health(health):
    '''Write to disk on Health status'''

    with open(HEALTH_FILE, 'w') as file:
        file.write(str(health))

def print_status(damage, health, steps):
    '''Status Update'''

    if damage == -10 or damage == -40:
        print(f'You took {abs(damage)} damage')
    elif steps == 1:
        print('You moved forwad')
    elif steps == -1:
        print('You moved back')
    print(f'Your current health is: {health}')


def rollDice():
    '''random stuff happening here'''    
    
    outcome = random.randint(1, 6)

    steps = 0 
    damage = 0
    d10 = None
    if outcome == 1:
        damage = -10
    elif outcome == 2:
        steps = -1
    elif outcome == 3:
        d10 = random.randint(1, 10)
        if d10 == 7:
            steps = 10
    elif outcome == 4:
        damage= -40
    elif outcome == 5:
        print("Do nothing")
    elif outcome == 6:
        steps = 1

    return ((steps,damage,outcome,d10))



def consumePotion(health):
    '''Stay in the game longer'''

    health = min(health + 70, 100)
    return health

def movePlayer(position, steps):
    '''Determine where on the board you are'''

    newPos = position + steps
    if newPos < 1:
        newPos = 1
    elif newPos > 10:
        newPos = 10
    return newPos

def playGame():
    '''Try to recreate the example'''

    print("Enter 'r' to roll the dice, 'p' to consume potion, or 'q' to quit: ")
    user_input = None # initizing variable in local function scope
    exampleGameIndex = 0
    road = read_road()
    position = 1
    health = read_health()
    tenSidedDice = None
    print(f'Your current health is: {health}')
    print_roadMap(road)
    journeyMessage = 'Your journey begins. You are\n' + \
                     'only at the first position.'
    print(journeyMessage)
    print('\n')
    travelerWillDoWhat = 'What will you do, traveller?'
    
    while position < 10:
        print(travelerWillDoWhat)
        user_input = input()
        if user_input == 'q':
            break
        elif user_input == 'p':
            if health == 100:
                print("You are already at full health.")
            else:
                health = consumePotion(health)
                write_health(health)
                print(f"You consume a potion\nYour health to {health}.")
                print_roadMap(road)
                print('\n'*2)
        elif user_input == 'r':
            steps, damage, outcome, tenSidedDice = rollDice()
            print(f'You rolled a {outcome}')
            if outcome == 3 and tenSidedDice != 7:
                print('Nobody heard your prayers')
            health += damage
            position = movePlayer(position, steps)
            for i in range(len(road)):
                if i+1 == position:
                    road[i] = 'X'
                else:
                    road[i] = '|'
            if health <= 0:
                print("You died. Game over.")
                break

            if position == 10:
                print("Congratulations, you made it to the end of the path!")
                
            write_road(road)
            print_status(damage, health, steps)
            print_roadMap(road)
            print('\n'*2)

'''Do you want to play a game? (In creepy computer generated voice)'''          
playGame()

