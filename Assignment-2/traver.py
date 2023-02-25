'''Uses with Linux systems'''
'''Assignment #2'''
#!/usr/bin/env python

import random
import csv

'''Files needed for game'''
ROAD_FILE = 'road.csv'
HEALTH_FILE = 'health.csv'

'''Actual Road'''
road = ['X','|','|','|','|','|','|','|','|','|']


def print_roadMap(road):
    '''Print road map'''

    for i in range(len(road)):
        print(road[i],end=" ")

with open(ROAD_FILE, 'w', encoding='UTF8', newline='') as f:
    '''New Game Road Record'''

    writer = csv.writer(f)
    writer.writerow(road)

with open(HEALTH_FILE,'w',encoding='UTF8',newline='') as f:
    '''New Game Health Status'''

    writer = csv.writer(f)
    writer.writerow(100)

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

def print_status(position, health):
    '''Status Update'''

    print(f"Current position: {position}, Health: {health}")

def roll_dice():
    '''Roll the dices D6 & D10'''

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

def consume_potion(health):
    '''Stay in the game longer'''

    health = min(health + 70, 100)
    return health

def move_player(position, steps):
    '''Determine where on the board you are'''

    new_pos = position + steps
    if new_pos < 1:
        new_pos = 1
    elif new_pos > 10:
        new_pos = 10
    return new_pos

def menu(item):
    '''Actions to take on dice roll'''

    item -= 1
    menu = []
    menu.append('1. Take 10 damage')
    menu.append('2. Take a step backwards')
    menu.append('3. Pray for salvation and roll a d10 to be saved. If the roll is equal to 7, send the player to the end of the path. Otherwise do nothing. ')
    menu.append('4. Take 40 damage')
    menu.append('5. Do nothing.')
    menu.append('6. Take a step forward')
    return(menu[item])

def play_game():
    '''Starting the game program'''

    road = read_road()
    position = road.index('X') + 1
    health = read_health()
    tenSidedDice = None
    print('\n')
    print_roadMap(road)
    print('\n')
    print_status(position, health)

    while position < 10:
        print('\n')
        user_input = input("Enter 'r' to roll the dice, 'p' to consume potion, or 'q' to quit: ")
        if user_input == 'q':
            break
        elif user_input == 'p':
            if health == 100:
                print("You are already at full health.")
            else:
                health = consume_potion(health)
                write_health(health)
                print(f"You consume a potion and restore your health to {health}.")
        elif user_input == 'r':
            steps, damage, outcome, tenSidedDice = roll_dice()
            print(f'You rolled a {outcome}')
            print(f'{menu(outcome)}')
            if tenSidedDice != None:
                print(f'On a ten sided dice your rolled a {tenSidedDice}')
            health += damage
            position = move_player(position, steps)
            for i in range(len(road)):
                if i+1 == position:
                    road[i] = 'X'
                else:
                    road[i] = '|'
        


            write_road(road)
            print_status(position, health)
            print_roadMap(road)

            if health <= 0:
                print("You died. Game over.")
                break

    if position == 10:
        print("Congratulations, you made it to the end of the path!")

play_game()
