import time
import random

#important info, lootboxes, prices and just a line for personal use
lootboxes = ['[Common] Tier 1 ($3.99)', '[Rare] Tier 2 ($5.99)', '[Legendary] Tier 3 ($7.99)', 'Complete Purchase']
lootboxes_noprice = ['[Common] Tier 1', '[Rare] Tier 2', '[Legendary] Tier 3']
items = ['Stick', 'Rock', 'Water Bottle', 'Crossbow', 'Iron Chunk', 'Apple', 'Excalibur', "King's Crown", 'Diamond'] #in order, common x3, rare x3, legendary x3
prices = [3.99, 5.99, 7.99]
line = '------------------------------------'

#amount of boxes
common = 0
rare = 0
legendary = 0

#open box function, box is the type (in integer form) and amt is the amount
def open_box(box, amt):
    if box == 1 or box == 2 or box == 3: #checks if the box is correct
        print(line + "\nOpening " + str(amt) + "x " + lootboxes_noprice[int(box)-1] + "\n" + line) #sends message saying it's opening #x of lootbox
        time.sleep(1)
        if box == 1:
            #common probabiltiies
            prob_com = 0.8
            prob_rar = 0.95
            prob_leg = 1
        elif box == 2:
            #rare probabilities
            prob_com = 0.5
            prob_rar = 0.9
            prob_leg = 1
        elif box == 3:
            #legendary probabilities
            prob_com = 0.3
            prob_rar = 0.8
            prob_leg = 1
        #loops amount of boxes it needs to open, and opens them
        n = 1
        notsofinal_items = list()
        for i in range(amt):
            for i in range(3):
                prob = random.random() #gets a random float between 0 and 1 for probability
                #checks if probability is between each probability for rarity, then gets a random prize from the list and adds it to another list for items
                if prob < prob_com:
                    rand_prize = random.randint(0, 2)
                    notsofinal_items += [items[rand_prize] + ' (COMMON)']
                elif prob_com < prob < prob_rar:
                    rand_prize = random.randint(3, 5)
                    notsofinal_items += [items[rand_prize] + ' (RARE)']
                else:
                    rand_prize = random.randint(6, 8)
                    notsofinal_items += [items[rand_prize] + ' (LEGENDARY)']
            seperator = ", "
            final_items = seperator.join(notsofinal_items) #just to remove brackets and split the items with commas
            #displays all items the user got with their rarities
            print("Box #" + str(n) + ": You got " + str(final_items) +"!")
            n += 1 #adding 1 to n to tell the code that we can move on to the next box
            del(final_items, notsofinal_items) #deleting both the final variable and the beginning variable
            notsofinal_items = list() #setting the beginning variable back to a list
    else:
        print("Error! Failed to find the right loot box. Please try again later.") #this is just here for testing, but in reality if someone for some reason tries to put in anything other than 1, 2 or 3, it'll send the error and exit
        exit

#start of shop, asking for name and asking for lootbox selection
print("Hello! Welcome to the Loot Box Purchasing System!\nBefore you buy any boxes, can you provide your name?")
user_name = input("Name: ")

print("\nHello {}! Please select the loot box below that you would like to purchase.".format(user_name))
time.sleep(0.5) #just a little delay (for personal sake)

#printing out lootboxes
n = 1
print(line)
for x in lootboxes:
    print(" " + str(n) + ". " + x)
    n += 1
print(line)

#asking for selection
selection = input("Selection: ")

infinite = 1

#infinite loop to keep checking for the right selection
while infinite == 1:
    if selection == "1" or selection == "2" or selection == "3" or selection == "4": #if it's between 1 and 4, it'll stop the loop and continue
        if selection == "1" or selection == "2" or selection == "3": #checks to see if it's a box or not
            print(" ")
            amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #asks how many boxes the user wants to purchase
            formatted_amount = amount
            print(" ")

            #checks if the amount given is an integer
            if amount.isdigit() == True:
                amount = int(amount) #this is
            else:
                amount = 0 #this is not.
                exit

            infinite2 = 1
            
            #another infinite loop to check if the amount is proper
            while infinite2 == 1:
                if int(amount) > 0: #this is proper, ends
                    infinite2 = 2
                else:
                    print("Invalid amount of loot boxes to purchase.")
                    amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #isn't proper so it continues to ask

                    #checks if the amount given is an integer
                    if amount.isdigit() == True:
                        amount = int(amount) #this is
                    else:
                        amount = 0 #this is not.
                        exit
            
            #adds boxes to each variable depending on box chosen
            if selection == "1":
                common = common + int(amount)
            elif selection == "2":
                rare = rare + int(amount)
            elif selection == "3":
                legendary = legendary + int(amount)
            
            #continues to ask what box they want to purchase in loop
            print("Please select the loot box below that you would like to purchase or select 4 to complete your purchase.")
            n = 1
            print(line)
            for x in lootboxes:
                print(" " + str(n) + ". " + x)
                n += 1
            print(line)

            selection = input("Selection: ")

        elif selection == "4": #it's not a box, it's complete purchase so it exits the infinite loop
            infinite = 2
    else:
        #not a box or a complete purchase so it sends the error message and proceeds to ask again
        print("Error! You have not selected a valid loot box. Please enter a value between 1-3 to select a lootbox or 4 to complete your purchase.")
        print("Please select the loot box below that you would like to purchase.")

        n = 1
        print(line)
        for x in lootboxes:
            print(" " + str(n) + ". " + x)
            n += 1
        print(line)

        selection = input("Selection: ")

#end of loop since the user added the amount of boxes they wanted and completed purchase
print("\nThanks, {}! Here is your receipt:\n{}".format(user_name, line))
if common == 0 and rare == 0 and legendary == 0: #if there are no boxes added to cart, it shows nothing
    print("No items to display.")
    print(line)
    print("Total Cost: $0.00")
    print("Thank you! Have a wonderful day!\n")

    input("{0}\nYou bought no loot boxes meaning you have none to open!\nPress any key to exit.\n{0}".format(line)) #tells you to exit whenever since user purchased nothing
else:
    #checks each and every box to see if theres any, if there are, it adds them in the right order, else, they dont show
    if common > 0:
        print(str(common) + "x   " + lootboxes[0])
    if rare > 0:
        print(str(rare) + "x   " + lootboxes[1])
    if legendary > 0:
        print(str(legendary) + "x   " + lootboxes[2])
    print(line)

    #gets the price of each box, and then adds it all up at the end
    current_price_common = float(prices[0])
    current_price_rare = float(prices[1])
    current_price_legendary = float(prices[2])
    total_price = (int(common) * current_price_common) + (int(rare) * current_price_rare) + (int(legendary) * current_price_legendary)

    #prints cost, thats it
    print("Total Cost: ${0:.2f}".format(total_price))
    print("Thank you! Have a wonderful day!\n")

    #little delay before opening boxes
    time.sleep(0.5)

    #prints and tells user that boxes are going to get opened
    print("\nTime to open boxes!")
    #checks all rarities and sees if there are any boxes of that rarity and opens them if there are
    if common > 0:
        open_box(1, common)
    if rare > 0: 
        open_box(2, rare)
    if legendary > 0: 
        open_box(3, legendary)

    #after it opens all the boxes, it will tell the user that they can look over their items and press any key to exit.
    input(line + line + "\nOnce you have finished looking over your items, press any key to exit.\n" + line + line)





