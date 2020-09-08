#Author: Brandon Phillips, Julien Ouelette
#Date: 05/28/2018
#Name: wasteland_ca
#Description: Wasteland is an open-ended, text-based RPG set in the aftermath of a nuclear war.
import random
#VARIABLE DEFINITIONS=========================
user_input = '' #Initialize user input as blank string.
user_quit = False #Initialize as false. Variable checks if user decided to quit.
main = True #Activate main loop.
intro_check = False #Initialize as False. Used at the start.
location = 'Air Canada Centre' #Initialize starting location as ACC.
money = 0 #Initalize money variable
exp = 0

#Shop-----------------------------------------
armour_shop = [] #Create blank list for armour shop
armour_shop_items = [] #Create blank list for armour shop names
weapon_shop = [] #Create blank list for weapon shop
weapon_shop_items = [] #Create blank list for weapon shop names
food_shop = [] #Create blank list for food shop
food_shop_items = [] #Create blank list for food shop names

#Battle---------------------------------------
inv_food_names = [] #Create blank list for names of food in player inventory
inv_food_stats = [] #Create blank list for stats of food in player inventory
battle_options = ['Attack', 'Items', 'Flee', 'Quit'] #List of what player can do in battle

#Inventory------------------------------------
food_list = {'Cola': [0,0,0,0,2], #Health bonus is temporary, other stat bonuses are permanent; Food number = 0
        'Canned Soup': [0,0,0,0,10], #Food number = 1
        'Potato': [0,0,0,0,3], #Food number = 2
        'Coffee': [0,0,0,1,5], #Food number = 3
        'Cereal': [0,0,0,0,5], #Food number = 4
        'Radioactive Ice Cream': [0,1,1,1,-3], #Food number = 5
        'Macaroni': [0,0,0,0,15], #Food number = 6
        'Water': [0,0,0,0,20], #Food number = 7
        'Twinkies': [0,0,0,0,25], #Food number = 8
        'Honey': [0,0,0,0,30]} #Food number = 9

weapon_list = {'Stick': [0,1,0,1,0], #All bonuses are present for as long weapon remains equipped; Weapon number = 0
          'Rock' : [0,2,0,0,0], #Weapon number = 1
          'Crowbar': [0,5,0,0,0], #Weapon number = 2
          'Baseball Bat': [0,7,0,0,0], #Weapon number = 3
          'Machete': [0,10,0,0,0], #Weapon number = 4
          'Switchblade': [0,5,0,2,0], #Weapon number = 5
          'Pipe Wrench': [0,3,0,0,0], #Weapon number = 6
          'Sledgehammer': [0,13,0,-3,0], #Weapon number =7
          'Axe': [0,7,0,0,0]} #Weapon number #8

armour_list = {'Space Suit': [0,1,1,1,1], #All bonuses are present for as long weapon remains equipped; Armour number = 0
         'Raider Armour': [0,3,1,0,0], #Armour number = 1
         'Military Armour': [0,2,1,1,0], #Armour number = 2
         'Casual Outfit': [0,0,0,4,0], #Armour number = 3
         'Steel Armour': [0,0,4,0,0]} #Armour number = 4

armour = 'Empty' #Initialize as 'empty.'
items = [] #Initialize as empty string.
weapon = 'Empty' #Initialize as 'empty.'

inventory = {'Armour: ':armour, 'Weapon: ':weapon, 'Items: ':items} #Armour and Weapon has only 1 key and value, Items is a full dictionary of all items the user gains.
#---------------------------------------------

#Stats----------------------------------------
#NOTE: Base player stats will be something like [1, 3, 3, 2, 10]
player_stats = [0,0,0,0,0] #Initialize player stats as list of 0's.

#NOTE:
enemy_list = {'Giant Cockroach': [1, 1, 1, 3, 5], #Dicitionary contains all enemy names and stats together; Enemy number = 0
               'Raider': [1, 3, 2, 1, 7], #Enemy number = 1
               'Mutant Rat': [1, 3, 1, 3, 5], #Enemy number = 2
               'Zombie': [1, 2, 1, 1, 10], #Enemy number = 3
               'Rogue Pre-war Drone': [1, 5, 1, 2, 7], #Enemy number = 4
               'Radioactive Zombie': [1, 4, 1, 1, 12], #Enemy number = 5
               'Colossal Zombie': [1, 6, 2, 2, 15], #Enemy number = 6
               'Wild Dog': [1, 3, 1, 4, 5], #Enemy number = 7
               'Armored Raider': [1, 4, 5, 1, 10]} #Enemy number = 8

boss_stats = {'Raider Leader': [1,2,3,3,20], #Boss number = 0
              'Red Angels Leader': [1,3,2,1,25], #Boss number = 1
              'The Librarian': [1,5,4,4,50]} #Boss number = 2 (Final Boss)
#---------------------------------------------

#Search---------------------------------------
#REWARDS VARIABLES
acc_rewards = [] #Initialize rewards for Air Canada Centre as blank list.
market_rewards = [] #Initialize rewards for Supermarket as blank list.
crater_rewards = [] #Initialize rewards for Crater as blank list.
raider_rewards = [] #Initialize rewards for Raider Hideout as blank list.
station_rewards = [] #Initialize rewards for Union Station as blank list.
park_rewards = [] #Initialize rewards for Park as blank list.
hfcentre_rewards = [] #Initialize rewards for Harbourfront Centre as blank list.
restaurant_rewards = [] #Initialize rewards for Restaurant as blank list.
hotel_rewards = [] #Initialize rewards for Hotel as blank list.
cntower_rewards = [] #Initialize rewards for CN Tower as blank list.

#MESSAGE VARIABLES
message_1 = ('\"The monitors appear to be damaged beyond repair.\"') #For the monitors in ACC.
message_2 = ('\"There is a note on the desk. It has: \'GO TO THE STATION\' written on it.\"') #For the sleeping chamber in ACC.
message_3 = ('\"The sign has: \'2177 - The day the bombs fell and the world ended.\' printed on it.\"') #For the sign at the Crater.
message_4 = ('\"The monitors appear to still be functional. They display only one train operating. \'TRACK 227: ALEXANDRIA\'\"') #For the monitor at Union Station.
message_5 = ('\"It\'s clear that the hotel has already been ransacked. The only thing left is a cheap dollar store bell.\"') #For the front desk at Hotel.
message_6 = ('\"But nothing was there...\"') #Message will appear for all instances of where nothing is in the area being searched.
message_list = [message_1, message_2, message_3, message_4, message_5, message_6] #List contains all messages.
message_num = 0 #Initialize as 0.
#---------------------------------------------

#=============================================
#SHOP SYSTEM FUNCTIONS========================
def createArmourShop(armour_list): #Define creatArmourShop as a function
    armour_names = list(armour_list.keys()) #Create a list for the armour names
    armour_stats = list(armour_list.values()) #Creat list for armour stats
    for x_counter in range(3): #Loop for as many shop items
        armour_num = random.randint(0,4) #Get random armour
        armour_x = armour_names[armour_num] #Select random armour name
        armour_x_stats = armour_stats[armour_num] #Select random armour stats
        armour_x_add = armour_x + ', STATS: ' #Create shop display for random armour
        if armour_x_stats[1] != 0: #Check if armour has STR bonus and add to shop display
            armour_x_add += 'STR(' + str(armour_x_stats[1]) + ') '
        if armour_x_stats[2] != 0: #Check if armour has DEF bonus and add to shop display
            armour_x_add += 'DEF(' + str(armour_x_stats[2]) + ') '
        if armour_x_stats[3] != 0: #Check if armour has SPD bonus and add to shop display
            armour_x_add += 'SPD(' + str(armour_x_stats[3]) + ') '
        if armour_x_stats[4] != 0: #Check if armour has HP bonus and add to shop display
            armour_x_add += 'HP(' + str(armour_x_stats[4]) + ') '
        armour_x_add += '- $' + str(assignMoneyObject(armour_x, armour_names)) #Add value of random armour
        armour_shop.append(armour_x_add) #Add random armour to shop list
        armour_shop_items.append(armour_x)

def createWeaponShop(weapon_list): #Defining createWeaponShop as a function
     weapon_names = list(weapon_list.keys()) #Create list for weapon names
     weapon_stats = list(weapon_list.values()) #Create list for weapon stats
     for x_counter in range(3): #Loop for as many weapons are in shop
        weapon_num = random.randint(0,8) #Get random weapon
        weapon_x = weapon_names[weapon_num] #Select random weapon name
        weapon_x_stats = weapon_stats[weapon_num] #Select random weapon stats
        weapon_x_add = weapon_x + ' STATS: ' #Create shop display for random weapon
        if weapon_x_stats[1] != 0: #Check if weapon has STR bonus and add to shop display
            weapon_x_add += 'STR(' + str(weapon_x_stats[1]) + ') '
        if weapon_x_stats[2] != 0: #Check if weapon has DEF bonus and add to shop display
            weapon_x_add += 'DEF(' + str(weapon_x_stats[2]) + ') '
        if weapon_x_stats[3] != 0: #Check if weapon has SPD bonus and add to shop display
            weapon_x_add += 'SPD(' + str(weapon_x_stats[3]) + ') '
        if weapon_x_stats[4] != 0: #Check if weapon has HP bonus and add to shop display
            weapon_x_add += 'HP(' + str(weapon_x_stats[4]) + ') '
        weapon_x_add += '- $' + str(assignMoneyObject(weapon_x, weapon_names)) #Assign money value to random weapon
        weapon_shop.append(weapon_x_add) #Add random weapon to shop list
        weapon_shop_items.append(weapon_x)

def createFoodShop(food_list): #Defining createFoodShop as a function
    food_names = list(food_list.keys()) #Create list for food names
    food_stats = list(food_list.values()) #Create list for food stats
    for x_counter in range(5): #Loop for as many foods are in shop
        food_num = random.randint(0,9) #Get randmon food
        food_x = food_names[food_num] #Select random food name
        food_x_stats = food_stats[food_num] #Select random food stats
        food_x_add = food_x + ' STATS: ' #Create shop display for random food
        if food_x_stats[1] != 0: #Check if food has STR bonus and add to shop display
            food_x_add += 'STR(' + str(food_x_stats[1]) + ') '
        if food_x_stats[2] != 0: #Check if food has DEF bonus and add to shop display
            food_x_add += 'DEF(' + str(food_x_stats[2]) + ') '
        if food_x_stats[3] != 0: #Check if food has SPD bonus and add to shop display
            food_x_add += 'SPD(' + str(food_x_stats[3]) + ') '
        food_x_add += 'HP(' + str(food_x_stats[4]) + ') ' #Add health bonus to shop display
        food_x_add += ' - $' + str(assignMoneyObject(food_x, food_names)) #Add random food money value to shop display
        food_shop.append(food_x_add) #Add random food to shop list
        food_shop_items.append(food_x)

def assignMoneyObject(x_object, x_object_names): #Defining assignMoneyAmour as a fucntion
    if len(x_object_names) == 5: #Check shop type
        value = random.randint(45,70) #Assign random value to each item
    elif len(x_object_names) == 9:
        value = random.randint(20,70)
    elif len(x_object_names) == 10:
        value = random.randint(10,45)
    else:
        print('ERROR #1: Object list isn\'t found!') #Error statement
    return value #Return item price

def openShop(): #Defining openShop as a function
    ask_loop = True #Create variable as True
    print('Welcome to my shop! Would you like to buy something?') #Print statement
    while(ask_loop): #While variable is true run loop
        u_input = input('Your response (Yes/No): ') #Get user input
        if u_input.title() == 'Yes': #Check if user wants to enter shop
            print('Feel free to browse my shop!') #Print statement
            return True #Return True value
            ask_loop = False #End loop
        elif u_input.title() == 'No': #Check if user doesn't want to enter shop
            return False #Return False value
            ask_loop = False #End loop
        else: #Check if user didn't answer yes or no
            print('Please answer yes or no.') #Print statement

def purchaseShopItems(moneyx, location, items): #Defining purchaseShopItems as a function
    buy_loop = True #Set variable to True
    while(buy_loop): #While variable is true run shop
        print('You currently have $' + str(moneyx)) #Print players current money
        print('What would you like to buy?') #Print statement
        u_input = getShopInput() #Call getShopInput for user input
        if u_input.title() != 'Quit': #If user input isn't
            buy_loop, moneyx = checkUserBuy(u_input, location, moneyx, items) #Check if user can buy the item
        else: #Activate if user typed quit
            buy_loop = False #End shopping
        return u_input.title(), moneyx #Return user input and money

def getShopInput(): #Defining getShopInput as a function
    u_input = input('Your response (type \'Quit\' to exit): ') #Get user input
    return u_input.title() #Return user input

def checkUserBuy(u_inputx, x_location, moneyx, items): #Defining checkUserBuy as a function
    if x_location == 'CN Tower': #Check the location to decide on shop
        if checkItemBuy(u_inputx, armour_shop_items) and checkMoneyBuy(u_inputx, armour_shop_items, armour_shop, moneyx): #Only pass if the item is in the shop and user has enough money
            moneyx = subtractShopMoney(u_inputx, armour_shop_items, armour_shop, moneyx, armour_list, items) #Take money away from user
            return (False, moneyx) #Return False and money
        else: #If user didn't pass the checks
            return (True, moneyx) #Return True and money
    elif x_location == 'Crater':
        if checkItemBuy(u_inputx, weapon_shop_items) and checkMoneyBuy(u_inputx, weapon_shop_items, weapon_shop, moneyx):
            moneyx = subtractShopMoney(u_inputx, weapon_shop_items, weapon_shop, moneyx, weapon_list, items)
            return (False, moneyx)
        else:
            return (True, moneyx)
    elif x_location == 'Restaurant':
        if checkItemBuy(u_inputx, food_shop_items) and checkMoneyBuy(u_inputx, food_shop_items, food_shop, moneyx):
            moneyx = subtractShopMoney(u_inputx, food_shop_items, food_shop, moneyx, food_list, items)
            return (False, moneyx)
        else:
            return (True, moneyx)
    else: #Activate if user isn't in location with a shop
        print('ERROR #2: You\'re not in a location with a shop!') #Error statement
        return (True, moneyx)

def checkItemBuy(u_inputx, x_shop_names): #Defining checkItemBuy as a function
    if u_inputx in x_shop_names: #Check if item user wants is in the shop
        return True #Return True
    elif u_inputx.isdigit() and len(x_shop_names) >= int(u_inputx) > 0: #Check if user entered a shop number value
        return True #Return True
    else: #Activate if user didn't enter a shop item
        print('That item isn\'t in the shop!') #Print statement
        return False #Return False

def checkMoneyBuy(u_inputx, x_shop_names, x_shop, moneyx): #Defining checkMoneyBuy as a function
    if u_inputx.replace(' ','').isalpha(): #Check if user inputted the name of the item
        item_bought = x_shop_names.index(u_inputx) #Get shop display
        cost = x_shop[item_bought][-2:] #Get cost of the item
    elif u_inputx.isdigit(): #Check if user inputted number value of the item
        u_inputx = int(u_inputx) #Cast user input into an integer
        if x_shop[u_inputx -1] == 'Empty': #Check if shop slot is empty
            print('That item isn\'t in the shop!') #Print statement
            return False #Return False
        else: #Activate if shop slot isn't empty
            cost = x_shop[u_inputx -1][-2:] #Get cost of the item
    cost = int(cost) #Cast cost into an integer
    if moneyx > cost: #Check if user has enough money for item
        return True #Return True
    else: #If user doesn't have enough money
        print('You don\'t have enough money for that item!') #Print statement
        return False #Return False

def subtractShopMoney(u_inputx, x_shop_names, x_shop, moneyx, x_list, items): #Defining subtractShopMoney as a function
    x_list_names = list(x_list.keys()) #Create name list of every item name, shop specific
    if u_inputx.replace(' ','').isalpha(): #Check if user entered name of item
        item_bought = x_shop_names.index(u_inputx) #Get the index of the item bought
        cost = x_shop[item_bought][-2:] #Get the cost of the item
        x_num = x_list_names.index(u_inputx) #Get the index of the item on the all items name list
    elif u_inputx.isdigit(): #Check if user entered number value of item
        u_inputx = int(u_inputx) #Cast user input into an integer
        item_bought = u_inputx -1 #Get the index of the item bought
        cost = x_shop[item_bought][-2:] #Get the cost of the item
        item_bought_name = x_shop_names[item_bought] #Get the name of the item bought
        x_num = x_list_names.index(item_bought_name) #Get the index of the item on the all items name list
    addToInventory(x_list, x_num, items) #Add item bought to user inventory
    cost = int(cost) #Cast cost into an integer
    moneyx -= cost #Subtract money from the user
    x_shop[item_bought] = 'Empty' #Set shop item to empty
    return moneyx #Return money

def checkLeave(u_inputx): #Defining checkLeave as a function
    if u_inputx == 'Quit': #Check if user typed quit
        print('Have a nice day!') #Print statement
        return False #Return False
    else: #If user didn't type quit
        return True #Return True

def runShop(moneyx, type_shop, location, items): #Defining runShop as a function
    shop_loop = openShop() #Check if user wants to enter shop
    while(shop_loop): #While variable is True run shop
        displayChoiceList('shop', type_shop) #Display shop choices
        u_input, moneyx = purchaseShopItems(moneyx, location, items) #Purchase item user wants
        shop_loop = checkLeave(u_input) #Check if user wants to leave the shop
    return moneyx, type_shop #Return money
#=============================================
#BATTLE SYSTEM FUNCTIONS======================
def displayLifeBar(health_stat,current_health_stat): #Function displays health and visualizes it as health bar.
    x_current_health_stat = (current_health_stat / health_stat) * 10 #Put into percentage.
    x_current_health_stat = int(x_current_health_stat) #Remove decimal(s).
    x_health_stat = 10 #Set total health out of 10.
    print('==CURRENT HEALTH==') #Title bar.
    print('[',end='') #Health bar opening bracket.
    for x_counter in range(x_health_stat): #Loop for as many times as total health.
        if x_current_health_stat >= x_counter +1: #Check if current health exceeds the current counter value.
            print('|',end='') #Print '|', which represents a 'health point'.
        else: #Activate if all other conditions fail; Assume that this means current health is lower than total.
            print(' ',end='') #Print blank string in health bar.
    print(']') #Health bar closing bracket.
    print('Current health: ' + str(current_health_stat) + ' Maximum health: ' + str(health_stat)) #Display remaining health in numeric form.
    print('='*18) #End title bar.

def getUserMove(): #Defining getUserMove as a function
    input_loop = True #Set variable to True
    while(input_loop): #While variable is True run input loop
        print ('What would you like to do?') #Print statement
        u_input = input('Your response: ') #Get user input
        input_loop = checkUserMove(u_input, battle_options) #Check if user input was valid
    return u_input #Return user input

def checkUserMove(u_inputx, player_optionsx): #Defining checkUserMove as a function
    if u_inputx.title() in player_optionsx: #Check if user enter name of move
        return False #Return False
    elif u_inputx == '1' or u_inputx == '2' or u_inputx == '3' or u_inputx == '4': #Check if user enter number of move
        return False #Return False
    else: #If user didn't enter a valid move
        print('Please choose one of the avliable options.') #Print statement
        return True #Return True

def runUserMove(u_inputx, player_statsx, current_healthx, enemy_stats, moneyx, x_exp): #Defining runUserMove as a function
    if u_inputx.title() == 'Attack' or u_inputx == '1': #Check if user wants to attack
        if checkSpeed(player_stats, enemy_stats): #Check if user is faster than enemy
            attackEnemy(player_stats, enemy_stats) #Attack the enemy
            if checkEnemyHealth(enemy_stats): #Check if enemy is dead
                x_exp = gainXP(x_exp) #Gain random amount of xp
                moneyx = gainMoney(moneyx) #Gain random amount of money
                return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
            else: #If enemy isn't dead
                print('', end='') #Skip line
            current_healthx = attackPlayer(player_stats, enemy_stats, current_healthx) #Attack player
            if checkPlayerHealth(current_healthx): #Check if player is dead
                print('You have died!') #Print statement
                print('Game Over!') #Print statement
                return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
            else: #If player isn't dead
                return (True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
        else: #If enemy is faster than player
            current_healthx = attackPlayer(player_stats, enemy_stats, current_healthx) #Attack player
            if checkPlayerHealth(current_healthx): #Check if player is dead
                print('You have died!') #Print statement
                print('Game Over!') #Print statement
                return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
            else: #If player isn't dead
                print('', end='') #Skip line
            attackEnemy(player_stats, enemy_stats) #Attack enemy
            if checkEnemyHealth(enemy_stats): #Check is enemy is dead
                x_exp = gainXP(x_exp) #Gain random amount of xp
                moneyx = gainMoney(moneyx) #Gain random amount of money
                return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
            else: #If enemy isn't dead
                return(True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
    elif u_inputx.title() == 'Items' or u_inputx == '2': #Check if user wants to use their items
        if showFoodInventory(items): #Shop the user's avalible foods
            user_input = getUserChoice() #Get the food the user wants to use
            if user_input != 'Back': #Check if user wants to go back the the menu
                player_statsx, current_healthx = useFood(user_input, inv_food_names, inv_food_stats, player_statsx, current_healthx) #Use the food chosen
                current_healthx = attackPlayer(player_stats, enemy_stats, current_healthx) #Attack player
                if checkPlayerHealth(current_healthx): #Check if player is dead
                    print('You have died!') #Print statement
                    print('Game Over!') #Print statement
                    return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
                else: #If player isn't dead
                    return (True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
            else: #If user wants to go back to menu
                return (True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
        else: #If the user doesn't have any foods to use
            return(True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
    elif u_inputx.title() == 'Flee' or u_inputx == '3': #Check if user wants to Flee
        if checkFlee(player_stats, enemy_stats): #Check if player managed to run away
            return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
        else: #If player didn't managed to run away
            current_healthx = attackPlayer(player_stats, enemy_stats, current_healthx) #Attack player
            if checkPlayerHealth(current_healthx): #Check if player has died
                print('You have died!') #Print statement
                print('Game Over!') #Print statement
                return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
            else: #If player hasn't died
                return (True, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return True, player stats and player current health
    elif u_inputx.title() == 'Quit' or u_inputx == '4': #Check if user wants to quit
        return (False, player_statsx, current_healthx, u_inputx, moneyx, x_exp) #Return False, player stats and player current health
    else: #Activate only if user's inptu was invalid
        print('ERROR #1 (Battle System): Your input was invaild') #Error statement
        return (True, player_statsx, current_healthx, u_inputx, moneyx, x_exp)

def showFoodInventory(itemsx): #Defining showFoodInventory as a function
    print('Items: ') #Print statement
    food = [] #Create blank list for user avaliable foods
    checkFood(food_list, items, food, inv_food_names, inv_food_stats) #Check for user foods
    if food == []: #Check if user has no avaliable foods
        print('You have no items to use!') #Print statement
        return False #Return False
    else: #If user does have food
        for counter in range(len(food)): #Run loop for as many foods as user has
            print('-' + str(counter +1) + '-' + food[counter]) #Print all user foods
        return True #Return True

def checkFood(food_listx, itemsx, foodx, inv_food_namesx, inv_food_statsx): #Defining checkFood as a function
    food_names = list(food_listx.keys()) #POSSIBLY REMOVE
    food_stats = list(food_listx.values()) #POSSIBLY REMOVE
    inv_food_statsx.clear() #Clear list of user's food stats
    inv_food_namesx.clear() #Clear list of user's food names
    for counter in range(len(items)): #Loop for as many items are in user's inventory
        if items[counter] in food_names: #Check if the item in user inventory is a food
            food_number = food_names.index(items[counter]) #Get the index of the food from the list of all foods
            specfood_name = food_names[food_number] #Get the name of the food in the inventory
            inv_food_namesx.append(specfood_name) #Add name of food to the inventory list of foods
            specfood_stats = food_stats[food_number] #Get the stats of the food in the inventory
            inv_food_statsx.append(specfood_stats) #Add the stats of the food to the inventory list of foods
            specfood = specfood_name + ', STATS: ' #Create display for specific food
            if specfood_stats[1] != 0: #Check if food has a strength bonus
                specfood += ' STR(' + str(specfood_stats[1]) + ') ' #Add strength bonus to display
            if specfood_stats[2] != 0: #Check if food has a defence bonus
                specfood += 'DEF(' + str(specfood_stats[2]) + ') ' #Add defence bonus to display
            if specfood_stats[3] != 0: #Check if food has a speed bonus
                specfood += 'SPD(' + str(specfood_stats[3]) + ') ' #Add speed bonus to display
            specfood += 'HP(' + str(specfood_stats[4]) + ') ' #Add health bonus to display
            foodx.append(specfood) #Add specific food to display of inventory foods
    return foodx #Return food list

def getUserChoice(): #Defining getUserChoice as a function
    loop_input = True #Set variable to True
    while(loop_input): #Loop for user input while variable is True
        print('What would you like to use?') #Print statement
        user_input = input('Your response (type \'back\' to return to menu): ') #Get user input
        loop_input = checkUserInput(user_input, inv_food_names) #Check if user input is valid
    return user_input.title() #Return user input

def checkUserInput(user_inputx, inv_food_namesx): #Defining checkUserInput as a function                                                                                                                                                                                                                                                                 
    if user_inputx.title() in inv_food_namesx: #Check if user inputted a name of a food in their inventory
        return False #Return False
    elif user_inputx.isdigit() and len(inv_food_namesx) >= int(user_inputx) > 0: #Check if user inputted a number value of a food in their inventory
        return False #Return False
    elif user_inputx.title() == 'Back': #Check if user wants to go back to menu
        return False #Return False
    else: #If user input isn't valid
        print('That item isn\'t in your inventory.') #Print statement
        return True #Return True

def useFood(user_inputx, inv_food_namesx, inv_food_statsx, player_statsx, current_healthx): #Defining useFood as a function
    if user_inputx.replace(' ','').isalpha(): #Check if user inputted a food name
        x_food_num = inv_food_namesx.index(user_inputx) #Get the index of the food in their inventory
        x_food_stats = inv_food_statsx[x_food_num] #Get the food stats
        x_food_name = inv_food_namesx[x_food_num] #Get the food name
    elif user_inputx.isdigit(): #Check if user inputted a number of a food
        x_food_stats = inv_food_statsx[int(user_inputx) -1] #Get the food stats
        x_food_name = inv_food_namesx[int(user_inputx) -1] #Get the food name
    print('You use the ' + x_food_name + '!') #Print what food the user used
    player_stats[1] += x_food_stats[1] #Add the strength bonus
    player_stats[2] += x_food_stats[2] #Add the defence bonus
    player_stats[3] += x_food_stats[3] #Add the speed bonus
    current_healthx += x_food_stats[4] #Add the health bonus
    current_healthx = checkCurrentHealth(player_stats, current_healthx) #Check if current health is greater than max health
    displayLifeBar(player_statsx[4], current_healthx) #Display user health
    removeFood(food_list, x_food_name) #Remove the food used from the user inventory
    return player_statsx, current_healthx #Return player stats and current health

def removeFood(food_listx, x_food_name): #Defining removeFood as a function
    food_names_list = list(food_listx.keys()) #Create a list for all the food names
    food_num = food_names_list.index(x_food_name) #Get the index of the food used from the list of all foods
    removeFromInventory(food_listx, food_num, items) #Remove the food used from user inventory

def checkSpeed(player_statsx, enemy_statsx): #Defining checkSpeed as a function
    if player_stats[3] > enemy_statsx[3]: #Check if player is faster
        print('You\'re quick movements allow you to attack first!') #Print statement
        return True #Return True
    elif enemy_statsx[3] > player_stats[3]: #Check if enemy is faster
        print('The enemy\'s quick movements allow them to attack first!') #Print statement
        return False #Return False
    else: #If player speed and enemy speed is the same
        first_attack = random.randint(1,2) #Randomize who attacks first
        if first_attack == 1: #If player attacks first
            print('You\'re quick movements allow you to attack first!') #Print statement
            return True #Return True
        else: #If enemy attacks first
            print('The enemy\'s quick movements allow them to attack first!') #Print statement
            return False #Return False
    
def attackEnemy(player_statsx, enemy_statsx): #Defining attackEnemy as a function
    player_dmg = player_stats[1] - enemy_statsx[2] #Set player damage
    player_dmg = checkPlayerDmg(player_dmg) #Check if player damage is negative
    if checkCrit(): #Check if hit was critical
        player_dmg *= 3 #If cirtical multiply damage by 3
    else: #If not critical
        print('', end='') #Skip line
    enemy_statsx[4] -= player_dmg #Remove enemy health
    if enemy_statsx[4] <= 0: #Check if enemy has died
        enemy_statsx[4] = 0 #If enemy has died set enemy health to 0
    print('You attacked the enemy for ' + str(player_dmg) + ' damage!') #Print player damage on enemy
    print('The enemy now has ' + str(enemy_statsx[4]) + ' health left!') #Print enemy health left

def checkPlayerDmg(player_dmgx): #Defining checkPlayerDmg as a fucntion
    if player_dmgx <= 0: #If player damage is 0 or negative
        return 1 #Set player damage to 1
    else: #If player damage isn't 0 or negative
        return player_dmgx #Return player damage

def checkEnemyHealth(enemy_statsx): #Defining checkEnemyHealth as a function 
    if enemy_statsx[4] <= 0: #Check if enemy has died
        print('The enemy has died!') #Print statement
        print('You won the battle!') #Print statement
        return True #Return True
    else: #If enemy hasn't died
        return False #Return False

def attackPlayer(player_statsx, enemy_statsx, current_healthx): #Defining attackPlayer as a function
    enemy_dmg = enemy_statsx[1] - player_stats[2] #Set enemy damage
    enemy_dmg = checkEnemyDmg(enemy_dmg) #Check if enemy damage is 0 or negative
    if checkCrit(): #Check if hit was critical
        enemy_dmg *= 3 #Multiple damage by 3
    else: #If not critical
        print('', end='') #Skip line
    current_healthx -= enemy_dmg #Remove player health
    if current_healthx <= 0: #Check if player has died
        current_healthx = 0 #Set player health to 0
    print('The enemy has attacked you for ' + str(enemy_dmg) + ' damage!') #Print enemy damage
    displayLifeBar(player_statsx[4], current_healthx) #Display player health
    return current_healthx #Return player current health

def checkEnemyDmg(enemy_dmgx): #Defining checkOppDmg as a function
    if enemy_dmgx <= 0: #Check if enemy damage is 0 or negative
        return 1 #Set enemy damage to 1
    else: #If enemy damage isn't 0 or negative
        return enemy_dmgx #Return enemy damage

def checkPlayerHealth(current_healthx): #Defining checkPlayerHealth as a function
    if current_healthx <= 0: #Check if player has died
        return True #Return True
    else: #If player hasn't died
        return False #Return False

def checkCrit(): #Defining checkCrit as a function
    crit_hit = random.randint(1,5) #Create a random number from 1 to 5
    if crit_hit == 1: #If random number was 1
        print('CRITICAL HIT!') #Print statement
        return True #Return True
    else:  #If random number wasn't 1
        return False #Return False

def checkCurrentHealth(player_statsx, current_healthx): #Defining checkCurrentHealth as a function
    if current_healthx > player_statsx[4]: #Check if current health is greater than max health
        current_healthx = player_statsx[4] #Set current health to max health
    else: #If current health is less than max health
        print('', end='') #Skip line
    return current_healthx #Return current health

def checkFlee(player_statsx, enemy_statsx): #Defining checkFlee as a function
    if player_statsx[3] > enemy_statsx[3]: #If player is faster than enemy
        print('You managed to run away!') #Print statement
        return True #Return True
    elif enemy_statsx[3] > player_statsx[3]: #If enemy is faster than player
        print('The enemy is too fast for you to run away!') #Print statement
        return False #Return False
    else: #If player and enemy are same speed
        run_away = random.randint(1,2) #Create random number from 1 to 2
        if run_away == 1: #If random number is 1
            print('The enemy almost caught up to you, but you managed to escape!') #Print statement
            return True #Return True
        else: #If random number is 2
            print('You almost escaped, but the enemy managed to catch you! Better luck next time!') #Print statement
            return False #Return False

def gainXP(x_exp): #Defining gainXP as a function
    x_exp_gained = random.randint(1,4) #Get a random amount of xp gained
    x_exp += x_exp_gained #Add xp gained to current xp
    print('You gained ' + str(x_exp_gained) + 'XP!') #Print statement
    return x_exp #Return exp

def gainMoney(moneyx): #Defining gainMoney as a function
    gained_money = random.randint(5,15) #Get amount of money found
    moneyx += gained_money #Add money to player money
    print('You found $' + str(gained_money) + '!') #Print statement
    return moneyx #Return money

def checkGameEnd(u_inputx, current_healthx): #Defining checkGameEnd as a function
    if u_inputx.isalpha() and u_inputx.title() == 'Quit': #Check if player quit
        return True #Return True
    elif u_inputx.isdigit() and u_inputx == '4': #Check if player quit
        return True #Return True
    elif checkPlayerHealth(current_healthx): #Check if player died
        return True #Return True
    else: #If player didn't die/quit
        return False #Return False

def getEnemy(player_stats, enemy_list): #Defining getEnemy as a function 
    enemy_names_list = list(enemy_list.keys()) #Get names of all enemies
    enemy_num = random.randint(0,8) #Get a random enemy
    enemy_name = enemy_names_list[enemy_num] #Get a random enemy name
    enemy_stats = scaleEnemyStats(player_stats, enemy_num) #Get the enemy stats
    return enemy_stats, enemy_name #Return enemy stats and name

def checkForBattle(): #Defining checkForBattle as a function
    check_battle = random.randint(1,3) #Randomize battle
    if check_battle == 1: #If there is a battle
        return True #Return True
    else: #If no battle
        return False #Return False

def runBattle(player_stats, current_health, user_quit, moneyx, x_exp): #Defining runBattle as a function
    if checkForBattle(): #Check if player gets a battle
        enemy_stats, enemy_name = getEnemy(player_stats, enemy_list) #Get the enemy stats and name
        print('A ' + enemy_name + ' has started to attack you!') #Print statement
        print('A battle has begun!') #Print statement
        loop_battle = True #Start battle
    else: #If player doesn't get in a battle
        loop_battle = False #Don't start battle
    while(loop_battle): #While variable is True run battle
        displayChoiceList('battle', battle_options) #Display choice for battle
        u_input = getUserMove() #Get the user move
        loop_battle, player_stats, current_health, u_input, moneyx, x_exp = runUserMove(u_input, player_stats, current_health, enemy_stats, moneyx, x_exp) #Run the user move
        if checkGameEnd(u_input, current_health): #Check if game should end
            user_quit = True #End game
        else: #If game shouldn't end
            user_quit = False #Don't end game
    return player_stats, current_health, user_quit, moneyx, x_exp #Return player stats and current health
#=============================================
#STATS FUNCTIONS==============================
#def setPlayerStats(player_stats): #Function sets/resets player stats. Use this each time a change is made to an individual stat.
    #player_stats = [level_stat, strength_stat, defence_stat, speed_stat, health_stat] #Define player stat as an array of variables.
    #return player_stats

def initializePlayerStats(player_stats): #Function sets all the player stats to the base stats.
    #NOTE: This should function should be called at the start.
    player_stats[0] = 1 #Set level as 1.
    player_stats[1] = 3 #Set strength as 3.
    player_stats[2] = 3 #Set defence as 3.
    player_stats[3] = 2 #Set speed as 2.
    player_stats[4] = 10 #Set health as 10.
    return player_stats

def displayStats(stats_list): #Function displays a list of stats in user-friendly way.
    print('==CURRENT STATS==') #Title bar.
    print('LEVEL: ' + str(stats_list[0])) #Display individual stat.
    print('STRENGTH: ' + str(stats_list[1])) 
    print('DEFENCE: ' + str(stats_list[2])) 
    print('SPEED: ' + str(stats_list[3])) 
    print('HEALTH: ' + str(stats_list[4]))
    print('=' * 17) #End title bar.

def levelPlayer(player_stats): #Function levels up player by increasing stat values.
    if (player_stats[0] + 1) <= 10: #Check if player level is less than 10. 10 is the level cap for our game.
        print('Level up!') #Level up message.
        player_stats[0] += 1 #Increase level by one.
        player_stats[4] += 2 #Increase health by two.
        for counter in range(1,4): #Loop 3 times; loop increases strength, defence, and speed using random values.
            bonus = random.randint(1,3) #Randomize a integer between 1 and 3.
            player_stats[counter] += bonus #Increase stat by bonus.
        displayStats(player_stats)
    else: #Activate if level isn't below 10
        player_stats = player_stats #Keep player stats the same.
    return player_stats

def subtractXP(x_exp, player_statsx): #Defining subtractXP as a function
    if player_statsx[0] <= 3: #Check player level and subtract xp based on their level
        x_exp -= 10
    elif player_statsx[0] <= 6:
        x_exp -= 15
    elif player_statsx[0] <= 10:
        x_exp -= 20
    else:
        print('ERROR - Shouldn\'t be subtracting exp') #Error statement
    return x_exp

def checkUserLevelUp(x_exp, player_statsx): #Defining checkPlayerLevelUp as a function
    if player_statsx[0] <= 3 and x_exp >= 10: #Check if player has enough exp to level up at certain levels
        return True
    elif player_statsx[0] <= 6 and x_exp >= 15:
        return True
    elif player_statsx[0] <= 10 and x_exp >= 20:
        return True
    else:
        return False

def scaleEnemyStats(player_stats, enemy_num): #Function adjust enemy stats according to players stats.
    enemy_stats = 0 #Initialize as 0.
    enemy_stats = getStatsList(enemy_list) #Set enemy stats as the keys of enemy_stats_dictionary.
    enemy_stats = enemy_stats[enemy_num] #Set enemy stats of individual stats basd on enemy number.
    for x_counter in range(len(enemy_stats)): #Loop for as many enemy stats (5).
        if player_stats[0] > 1 and player_stats[x_counter] > enemy_stats[x_counter]: #Checks if player level is above 1 and individual player stat is greater than individual enemy stat.
            scale_bonus = player_stats[x_counter] - enemy_stats[x_counter] #Set initial scale bonus as the difference between individual player stat and individual enemy stat.
            enemy_stats[x_counter] += scale_bonus #Add scale bonus to individual enemy stat.
        scale_bonus = random.randint(-2, 1) #Create the scale bonus using the range values.
        if enemy_stats[x_counter] + scale_bonus <= 0: #Check if the scale bonus will give a value of zero or less.
            scale_bonus = 0 #If true, default the scale bonus to 0.
        enemy_stats[x_counter] += scale_bonus #Add bonus to enemy stat.
    return enemy_stats
#=============================================

#INVENTORY FUNCTIONS==========================
def getNameList(object_list): #Fuction gets all dictionary keys (names are stored in the keys).
    if type(object_list) != list: #Check if object list type does not equal list.
        object_name = list(object_list.keys()) #Put all dictionary keys into separate list.
    else: #Activate if condition fails; assume object_name is already list.
        object_name = object_list #Keep object list the same.
    return object_name

def getStatsList(object_list): #Function gets all dictionary values (stats are stored in the values.
    object_stats = 0 #Initialize local variable as 0.
    if type(object_list) != list: #Check for list type.
        object_stats = list(object_list.values()) #Put all dictionary values into separate list.
    return object_stats

def getObjectNumberAndList(food_list, armour_list, weapon_list, user_input):
    food_list = list(food_list.keys()) #Get the keys of dictionary.
    if type(armour_list) == dict: #Check if variable is dictionary.
        armour_list = list(armour_list.keys()) #Get the keys of dictionary.
    if type(weapon_list) == dict: #Check if variable is dictionary.
        weapon_list = list(weapon_list.keys()) #Get the keys of dictionary.
    if user_input.title() in food_list: #Check if input is in specific list.
        object_list = food_list #Get list.
        object_num = food_list.index(user_input.title()) #Find index of input in that list, and put it in variable.
    elif user_input.title() in armour_list: #Check if input is in specific list.
        object_list = armour_list #Get list.
        object_num = armour_list.index(user_input.title()) #Find index of input in that list, and put it in variable.
    elif user_input.title() in weapon_list: #Check if input is in specific list.
        object_list = weapon_list #Get list.
        object_num = weapon_list.index(user_input.title()) #Find index of input in that list, and put it in variable.
    else: #Activate if other conditions fail; assume something went wrong.
        print('Error s-1 (getObjectNumber): Input does not exist in any of the lists!') #Error message.
    return object_num, object_list

def addToArmourValue(armour_num, items, player_stats): #Function adds armour to the armour key of the inventory dictionary.
    armour_name = getNameList(armour_list) #Get all armour dictionary keys in a list.
    armour_stats = getStatsList(armour_list) #Get all armour dictionary values in a list.

    current_armour_stats = (armour_stats[armour_num]) #Get the specific armour's (determined by armour number) stats and put in a list.
    strength_stat = str(current_armour_stats[1]) #Get strength stat from armour stats.
    defence_stat = str(current_armour_stats[2]) #Get defence stat from armour stats.
    speed_stat = str(current_armour_stats[3]) #Get speed stat from armour stats.
    health_stat = str(current_armour_stats[4]) #Get health stat from armour stats.
    
    armour = (armour_name[armour_num] + ', STATS: STR(' + strength_stat + ') DEF(' + defence_stat + ') SPD(' + speed_stat + ') HP(' + health_stat + ')') #Stat display message.
    for counter in range(1,5): #Loop for 4 times
        player_stats[counter] += current_armour_stats[counter] #Add armour stats to player stats
    return armour, player_stats #Return armour and play stats

def addToWeaponValue(weapon_num, player_stats): #Function adds weapon to the weapon key of the inventory dictionary.
    weapon_names = getNameList(weapon_list) #Get all weapon dictionary keys in a list.
    weapon_stats = getStatsList(weapon_list) #Get all weapon dictionary values in a list.
    
    current_weapon_stats = (weapon_stats[weapon_num]) #Get the specific weapon's (determined by weapon number) stats and put in a list.
    strength_stat = str(current_weapon_stats[1]) #Get strength stat from weapon stats.
    defence_stat = str(current_weapon_stats[2]) #Get defence stat from weapon stats.
    speed_stat = str(current_weapon_stats[3]) #Get speed stat from weapon stats.
    
    weapon = (weapon_names[weapon_num] + ', STATS: STR(' + strength_stat + ') DEF(' + defence_stat + ') SPD(' + speed_stat + ')') #Stat display message.
    for counter in range(1,5): #Loop 4 times
        player_stats[counter] += current_weapon_stats[counter] 
    return weapon, player_stats

def defaultObject(x_object, object_num, player_stats, x_list): #Function sets the string to 'Empty'.
    x_list_stats = getStatsList(x_list) #Get all weapon dictionary values in a list.
    current_object_stats = (x_list_stats[object_num]) #Get the specific weapon's (determined by weapon number) stats and put in a list.
    x_object = 'Empty' #Set object as empty. CHECK FOR ARMOUR OR WEAPON (ARMOUR: EMPTY/ WEAPON: EMPTY)
    for counter in range(1,5):
        player_stats[counter] -= current_object_stats[counter]
    return x_object, player_stats

def addToInventory(x_object_list, object_num, items): #Function adds object to items list. Object may be weapon, armour, food, or books.
    #NOTE: x_object_list parameter is the original dictionary the object originates from, object_num is the number associated with a particular object (i.e. weapon number), items is just items.
    object_name = getNameList(x_object_list) #Set object name as the entire name list.
    object_name = object_name[object_num] #Define which individual name to pull from.
    print('The ' + object_name + ' has been added to your inventory.') #Display message to signify addition.
    items.append(object_name) #Add object to inventory (items).

def removeFromInventory(x_object_list, object_num, items): #Function removes object from items list.
    object_name = getNameList(x_object_list) #Set object name as the entire name list.
    object_name = object_name[object_num] #Define which individual name to pull from.
    print('The ' + object_name + ' has been removed from your inventory.') #Display message to signify addition.
    items.remove(object_name) #Remove object from inventory (items).
    return items
    
def displayInventory(inventory,items): #Function displays inventory dictionary in user friendly form.
    inventory_items = getNameList(inventory) #Get all inventory dictionary keys in a list.
    inventory_stats = getStatsList(inventory) #Get all inventory dictionary values in a list.
    print('==INVENTORY==') #Title bar.
    for x_counter in range (3): #Loop for as many elements in dictionary.
        if x_counter == 2: #Check if counter has incremented twice; items element is next.
            print ('Items: ', end='') #Includes 'Items: ' in final message.
            if items == []: #Checks if inventory(items) is currently empty.
                print('Empty') #Display 'Empty' instead.
            else: #Activate if all other conditions fail.
                for i_counter in range (len(items)): #Loop for as many items in items list.
                    print(items[i_counter] + ', ', end= '') #Include individual item in final message.
                print('') #End print line.
        else: #Activate if all other conditions fail.
            print(inventory_items[x_counter], end='') #Display item.
            print(inventory_stats[x_counter])#Display item stats.
    print('=' * 13) #End title bar.

def resetInventory(inventory, armour, weapon, items): #Function defines the inventory dictionary
    #NOTE: Use this function everytime a change is made for a specific variable in the inventory
    inventory = {'Armour: ':armour, 'Weapon: ':weapon, 'Items: ':items} #Set/reset inventory dictionary.
    return inventory

def equiptWeapon(inventory, weapon_num, player_stats): #Function removes weapon from items list and adds to weapon value in dictionary.
    current_inventory = 0 #Initialize local variable
    print('Equipping weapon from inventory...') #Display action message.
    removeFromInventory(weapon_list, weapon_num, items) #Remove from items list.
    print('Equipped!') #Message signifying completion.
    weapon, player_stats = addToWeaponValue(weapon_num, player_stats) #Add weapon to weapon key in inventory dictionary.
    current_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory to adjust to changes.
    return weapon, current_inventory, player_stats

def equiptArmour(inventory, armour_num, player_stats): #Function removes armour from items list and adds to weapon value in dictionary.
    current_inventory = 0 #Initialize local variable.
    print('Equipping armour from inventory...') #Display action message.
    removeFromInventory(armour_list, armour_num, items) #Remove from items list.
    print('Equipped!') #Message signifying completion.
    armour, player_stats = addToArmourValue(armour_num, items, player_stats) #Add armour to armour key in inventory dictionary.
    current_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory to adjust to changes.
    return armour, current_inventory, player_stats

def unequiptWeapon(inventory,weapon_num, player_stats): #Function removes weapon from weapon value in dictionary ands puts in back in inventory.
    weapon = 0 #Initialize local variable.
    current_inventory = 0 #Initialize local variable.
    print('Unequipping weapon...') #Display action message.
    addToInventory(weapon_list, weapon_num, items) #Add weapon to items list.
    weapon, player_stats = defaultObject(weapon, weapon_num, player_stats, weapon_list) #Reset weapon key in dictionary.
    print ('Unequipping complete!') #Message signifying completion.
    current_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory to adjust to changes.
    return weapon, current_inventory, player_stats

def unequiptArmour(inventory,armour_num, player_stats): #Function removes armour from armour value in dictionary ands puts in back in inventory.
    armour = 0 #Initialize local variable.
    current_inventory = 0 #Initialize local variable.
    print('Unequipping armour...') #Display action message.
    addToInventory(armour_list, armour_num, items) #Add weapon to items list.
    armour, player_stats = defaultObject(armour, armour_num, player_stats, armour_list) #Reset weapon key in dictionary.
    print ('Unequipping complete!') #Message signifying completion.
    current_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory to adjust to changes.
    return armour, current_inventory, player_stats

def resetList(x_object_list, object_list): #Function checks if variable that is supposed to be dictionary is list, and converts it back to.
    if type(x_object_list) != dict: #Check if local list is type dictionary.
        if (x_object_list) != object_list: #Check if local list is type dicitonary AND not the same as original list.
            x_object_list = object_list #Set local list as original list.
        else: #Activate if condition fails. Assume the two lists equal to each other.
            x_object_list = x_object_list #Keep list the same.
    else: #Activate if condition fails. Assume x_object_list is already list type.
        x_object_list = x_object_list #Keep list the same.

def runInventoryLoop(user_input,inventory,food_list,armour_list,weapon_list,armour,weapon,items,player_stats): #Function includes entirety of inventory option.
    inventory_loop = True #Activate function loop.
    x_inventory = inventory #Set local variable.
    x_food_list = food_list #Set local variable.
    x_armour_list = armour_list #Set local variable.
    x_weapon_list = weapon_list #Set local variable.
    object_num = None #Initialize local variable.
    x_object_list = None #Initialize local variable.
    while(inventory_loop):
        displayStats(player_stats) #Display player stats.
        displayInventory(x_inventory,items) #Display inventory
        choices = ['Equipt/Unequipt','Trash','Return','Quit'] #Set choices.
        displayChoiceList('inventory',choices) #Display choices.
        user_input = getInput() #Get user input.
        if user_input.title() == choices[0] or user_input.isdigit() and (int(user_input) - 1) == 0: #Check if user chooses 'Equipt/Unequipt'.
            print('What would you like to equipt/unequipt? (alphabetic input only)')
            x_inventory = list(x_inventory.values()) #Get the values of dictionary.
            user_input = getInput() #Get user input.
            if user_input.title() != x_inventory[0] and x_inventory[0] == 'Empty' and user_input.title() in armour_list and user_input.title() in items: #Check if what user entered is not in the armour slot, is in the armour list and in items.
                armour_num, x_armour_list = getObjectNumberAndList(food_list,armour_list,weapon_list,user_input) #Get armour number and list.
                x_armour_list = resetList(x_armour_list, armour_list) #Reset armour list.
                armour, x_inventory, player_stats = equiptArmour(x_inventory, armour_num, player_stats) #equipt armour.
                x_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory.
            elif user_input.title() != x_inventory[1] and x_inventory[1] == 'Empty' and user_input.title() in weapon_list and user_input.title() in items: #Check if what user entered is not in the weapon slot, is in the weapon list and in items.
                weapon_num, x_weapon_list = getObjectNumberAndList(food_list,armour_list,weapon_list,user_input) #Get weapon number and list.
                x_weapon_list = resetList(x_weapon_list, weapon_list) #Reset weapon list.
                weapon, x_inventory, player_stats = equiptWeapon(x_inventory, weapon_num, player_stats) #equipt weapon.
                x_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory.
            elif user_input.title() in x_inventory[0] and user_input.title() in armour_list: #Check if what user entered is in the armour slot.
                armour_num, x_armour_list = getObjectNumberAndList(food_list, armour_list, weapon_list, user_input) #Get armour number and list.
                x_armour_list = resetList(x_armour_list, armour_list) #Reset armour list.
                armour, x_inventory, player_stats = unequiptArmour(x_inventory,armour_num,player_stats) #Unequipt armour.
                x_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory.
            elif user_input.title() in x_inventory[1] and user_input.title() in weapon_list: #Check if what user entered is in the weapons slot.
                weapon_num, x_weapon_list = getObjectNumberAndList(food_list, armour_list, weapon_list, user_input) #Get weapon number and list.
                x_weapon_list = resetList(x_weapon_list, weapon_list) #Reset weapon list.
                weapon, x_inventory, player_stats = unequiptWeapon(x_inventory,weapon_num,player_stats) #Unequipt item.
                x_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory.
            elif user_input.title() == 'Return': #Check for return.
                print('Returning to previous...') #Return message.
            else: #Activate if all other conditions fail.
                print('Error s-1 (runInventoryLoop): That object either doesn\'t exist or cannot be equipped.') #Error message.
                x_inventory = resetInventory(inventory, armour, weapon, items) #Reset inventory.
        elif user_input.title() == choices[1] or user_input.isdigit() and (int(user_input) - 1) == 1: #Check if user chooses 'Trash'.
            choices = items #Set choices as items.
            displayChoiceList('inventory', choices) #Display choices.
            print('What would you like to trash?') #Ask for user input.
            user_input = getInput() #Get user input.
            if user_input.title() in choices: #Check if input is choices.
                object_num, x_object_list = getObjectNumberAndList(food_list, armour_list, weapon_list, user_input) #Get object number and list.
                print('Trashing...') #Action message.
                items = removeFromInventory(x_object_list, object_num, items) #Remove object from inventory.
                print('Trashing complete!') #Completion message.
            elif user_input.isdigit() and len(choices) >= int(user_input): #Check if input is digit and less than total choices.
                object_num, x_object_list = getObjectNumberAndList(food_list, armour_list, weapon_list, choices[int(user_input)-1]) #Get object number and list.
                print('Trashing...') #Action message.
                items = removeFromInventory(x_object_list, object_num, items) #Remove object from inventory.
                print('Trashing complete!')  #Completion message.
            else: #Activate if condition fails; assume input is not in choices.
                print('Error s-2 (runInventoryLoop): Invalid input! That option doesn\'t exist in inventory!') #Error message.
        elif user_input.title() == choices[2] or user_input.isdigit() and (int(user_input) - 1) == 2: #Check if user chooses 'Return'.
            print('Returning to previous...') #Return message.
            inventory_loop = False #End function loop.
            user_quit = False #Keep game going.
        elif user_input.title() == choices[3] or user_input.isdigit() and (int(user_input) - 1) == 3: #Check if user chooses 'Quit'.
            print('Goodbye!') #Farewell message.
            inventory_loop = False #End function loop.
            user_quit = True #End game.
    return user_quit, x_inventory #NOTE: probably going to have to return player stats!
    
#=============================================

#NAVIGATION FUNCTIONS=========================
def displayChoiceList(x_type, choices): #Display list of choices based on input.
    if x_type == 'main': #Check for hardcoded type in parameters; used for general menu and title screen.
        x_title = 'OPTIONS' #Set title of list based on type.   
    elif x_type == 'move': #Used for location menu.
        x_title = 'LOCATION OPTIONS'
    elif x_type == 'search': #Used for search/investigate menu.
        x_title = 'SEARCH OPTIONS'
    elif x_type == 'talk': #Used for speech menu.
        x_title = 'SPEECH OPTIONS'
    elif x_type == 'battle': #Used for battle menu(s).
        x_title = 'BATTLE OPTIONS'
    elif x_type == 'shop': #Used for shop menu(s).
        x_title = 'SHOP OPTIONS'
    elif x_type == 'inventory': #Used for the inventory menu.
        x_title = 'INVENTORY OPTIONS'
    x_title = ('==' + x_title + '==') #Define title.
    print (x_title) #print title indicator.
    for counter in range(len(choices)): #Loop for as many times there are choices.
        print ('-' + str(counter + 1) + '-' + choices[counter]) #Print option.
    print ('=' * len(x_title)) #Print ending indicator as many times as title.

def getInput(): #Function gets user input.
    user_input = input('Your response: ') #Store input in variable.
    return user_input

def changeLocation(u_input, location, choices): #Function changes user location.
    if u_input.title() in choices: #Check if user inputs valid location.
        if u_input.title() == 'Return':
            print('', end='')
        else:
            location = u_input.title() #Set location to user choice.
    elif u_input.isdigit() and len(choices) >= int(u_input) > 0: #Check if user inputs a number beside an option in menu.
        if choices[int(u_input) -1] == 'Return':
            print('', end='')
        else:
            location = choices[(int(u_input)-1)] #Set location based on input. Subtract because list starts at 0.
    else: #Activate if all else fails.
        print('Error s-1 (changeLocation): Invalid response!') #Error message.
    return location
    
def setMoveChoices(location): #Function adjusts choices based on location.
    if location == 'Air Canada Centre': #Check for certain location.
        choices_x = ["Union Station","Raider Hideout","Crater","Supermarket"] #Set choices based on nearby locations on drawn map.
    elif location == 'Supermarket':
        choices_x = ["Crater", "Park", "Harbourfront Centre", "Air Canada Centre"]
    elif location == 'Crater':
        choices_x = ["Raider Hideout", "Supermarket", "Air Canada Centre"]
    elif location == 'Raider Hideout':
        choices_x = ["Union Station", "CN Tower", "Crater", "Air Canada Centre"]
    elif location == 'Union Station':
        choices_x = ["CN Tower","Raider Hideout","Air Canada Centre"]
    elif location == 'Park':
        choices_x = ["Restaurant","Harbourfront Centre","Air Canada Centre"]
    elif location == 'Harbourfront Centre':
        choices_x = ["Restaurant", "Park", "Supermarket"]
    elif location == 'Restaurant':
        choices_x = ["CN Tower", "Hotel", "Park", "Harbourfront Centre"]
    elif location == 'Hotel':
        choices_x = ["CN Tower", "Restaurant"]
    elif location == 'CN Tower':
        choices_x = ["Union Station", "Raider Hideout", "Hotel", "Restaurant"]
    choices_x.append('Return')
    choices_x.append('Quit')
    return choices_x

def initializeLocation(): #Function sets location and choices based on game story.
    #NOTE: This function should only be used at the beginning of the game.
    location = 'Air Canada Centre' #Initialize location as starting point in game.
    choices = ["Move","Search","Talk"] #Initialize choices.
    return location, choices
    
def runLocationLoop(location, choices): #Function includes the entirety of moving.
    user_quit = False #Initialize local variable as false.
    u_input = '' #Initialize as blank string.
    nav_loop = True #Activate loop.
    while(nav_loop): #Navigation loop. Loop for as long as variable remains true.
        print ('You\'re currently at the ' + location) #Display current location.
        print ('Where would you like to move to?') #Ask for input.
        choices = setMoveChoices(location) #Get user choice.
        displayChoiceList('move',choices) #Display choice options.
        u_input = getInput() #Get user input.
        location = changeLocation(u_input, location, choices) #Change the location.
        if location.upper() == 'QUIT': #Check if user wants to quit.
            print ('Goodbye!') #Goodbye message.
            nav_loop = False #End loop.
            user_quit = True #Set variable to true
        elif location.upper() == 'RETURN': #Check if user wants to return.
            print('Returning to previous...') #Return message.
            nav_loop = False #End loop. <-- Remove later.
            user_quit = False #Set to variable to false.
        return user_quit, location
#=============================================
            
#SEARCH FUNCTIONS=============================
#To do list: include the ability to search and find money.    
def setSearchChoices(location):
    if location == 'Air Canada Centre': #Check for specific location.
        #NOTE: search choices that display a message (if they exist) come first, then choices that can have randomized rewards.
        x_choices = ["Monitors", "Sleeping Chamber", "Cupboard", "Fridge", "Outside"] #Set list of search options. choice_num = 3, index_skip = 2.
    elif location == 'Supermarket':
        x_choices = ["Produce Department", "Cash Register"] #choice_num = 2
    elif location == 'Crater':
        x_choices = ["Sign","Rocks","Crater Viewing", "Weapon Shop"] #choice_num = 2, index_skip = 1.
    elif location == 'Raider Hideout':
        x_choices = ["Mysterious Box", "Coffee Table", "Bed"] #choice_num = 3
    elif location == 'Union Station':
        x_choices = ["Monitors","Train Tracks", "Terminal"] #choice_num = 1, index_skip = 1.
    elif location == 'Park':
        x_choices = ["Slide","Swings","Monkey Bars"] #choice_num = 3
    elif location == 'Harbourfront Centre':
        x_choices = ["Boats", "Food Truck"] #choice_num = 2
    elif location == 'Restaurant':
        x_choices = ["Table", "Bar", "Kitchen", "Food Shop"] #choice_num = 3
    elif location == 'Hotel':
        x_choices = ["Front Desk", "Lobby"] #choice_num = 1, index_skip = 1.
    elif location == 'CN Tower':
        x_choices = ["Outside", "Gift Shop", "Main Pod", "Armour Shop"] #choice_num = 3
    x_choices.append('Return')
    x_choices.append('Quit')
    return x_choices

def getRewardList(location): #Function gets the reward list for specific location.
    if location == 'Air Canada Centre': #Check for specific location.
        location_reward_list = acc_rewards #Set reward list based on location.
    elif location == 'Supermarket':
        location_reward_list = market_rewards
    elif location == 'Crater':
        location_reward_list = crater_rewards
    elif location == 'Raider Hideout':
        location_reward_list = raider_rewards
    elif location == 'Union Station':
        location_reward_list = station_rewards
    elif location == 'Park':
        location_reward_list = park_rewards
    elif location == 'Harbourfront Centre':
        location_reward_list = hfcentre_rewards
    elif location == 'Restaurant':
        location_reward_list = restaurant_rewards
    elif location == 'Hotel':
        location_reward_list = hotel_rewards
    elif location == 'CN Tower':
        location_reward_list = cntower_rewards
    return location_reward_list

def setSearchRewards(x_location_reward_list,choice_num,index_skip): #Function sets reward for specific location.
    #NOTE: choice_num is the number of choices that can be randomized. index_skip is the amount of choices that cannot be randomized.
    for counter in range(index_skip): #Loop index_skip amount of times.
        x_location_reward_list.append('Message') #Add the keyword 'Message' to the reward list.
    for counter in range(choice_num): #Loop choice_num amount of times.
        random_chance = random.randint(1,2) #Randomize either a 1 or 2.
        if random_chance == 1: #Check for 1; 1 means a reward will be generated.
            reward_list, reward_num = randomizeReward() #Randomize reward and reward_list.
            reward_list = list(reward_list.keys()) #Get the keys from reward_list.
            reward = reward_list[reward_num] #Get reward using the reward_list and reward_num.
            x_location_reward_list.append(reward) #Add reward to list.
        else: #Activate if all other conditions fail; assume 2. 2 means a reward will not be generated.
            x_location_reward_list.append('Nothing') #Add the keyword 'Nothing' to the reward list.
    if x_location_reward_list == station_rewards:
        x_location_reward_list.append('Terminal')
       
def generateAllGameRewards(): #Function generates search rewards for all locations in the game.
    setSearchRewards(acc_rewards,3,2) #Set reward list for ACC.
    setSearchRewards(market_rewards,2,0) #Set reward list for Supermarket.
    setSearchRewards(crater_rewards,2,1) #Set reward list for Crater.
    setSearchRewards(raider_rewards,3,0) #Set reward list for Raider Hideout.
    setSearchRewards(station_rewards,1,1) #Set reward list for Union Station.
    setSearchRewards(park_rewards,3,0) #Set reward list for Park.
    setSearchRewards(hfcentre_rewards,2,0) #Set reward list for Harbourfront Centre.
    setSearchRewards(restaurant_rewards,3,0) #Set reward list for Restaurant.
    setSearchRewards(hotel_rewards,1,1) #Set reward list for Hotel.
    setSearchRewards(cntower_rewards,3,0) #Set reward list for CN Tower.

def removeFromRewardList(location_reward_list, object_index): #Function removes object from reward list.
    location_reward_list[object_index] = 'Nothing' #Set reward in reward list to to nothing.
    return location_reward_list
    
def randomizeRewardList(): #Function randomizes an 'object list'.
    reward_list = 0 #Initialize as 0.
    reward_list = random.randint(1,3) #Ranomize a number between 1-3. Each number represents one of the three item lists.
    if reward_list == 1: #Check for randomized number.
        reward_list = food_list #Set list based on result.
    elif reward_list == 2: 
        reward_list = weapon_list
    elif reward_list == 3:
        reward_list = armour_list
    return reward_list

def randomizeRewardNumber(reward_list): #Function randomizes an object number based on list parameter.
    reward = list(reward_list.keys()) #Set reward as list of reward_list dictionary keys.
    list_end = len(reward_list) - 1 #Set end of randomizer range as the len value of list subtracted by one. (subtract one to account for list index rules).
    reward_num = random.randint(0, list_end) #Randomize reward number.
    return reward_num

def randomizeReward(): #Function includes randomization of reward_num and reward_list.
    reward_list = randomizeRewardList() #Randomize an 'object list'.
    reward_num = randomizeRewardNumber(reward_list) #Randomize an 'object number'.
    return reward_list, reward_num

def displayMessage(message_list, message_num): #Function displays message with a title bar preceeding it.
    message = message_list[message_num] #Set message as specific message in message list.
    print('==SEARCH OBSERVATION==') #Title bar.
    print(message) #Print message.
    print('=' * 22) #Ending title bar.

def getMessageNumber(location, search): #Function gets message_num variable based on location and user search choice.
    if location == 'Air Canada Centre' and search == 'Monitors': #Check for specific location and search choice.
        message_num = 0 #Set message_num based on if statement conditions.
    elif location == 'Air Canada Centre' and search == 'Sleeping Chamber':
        message_num = 1
    elif location == 'Crater' and search == 'Sign':
        message_num = 2
    elif location == 'Union Station' and search == 'Monitors':
        message_num = 3
    elif location == 'Hotel' and search == 'Front Desk':
        message_num = 4
    else: #Activate if all other conditions fail.
        print('Error: uh oh! Looks like something went wrong in getMessageNumber!') #Error message.
        message_num = 6 #Set message as nothing by default.
    return message_num

def checkForKeyword(x_keyword, search, food_list, armour_list, weapon_list, message_list, message_num, location, player_stats, current_health, money): #Function checks for keyword; Includes the displaying of messages, and adding to inventory.
    if x_keyword == 'Message': #Check for message keyword.
        message_num = getMessageNumber(location, search) #Get message number and set it as message_num.
        displayMessage(message_list, message_num) #Display messag\e.
        if message_num == 3: #Check for the Alexandria message. NOTE: FINAL BOSS IS HERE.
            choices = ['Yes', 'No'] #Set choices.
            print('Would you like to investigate Track 227?') #Ask for user input.
            displayChoiceList('main',choices) #Display choices.
            user_input = getInput() #Get user input.
            if user_input.title() == choices[0] or user_input.isdigit() and int(user_input) - 1 == 0: #Check for yes.
                user_quit = getFinalBoss(player_stats, current_health, money, exp) #Start the final boss event.
                return user_quit
            elif user_input.title() == choices[1] or user_input.isdigit() and int(user_input) - 1 == 1: #Check for no.
                print('',end='') #Do nothing.
            else: #Activate if all other conditions fail; assume input is invalid.
                print('Error s-1 (checkForKeyword): Input is invalid!')
    elif x_keyword == 'Nothing': #Check for nothing keyword.
        displayMessage(message_list, 5) #Display message for finding nothing.
    elif x_keyword == 'Terminal': #Check for terminal keyword.
        money = displayTerminal(money) #Open terminal.
    else: #Activate if all other conditions fail.
        if x_keyword in list(food_list.keys()): #Check if keyword is in food list.
            food_list_keys = list(food_list.keys()) #Set food_list_keys as all keys in food_list.
            x_object_num = food_list_keys.index(x_keyword) #Get the index of the keyword in food list.
            addToInventory(food_list, x_object_num, items) #Add food to inventory.
            return True #Return True; True signifies that a keyword object was found.
                                 
        elif x_keyword in list(weapon_list.keys()): #Check if keyword is in weapon list.
            weapon_list_keys = list(weapon_list.keys()) #Set weapon_list_keys as all keys in weapon list.
            x_object_num = weapon_list_keys.index(x_keyword) #Get the index of the keyword in weapon list.
            addToInventory(weapon_list, x_object_num, items) #Add weapon to inventory.
            return True #Return True; True signifies that a keyword object was found.
                                 
        elif x_keyword in list(armour_list.keys()): #Check if keyword is in armour list.
            armour_list_keys = list(armour_list.keys()) #Set armour_list_keys as all keys in armour list.
            x_object_num = armour_list_keys.index(x_keyword) #Get the index of keywrod in armour list.
            addToInventory(armour_list, x_object_num, items) #Add armour to inventory.
            return True #Return True; True signifies that a keyword object was found.

def searchSpot(u_input, choices, location, money, weapon_shop, armour_shop, food_shop, message_list, message_num, player_stats, current_health): #Function checks user input and searches based on it.
    location_reward_list = getRewardList(location) #Set reward list based on current location.
    x_check = 0 #Initialize as 0.
    if u_input.upper() == 'RETURN' or u_input.isdigit() == True and len(choices) >= int(u_input) > 0 and choices[int(u_input)-1].upper() == 'RETURN': #Check if user wants to return.
        print('Returning to previous menu...') #Return message.
        user_quit = False #Set variable to true.
        search_loop = False #Deactive search loop.
    elif u_input.upper() == 'QUIT' or u_input.isdigit() == True and len(choices) >= int(u_input) > 0 and choices[int(u_input)-1].upper() == 'QUIT': #Check if user wants to quit.
        print('Goodbye!') #Farewell message.
        user_quit = True #Set variable to true.
        search_loop = False #Deactive search loop.
    elif u_input.title() in choices and u_input.title() == 'Weapon Shop' or u_input.isdigit() and len(location_reward_list) >= (int(u_input) - 1) > 0 and choices[int(u_input)-1].title() == 'Weapon Shop': #Check if user wants to enter specific shop and it is in choices list.
        money, weapon_shop = runShop(money, weapon_shop, location, items)
        user_quit = False #Set variable to false.
        search_loop = True #Keep search loop active.
    elif u_input.title() in choices and u_input.title() == 'Armour Shop' or u_input.isdigit() and len(location_reward_list) >= (int(u_input) - 1) > 0 and choices[int(u_input)-1].title() == 'Armour Shop': #Check if user wants to enter specific shop and it is in choices list.
        money, armour_shop = runShop(money, armour_shop, location, items)
        user_quit = False #Set variable to false.
        search_loop = True #Keep search loop active.
    elif u_input.title() in choices and u_input.title() == 'Food Shop' or u_input.isdigit() and len(location_reward_list) >= (int(u_input) - 1 > 0) and choices[int(u_input)-1].title() == 'Food Shop': #Check if user wants to enter specific shop and it is in choices list.
        money, food_shop = runShop(money, food_shop, location, items)
        user_quit = False #Set variable to false.
        search_loop = True #Keep search loop active.
    elif u_input.title() in choices: #Check if input exists in choices list.
        search_index = choices.index(u_input.title()) #Get the index of user choice.
        search = choices[search_index] #Get the user choice from choices list.
        x_keyword = location_reward_list[search_index] #Set keyword as user choice in reward list.
        print('You search the ' + choices[search_index] + '...') #Action message.
        x_check = checkForKeyword(x_keyword, search, food_list, armour_list, weapon_list, message_list, message_num, location, player_stats, current_health, money) #Check for keyword and send result of check into x_check.
        if x_check == 'user_quit':
            user_quit = True
            search_loop = False
        else:
            user_quit = False #Set variable to false.
            search_loop = True #Keep search loop active.
    elif u_input.isdigit() and len(choices) >= int(u_input) > 0: #Check if user inputs a number beside an option in menu.
        search_index = choices[(int(u_input)-1)] #Set location based on input. Subtract because list starts at 0.
        search_index = choices.index(search_index) #Get the index of user_choice.
        search = choices[search_index] #Get the user choice from choices list.
        x_keyword = location_reward_list[search_index] #Set keyword as user choice in reward list.
        print('You search the ' + choices[search_index] + '...') #Action message.
        x_check = checkForKeyword(x_keyword, search, food_list, armour_list, weapon_list, message_list, message_num, location, player_stats, current_health, money) #Check for keyword and send result of check into x_check.
        if x_check == 'user_quit':
            user_quit = True
            search_loop = False
        else:
            user_quit = False #Set variable to false.
            search_loop = True #Keep search loop active.
    else: #Activate if all other conditions fail.
        print('Error s-1 (searchSpot): Oops! That\'s not a valid response. Please try again') #Error message.
        user_quit = False #Set variable to false.
        search_loop = True #Keep search loop active.
    if x_check == True: #Check if x_check returned true. This mean an object keyword has been found.
        removeFromRewardList(location_reward_list,search_index)#Replace object keyword with 'Nothing' keyword.
        user_quit = False #Set variable to false.
        search_loop = True #Keep search loop active.
    return user_quit, search_loop, money
            
def runSearchLoop(location, u_input, money, weapon_shop, armour_shop, food_shop, message_list, message_num, player_stats, current_health): #Function includes entire Search loop.
    search_loop = True #Activate loop.
    while(search_loop): #Loop for as long as search variable remains true.
        print ('You\'re currently at the ' + location) #Print location.
        print ('Where would you like to search?') #Ask for input.
        choices = setSearchChoices(location) #Set search options.
        displayChoiceList('search',choices) #Display choice list.
        u_input = getInput() #Get user input.
        user_quit, search_loop, money = searchSpot(u_input,choices,location, money, weapon_shop, armour_shop, food_shop, message_list, message_num, player_stats, current_health) #Search the location.
    return user_quit
        
#=============================================
#MAIN PROGRAM FUNCTIONS=======================
def printCredits(): #Function prints the credits.
    print(' ICS3U Period 5 CA by: Brandon Phillips, Julien Ouellette') 
    
def printAsciiWasteland(): #Function prints game title in ASCII line by line. (Source: http://patorjk.com/software/taag/#p=display&f=Bulbhead&t=Wasteland)
    print(' _    _    __    ___  ____  ____  __      __    _  _  ____')  
    print('( \\/\\/ )  /__\\  / __)(_  _)( ___)(  )    /__\\  ( \\( )(  _ \\') 
    print(' )    (  /(__)\ \__ \  )(   )__)  )(__  /(__)\  )  (  )(_) )')
    print('(__/\\__)(__)(__)(___/ (__) (____)(____)(__)(__)(_)\_)(____/')

def printAsciiExplosion(): #Function prints an ASCII explosion line by line. (Source: http://www.chris.com/ascii/index.php?art=objects/explosives)
    print('              ________________')
    print('         ____/ (  (    )   )  \___')
    print('        /( (  (  )   _    ))  )   )\\')
    print('      ((     (   )(    )  )   (   )  )')
    print('    ((/  ( _(   )   (   _) ) (  () )  )')
    print('   ( (  ( (_)   ((    (   )  .((_ ) .  )_')
    print('  ( (  )    (      (  )    )   ) . ) (   )')
    print(' (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )')
    print(' ( (  (   ) (  )   (  ))     ) _)(   )  )  )')
    print('( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )') 
    print(' (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )')
    print('( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )') 
    print(' ((  (   )(    (     _    )   _) _(_ (  (_ )')
    print('  (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)')
    print('  ((__)        \\||lll|l||///          \_))')
    print('          (   /(/ (  )  ) )\   )')
    print('         (    ( ( ( | | ) ) )\   )')
    print('          (   /(| / ( )) ) ) )) )')
    print('        (     ( ((((_(|)_)))))     )')
    print('         (      ||\(|(|)|/||     )')
    print('       (        |(||(||)||||        )')
    print('         (     //|/l|||)|\\ \     )')
    print('       (/ / //  /|//||||\\  \ \  \ _)')
    print('') #Print blank line to give space.
    
def printTitleScreen(): #Function prints entire title screen.
    print('=' * 60) #Title bar.
    printAsciiWasteland() #Print title.
    print('')#Print blank line; add a space.
    printCredits() #Print credits.
    print('=' * 60) #End title bar.

def getTitleScreenLoop(user_input): #Function contains menu loop at the title screen.
    x_loop = True #Activate loop.
    while(x_loop): #Activate for as long as loop variable remains true.
        choices = ['Start', 'Quit'] #Define valid choices.
        displayChoiceList('main',choices) #Display valid choices.
        user_input = getInput() #Get user input.
        if user_input.title() == choices[0] or user_input.isdigit() and (int(user_input) - 1) == 0: #Check if user chooses 'Start'.
            user_quit = False #Continue game.
            x_loop = False #End loop.
        elif user_input.title() == choices[1] or user_input.isdigit() and (int(user_input) - 1) == 1: #Check if user chooses 'Quit'.
            print('Goodbye!') #Farewell message.
            user_quit = True #End game.
            x_loop = False #End loop.
        else: #Activate if all other conditions fail.
            print('Error s-1 (getTitleScreenLoop): Input is invalid! Please try again.') #Error message.
    return user_quit

def getTitleScreen(): #Function includes entirety of title screen.
    printTitleScreen() #Print title screen.
    user_quit = getTitleScreenLoop(user_input) #Menu loop.
    return user_quit

def printIntroductionMessage(): #Function contains prologue message. Prints line by line.
    print('It is the year 2177, a half century after the')
    print('events of World War Three. The use of nuclear')
    print('weapons lead to the downfall of humanity and')
    print('left the entire planet in a seemingly endless')
    print('state of nuclear winter. The game begins when')
    print('our protagonist -the player, wakes up to their')
    print('sleeping pod crashing back towards earth.')

def printStoryIntroduction(): #Function prints game introduction.
    print('SYSTEM: OXYGEN LEVELS CRITICAL!')
    print('        INITIATING EMERGENCY EXIT!')
    print('*There is a long silence*')
    print('*Suddenly you hear a loud \'THUD\' and are blinded by')
    print(' a white light... Eventually your vision returns...*')
        
def printIntroduction(): #Function prints the entirety of the introduction.
    print('=' *45) #Explosion Title bar.
    printAsciiExplosion() #Print ASCII explosion.
    print(('=' * 20) + 'INTRO' + ('=' * 20)) #Message Title bar.
    printIntroductionMessage()
    print('=' *45)#Message end title bar.

def askForIntro(): #Function asks if user wants to see the introduction.
    user_input = '' #Initialize local variable as blank string.
    intro_loop = True #Activate loop.
    while(intro_loop): #Activate for as long as variable remains true.
        print('This game has a (short) introduction. Would you like to skip it?') #Ask for input.
        choices = ['Yes','No'] #Set choices.
        displayChoiceList('main',choices) #Display choices.
        user_input = getInput() #Get input.
        if user_input.title() == 'Yes' or user_input.isdigit() and (int(user_input) - 1) == 0: #Check for yes.
            intro_check = False #Set check as false.
            intro_loop = False #Deactivate loop.
        elif user_input.title() == 'No' or user_input.isdigit() and (int(user_input) - 1) == 1: #Check for no.
            intro_check = True #Set check as true.
            intro_loop = False #Deactivate loop.
        else: #Activate if all other conditions fail. Assume input is invalid.
            print('Error s-1 (askForIntro): Input is invalid! Please try again.') #Error message.
    return intro_check

def setPlayerStats(): #Function lets the user set their own stats.
    x_player_stats = [0,0,0,0,0] #Initialize local variable as a list of 5 0's.
    x_player_stats = initializePlayerStats(player_stats) #Initialize player stats.
    displayStats(x_player_stats) #Display player stast.
    extra_points = 4 #Define extra points as 4.
    for x_counter in range(1,5): #Loop 4 times; one iteration represents 1 stat.
        if x_counter == 1: #Check if counter is at specific point.
            stat = 'STRENGTH' #Set stat name.
            desc = 'This effects how much damage you do to enemies.' #Set stat description.
        elif x_counter == 2:
            stat = 'DEFENCE'
            desc = 'This effects how much damage enemies do to you.'
        elif x_counter == 3:
            stat = 'SPEED'
            desc = 'This effects turn order and if you can flee a battle.'
        elif x_counter == 4:
            stat = 'HEALTH'
            desc = 'This effects how much damage you can take before you die.'
        if extra_points == 0: #Check if there are no more available points are left.
            print('',end='') #Do nothing.
        else: #Activate if conditions fails; assumes that extra_points > 0
            print('Available points: ' + str(extra_points)) #Display current amount of available points.
            print('How many points would you like to add to your ' + stat + ' stat?') #Asks user for input.
            print('Description: ' + desc) #Display specific individual stat description.
            response = getInput() #Get input.
            if response.isdigit() == False: #Check if input is not all numbers.
                print('Error s-1 (setPlayerStats): You have not inputted (only) a number!') #Error message.
            else: #Activate if conditions fail; assume that response in all numbers.
                response = int(response) #Cast into int.
                if response > extra_points or response < 0: #Check if response exceeds available points or if it's less than 0.
                    print('Error s-2 (setPlayerStats): number is either bigger than what is available or a negative!') #Error message.
                else: #Activate if conditions fail; assume that response is valid.
                    x_player_stats[x_counter] += response #Add response to individual player stat.
                    extra_points -= response #Subtract response from extra points total.
    displayStats(x_player_stats) #Display adjusted player stats.
    current_health = x_player_stats[4] #Set current to max health
    return x_player_stats, current_health #Return player stats and current health

def getFinalBoss(player_stats, current_health, moneyx, x_exp): #Function contains the entire final boss story scene and fight.
    print(('=' * 20) + 'STORY' + ('=' * 20)) #Story Title bar.
    print('*You enter the mysterious train and it leads')
    print('you into a strange, dimly lit room...')
    print('????: I\'ve been waiting for you, space man!')
    print('*You turn in the direction of the voice and bright red')
    print('lights turn on. You can now see a cloaked individual standing')
    print('a couple meters directly in front of you...*')
    print('????: Your untouched DNA shall further my knowledge')
    print('      about the world before the bombs. Now die!')
    print('*The cloaked individual pulls out his sword')
    print('and charges!*')
    print('='*45) #End title bar.
    final_battle = True
    boss_names = list(boss_stats.keys())
    boss_all_stats = list(boss_stats.values())
    enemy_name = boss_names[2]
    enemy_stats = boss_all_stats[2]
    print(enemy_name + ' has begun to attack you!')
    while(final_battle):
        displayChoiceList('battle', battle_options) #Display battle options
        u_input = getUserMove() #Get the user move
        final_battle, player_stats, current_health, u_input, moneyx, x_exp = runUserMove(u_input, player_stats, current_health, enemy_stats, moneyx, x_exp) #Run the user move
    if enemy_stats[4] <= 0:
        print(('=' * 20) + 'STORY' + ('=' * 20)) #Story title bar.
        print('THE LIBRARIAN: My advanced research...')
        print('*The Librarian has fled the scene*')
        print('='*50) #End title bar.
        print('Congratulations! You have completed Wasteland.')
        return 'user_quit'
    elif current_health <= 0:
        return 'user_quit'
    else:
        return False

def getCraterDialogue(): #Function includes all dialogue for crater.
    x_loop = True #Activate function loop.
    print(('=' * 20) + 'SPEECH' + ('=' * 20)) #Title bar.
    print('DENNIS: Well would you look at that!')
    print('        You don\'t see many people around')
    print('        these parts! What can I do for ya?')
    print('='*46) #End title bar.
    while(x_loop): #Loop for as long 
        choices = [ 'What happened here?', #Define choices.
                    'Where can I get a weapon?',
                    'Where can I get some armour?',
                    'Return',
                    'Quit']
        displayChoiceList('talk', choices) #Display choices.
        user_input = getInput() #Get input.
        if user_input.upper() == choices[0].upper() or user_input.isdigit() and int(user_input) == 1: #Check for option.
            print('DENNIS: What, you\'ve been living under a rock!?') #Display message.
            print('        The bombs friggin dropped! That\'s what!')
        elif user_input.upper() == choices[1].upper() or user_input.isdigit() and int(user_input) == 2:
            print('DENNIS: Hm? The weapon shop is pretty close here')
            print('        all you gotta do is SEARCH and you should find it.')
        elif user_input.upper() == choices[2].upper() or user_input.isdigit() and int(user_input) == 3:
            print('DENNIS: Only place I know of with an armour shop')
            print('        is where the old CN Tower used to be.')
            print('        you can get there from here through')
            print('        the Supermarket to Park to Restaurant')
            print('        to CN Tower.')
        elif user_input.upper() == choices[3].upper() or user_input.isdigit() and int(user_input) == 4: #Check for return.
            print('Returning to previous...') #Return message.
            x_loop = False #End loop.
            user_quit = False #Continue game.
        elif user_input.upper() == choices[4].upper() or user_input.isdigit() and int(user_input) == 5: #Check for quit.
            print('Goodbye!') #Farewell message.
            x_loop = False #End loop.
            user_quit = True #End game.
    return user_quit
        
def getHarbourFrontDialogue():
    x_loop = True #Activate function loop.
    print(('=' * 20) + 'SPEECH' + ('=' * 20)) #Title bar.
    print('ANGUS: You look lost friend...')
    print('='*46) #End title bar.
    while(x_loop): #Loop for as long 
        choices = [ 'Who are you?', #Define choices.
                    'Where am I?',
                    'Return',
                    'Quit']
        displayChoiceList('talk', choices) #Display choices.
        user_input = getInput() #Get input.
        if user_input.upper() == choices[0].upper() or user_input.isdigit() and int(user_input) == 1: #Check for option.
            print('ANGUS: The name\'s Angus. That\'s all you need to know.') #Display message.
        elif user_input.upper() == choices[1].upper() or user_input.isdigit() and int(user_input) == 2:
            print('ANGUS: This used to be the HarbourFront Centre.')
            print('       Now it\'s just a stronghold for Red Angels')
            print('       -former military.')
        elif user_input.upper() == choices[2].upper() or user_input.isdigit() and int(user_input) == 3: #Check for return.
            print('Returning to previous...') #Return message.
            x_loop = False #End loop.
            user_quit = False #Continue game.
        elif user_input.upper() == choices[3].upper() or user_input.isdigit() and int(user_input) == 4: #Check for quit.
            print('Goodbye!') #Farewell message.
            x_loop = False #End loop.
            user_quit = True #End game.
    return user_quit

def getCNTowerDialogue():
    x_loop = True #Activate function loop.
    print(('=' * 20) + 'SPEECH' + ('=' * 20)) #Title bar.
    print('FLORES: Welcome traveler! Please enjoy your stay!')
    print('='*46) #End title bar.
    while(x_loop): #Loop for as long 
        choices = [ 'Who are you?', #Define choices.
                    'Where am I?',
                    'What do you do?',
                    'Armour shop?',
                    'Return',
                    'Quit']
        displayChoiceList('talk', choices) #Display choices.
        user_input = getInput() #Get input.
        if user_input.upper() == choices[0].upper() or user_input.isdigit() and int(user_input) == 1: #Check for option.
            print('FLORES: I\'m Flores, leader of the Guardians!.') #Display message.
        elif user_input.upper() == choices[1].upper() or user_input.isdigit() and int(user_input) == 2:
            print('FLORES: This was formerly the CN Tower before ')
            print('        the war. The Guardians have since re-')
            print('        purposed this site into our home.')
        elif user_input.upper() == choices[2].upper() or user_input.isdigit() and int(user_input) == 3:
            print('FLORES: Glad you asked! The Guardians.')
            print('        travel to help innocents in need!')
            print('        As for me... well I lead them.')
        elif user_input.upper() == choices[3].upper() or user_input.isdigit() and int(user_input) == 4:
            print('FLORES: To access the armour shop, simply')
            print('        SEARCH around and you should find')
            print('        it. It\'s hard to miss!')
        elif user_input.upper() == choices[4].upper() or user_input.isdigit() and int(user_input) == 5: #Check for return.
            print('Returning to previous...') #Return message.
            x_loop = False #End loop.
            user_quit = False #Continue game.
        elif user_input.upper() == choices[5].upper() or user_input.isdigit() and int(user_input) == 6: #Check for quit.
            print('Goodbye!') #Farewell message.
            x_loop = False #End loop.
            user_quit = True #End game.
    return user_quit
            
def getRaiderHideoutDialogue():
    x_loop = True #Activate function loop.
    print(('=' * 20) + 'SPEECH' + ('=' * 20)) #Title bar.
    print('MORGAN: Alexandria... Huh? who the heck are you?')
    print('='*46) #End title bar.
    while(x_loop): #Loop for as long 
        choices = [ 'Who are you?', #Define choices.
                    'Where am I?',
                    'What\'s Alexandria?',
                    'Return',
                    'Quit']
        displayChoiceList('talk', choices) #Display choices.
        user_input = getInput() #Get input.
        if user_input.upper() == choices[0].upper() or user_input.isdigit() and int(user_input) == 1: #Check for option.
            print('MORGAN: I asked first.') #Display message.
        elif user_input.upper() == choices[1].upper() or user_input.isdigit() and int(user_input) == 2:
            print('MORGAN: T\'is the raider den. It\'s')
            print('        basically a hangout for all')
            print('        the thieves of Toronto.')
        elif user_input.upper() == choices[2].upper() or user_input.isdigit() and int(user_input) == 3:
            print('MORGAN: There\'s a rumour that there\'s a secret')
            print('        society in a place called \'Alexandria\'.')
            print('        My friend said the entrance is somewhere')
            print('        in Union Station. so you should check it out if')
            print('        you\'re really curious.')
        elif user_input.upper() == choices[3].upper() or user_input.isdigit() and int(user_input) == 4: #Check for return.
            print('Returning to previous...') #Return message.
            x_loop = False #End loop.
            user_quit = False #Continue game.
        elif user_input.upper() == choices[4].upper() or user_input.isdigit() and int(user_input) == 5: #Check for quit.
            print('Goodbye!') #Farewell message.
            x_loop = False #End loop.
            user_quit = True #End game.
    return user_quit

def runSpeech(location): #Function contains the entirety of speech system.
    if location == 'Crater': #Check for specific location.
        user_quit = getCraterDialogue() #Activate dialogue loop for that location.
    elif location == 'HarbourFront Centre':
        user_quit = getHarbourFrontDialogue()
    elif location == 'CN Tower':
        user_quit = getCNTowerDialogue()
    elif location == 'Raider Hideout':
        user_quit = getRaiderHideoutDialogue()
    else: #Activate if all other condtions fail; assume there is no dialogue for user location.
        print('There are no people to talk to at this location (' + location + ').') #Message.
        user_quit = False #Continue game.
    return user_quit

#Terminal
riddles = ['How many letters are in the alphabet?', #Create list of riddles
             'Mr. Smith has 4 daughters. Each of his daughters has a brother. How many children does Mr. Smith have?',
             'What number do you get when you multiply all of the numbers on a telephone\'s number pad?',
             'How many seconds are in a year?',
             'During what month do people sleep the least?',
             'A king, queen and two twins all lay in a large room. How many adults are in the room?',
             'How many eggs can you put in an empty basket?',
             '1, 11, 21, 1211 what\'s the next number in the sequence?',
             'An empty bus pulls up to a stop and 10 people get on. At the next stop 5 people get off and 20 people get on. At the third stop 25 people get off. How many people are currently on the bus?']

answers = [11, #Create list of answers to riddles
           5,
           0,
           12,
           2,
           0,
           1,
           111221,
           1]

answer_explain = ['There are 11 letters in \'the alphabet\'.', #Create list explaining the riddles
                  'All the daughters have the same brother.',
                  'Everything will be multiplied by 0.',
                  'The 2nd of January, 2nd of February, etc.',
                  'Since February has the least number of days.',
                  'They are all mattresses.',
                  'Since after you put 1 in the basket is no longer empty.',
                  'The each number describes the previous number. 1 -> 11(since there was one 1) --> 21(since there was two 1\'s).',
                  'Just the driver is left.']

def getRiddle(riddles, answers, answer_explain): #Defining getRiddle as a function
    riddle_num = random.randint(0,8) #Get the index of the of riddle
    x_riddle = riddles[riddle_num] #Get the riddle
    x_answer = answers[riddle_num] #Get the riddle answer
    x_answer_explain = answer_explain[riddle_num] #Get the riddle explaination
    return x_riddle, x_answer, x_answer_explain #Return riddle, riddle answer and riddle explaination

def getUserAnswer(): #Defining getUserAnswer as a function
    while(True): #Run infinite loop
        user_input = input('Your response (numerical answers or \'return\' to exit): ') #Get user input
        if user_input.title() != 'Return': #If user doesn't want to return
            try: #Try the following code
                user_input = int(user_input) #Cast user input into an integer
                break #Break from loop
            except ValueError: #If user input can't be casted into an integer, accept the error
                print('ERROR - Your input was invaild!') #Print statement
        else: #If user wants to return
            break #Break from loop
    return user_input #Return user input

def getTermMoney(money):
    gain_money = random.randint(15, 30)
    money += gain_money
    print('You have gained $' + str(gain_money) + '!')
    return money

def checkUserAnswer(user_inputx, x_answer, x_answer_explain, money): #Defining checkUserAnswer as a function
    if user_inputx == x_answer: #Check if user got the answer correct
        print('Correct! ' + x_answer_explain) #Print statement
        money = getTermMoney(money)
        return (False, money) #Return False
    elif str(user_inputx).title() == 'Return': #Check if user wants to return
        print('You exit the terminal.') #Print statement
        return (False, money) #Return False
    else: #If user didn't get the answer correct
        print('You\'ve answered incorrectly!') #Print statement
        return (True, money) #Return True
        
def displayTerminal(money): #Defining displayTerminal as a function
    terminal_loop = True #Set varaible to true
    x_riddle, x_answer, x_answer_explain = getRiddle(riddles, answers, answer_explain) #Get riddle, riddle answer and riddle explaination
    while(terminal_loop): #Run loop while variable is true
        print(x_riddle) #Print the riddle
        user_input = getUserAnswer() #Get user input
        terminal_loop, money = checkUserAnswer(user_input, x_answer, x_answer_explain, money) #Check if user got the riddle correct
    return money

def runMainLoop(user_input, user_quit, location, inventory, player_stats, current_health, money, exp): #Function includes entirety of main game.
    x_main_loop = True #Activate loop.
    while(x_main_loop): #Loop for as long as variable remains true.
        if user_quit == True: #Check is user has quit.
            x_main_loop = False #Deactivate function loop.
            print('',end='') #Do nothing.
        else: #Activate if all other conditions fail. Assume user has not quit yet.
            choices = ['Move','Search','Talk','Inventory','Quit'] #Set choices.
            displayChoiceList('main',choices) #Display choices.
            user_input = getInput() #Get input.
            if user_input.title() == choices[0] or user_input.isdigit() and (int(user_input) - 1) == 0: #Check if user chooses move.
                player_stats, current_health, user_quit, money, exp = runBattle(player_stats, current_health, user_quit, money, exp) #Run a battle
                if checkUserLevelUp(exp, player_stats): #Check if player should level up
                    exp = subtractXP(exp, player_stats)
                    player_stats = levelPlayer(player_stats) #Level up player
                else: #If player shouldn't level up
                    print('', end='') #Skip line
                if user_quit != True: #If user doesn't want to quit
                    user_quit, location = runLocationLoop(location, choices) #Move locations
                else: #If user does want to quit
                    print('Goodbye!') #Print statement
            elif user_input.title() == choices[1] or user_input.isdigit() and (int(user_input) - 1) == 1: #Check if user chooses search.
                user_quit = runSearchLoop(location, user_input, money, weapon_shop, armour_shop, food_shop, message_list, message_num, player_stats, current_health)
            elif user_input.title() == choices[2] or user_input.isdigit() and (int(user_input) - 1) == 2: #Check if user chooses talk.
                user_quit = runSpeech(location)
            elif user_input.title() == choices[3] or user_input.isdigit() and (int(user_input) - 1) == 3: #Check if user wants to check inventory.
                user_quit, inventory = runInventoryLoop(user_input,inventory,food_list,armour_list,weapon_list,armour,weapon,items,player_stats)
            elif user_input.title() == choices[4] or user_input.isdigit() and (int(user_input) - 1) == 4: #Check if user quit.
                print('Goodbye!') #Farewell message.
                x_main_loop = False #Deactivate function loop.
            else: #Activate if all other conditions fail; Assume user entered invalid input.
                print('Error s-1 (runMainLoop): Invalid input!')       
#=============================================

#MAIN PROGRAM (GAME)==========================
user_quit = getTitleScreen() #Title screen.
if user_quit == False: #Check if user has quit; section includes introduction and setting player stats.
    intro_check = askForIntro() #Ask user if they want to see the intro.
    if intro_check == True: #If they choose yes...
        printIntroduction() #Display introduction.
    print(('=' * 20) + 'SET STATS' + ('=' * 21)) #Set stats title bar.
    player_stats, current_health = setPlayerStats() #Let user set their stats
    print('=' * 50) #Set stats end title bar.
    if intro_check == True:
        print(('=' * 20) + 'STORY' + ('=' * 20)) #Story Title bar.
        printStoryIntroduction() #Print story introduction.
        print('=' *45)#Story end title bar.
    print(('=' * 20) + 'WASTELAND' + ('=' * 21)) #Main game title bar.
    print('You are currently at the ' + location + '.') #Display location
    generateAllGameRewards() #Generate all game rewards.
    createArmourShop(armour_list) #Generates the armour shop
    createWeaponShop(weapon_list) #Generates the weapon shop
    createFoodShop(food_list) #Generates the food shop
    inventory = resetInventory(inventory, armour, weapon, items) #Initialize the player inventory.
    runMainLoop(user_input, user_quit, location, inventory, player_stats, current_health, money, exp) #Main game.
    print('=' * 50) #Main game end title bar.
        
        
