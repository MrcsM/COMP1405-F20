import time

#important info, lootboxes, prices and just a line for personal use
lootboxes = ['[Common] Tier 1 ($3.99)', '[Rare] Tier 2 ($5.99)', '[Legendary] Tier 3 ($7.99)', 'Complete Purchase']
prices = [3.99, 5.99, 7.99]
line = '------------------------------------'

#type of boxes and amounts
common = 0
rare = 0
legendary = 0

#start of shop, asking for name and asking for lootbox selection
print("Hello! Welcome to the Loot Box Purchasing System!\nBefore you buy any boxes, can you provide your name?")
user_name = input("Name: ")

print("\nHello {}! Please select the loot box below that you would like to purchase.".format(user_name))
time.sleep(0.5) #just a little delay (for personal sake)

#printing out all of the lootbox options
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
    if selection == "1" or selection == "2" or selection == "3" or selection == "4": #if its between 1 and 4, it'll stop the loop and continue
        if selection == "1" or selection == "2" or selection == "3": #checks to see if its a box or not
            print(" ")
            amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #since it is, it asks how many you want to purchase
            formatted_amount = amount
            print(" ")

            #checking if the input is an integer
            if amount.isdigit() == True:
                amount = int(amount) #this is
            else:
                amount = 0 #this isn't
                exit

            infinite2 = 1
            
            #another infinite loop to check if the amount is proper
            while infinite2 == 1:
                if int(amount) > 0: #proper so ends loop
                    infinite2 = 2
                else:
                    print("Invalid amount of loot boxes to purchase.")
                    amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #asks again since the amount wasn't proper

                    #checking if the input is an integer
                    if amount.isdigit() == True:
                        amount = int(amount) #this is
                    else:
                        amount = 0 #this isn't
                        exit
            
            #adds boxes to each variable depending on box chosen
            if selection == "1":
                common = common + int(amount)
            elif selection == "2":
                rare = rare + int(amount)
            elif selection == "3":
                legendary = legendary + int(amount)
            
            #then continues to ask what boxes they want to buy while still in the loop
            print("Please select the loot box below that you would like to purchase or select 4 to complete your purchase.")
            #continues to print loot boxes
            n = 1
            print(line)
            for x in lootboxes:
                print(" " + str(n) + ". " + x)
                n += 1
            print(line)

            #asking for selection while in loop
            selection = input("Selection: ")

        elif selection == "4": #this isn't a box, so it ends the infinite loop and goes to end
            infinite = 2
    else:
        #not a box or complete purchase
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

    input("{0}\nPress any key to exit.\n{0}".format(line))
else:
    #checks each and every box to see if there's any, if there are, it adds them in the right order, else, they dont show
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

    input("{0}\nPress any key to exit.\n{0}".format(line))