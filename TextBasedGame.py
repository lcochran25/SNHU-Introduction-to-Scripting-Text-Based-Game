#Lukas Cochran


#Intro and instructions for gameplay
def instructions():
    print('Welcome to the Zombie Laboratory Game!')
    print('-' * 38)
    print('Game Play Instructions:')
    print('1. Moving commands: go North, go South, go East, go West')
    print('2. Collect 6 items before encountering the Zombie to win the game.')
    print('3. If all 6 items are not collected you will be bitten by the Zombie and turn!')
    print("4. To add items to inventory - Enter: get 'item name'")
    print('-' * 75)
instructions()


#Dictionary room set up for navigating game and item organization
rooms = {
        'Main Laboratory Room': {'South': 'Weapons Room', 'North': 'Medicine Room', 'West': 'Entry Port Room', 'East':'Files Room','item':'No Items'},
        'Entry Port Room': {'East': 'Main Laboratory Room', 'item':'Hazmat Suit'},
        'Supplies Room': {'East': 'Weapons Room','item':'Arm Padding'},
        'Weapons Room': {'North':'Main Laboratory Room','West':'Supplies Room','item':'Rifle'},
        'Medicine Room': {'South':'Main Laboratory Room','East':'Top Secret Lab Room','item':'Antidote Pill'},
        'Files Room': {'West':'Main Laboratory Room','North':'Break Room','item':'Lab Report'},
        'Break Room': {'South':'Files Room','item':'Red Bull'},
        'Top Secret Lab Room': {'West':'Medicine Room','item':'Zombie!!!'} #villian room

        }


#movements between all the rooms with conditional statement for wrong way / no room in direction entered
def movements(player, direction):
    while True:
        global rooms
        current_room = player
        if direction in rooms[current_room]:
            return rooms[current_room][direction]
        if direction not in rooms[current_room]:
            print('---WRONG WAY / NO ROOM ACCESS!---')  #output statement when no room in direction
            return player


#Displaying items in each room and collecting items to inventory
def items(player, item):
    while True:
        global rooms
        current_room = player
        if item in rooms[current_room]:
            return rooms[current_room][item]


#Game play loop function that calls other functions for moving between rooms and collecting items
def main_game_play():
    player = 'Main Laboratory Room'
    inventory = []
    item_count = 6


    while True:
        starting_room = player

        print(f'You are in the {starting_room}')
        print('Current Inventory:', inventory)
        print('You see', items(player, 'item'))
        print('-' * 45)
        print('Enter Play Command or Enter Exit to Quit Game')
        print('-' * 45)


        commands = input('Enter command:')   #player input commands

        action = commands.split()    #player command processing for moving and collecting items to inventory
        if action[0] == 'go':
            player = movements(player, action[1])
        elif action[0] == 'get':
            inventory.append(items(player, 'item'))
        elif action[0] == 'Exit':     #Exit option if player wants to quit - ends loop
            print('Game over. Thank you for playing!')
            break

        else:
            if action[0] != 'get' or 'go' or 'Exit':    #invalid player input conditional
                print('-----INVALID MOVE---TRY AGAIN-----')

        if len(inventory) == item_count:   #game output if player collects items and wins game - ends loop
            print('YOU COLLECTED ALL 6 ITEMS AND DEFEATED THE ZOMBIE!\n'
                  'YOU WIN!\n')
            break

        if player == 'Top Secret Lab Room' and len(inventory) < item_count:    #game output if player does not collect items and loses - ends loop
            print('You have entered the Top Secret Lab Room and see the Zombie!\n'
                  'You are not prepared with the items needed and the Zombie has bitten you!\n'
                  'You have lost!----Thanks for playing.\n')
            break


main_game_play()




