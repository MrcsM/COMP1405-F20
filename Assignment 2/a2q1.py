import time

#important info, lootboxes, prices and just a line for personal use
lootboxes = ['[Common] Tier 1 ($3.99)', '[Rare] Tier 2 ($5.99)', '[Legendary] Tier 3 ($7.99)']
prices = [3.99, 5.99, 7.99]
line = '------------------------------------'

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
    if selection == "1" or selection == "2" or selection == "3": #if its between 1 and 3, it'll stop the loop and continue
        infinite = 2
    else:
        print("Error! You have not selected a valid loot box. Please enter a value between 1-3 to select.") #else, it'll continue to ask until it gets the right values
        print("Please select the loot box below that you would like to purchase.")

        n = 1
        print(line)
        for x in lootboxes:
            print(" " + str(n) + ". " + x)
            n += 1
        print(line)

        selection = input("Selection: ")

#outside of the loop, meaning the user chose a box
print(" ")
amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #asking how many boxes they want to purchase
formatted_amount = amount
print(" ")

#checking if the input is an integer
if amount.isdigit() == True:
    amount = int(amount) #this is
else:
    amount = 0 #this is not
    exit

infinite = 1

#another infinite loop to check and see if the amount is correct
while infinite == 1:
    if int(amount) > 0: #ends loop if the amount is greater than 0
        infinite = 2
    else:
        print("Invalid amount of loot boxes to purchase.")
        amount = input("How many " + lootboxes[int(selection)-1] + " Would you like to purchase today?\nAmount: ") #else, it continues to ask
        formatted_amount = amount

        if amount.isdigit() == True:
            amount = int(amount)
        else:
            amount = 0
            exit

#prints receipt with amount of boxes they bought
print("Thanks {}! Here is your receipt:\n{}".format(user_name, line))
print(" " + formatted_amount + "x   " + lootboxes[int(selection)-1] + "\n{0}".format(line))

#calculating price
current_price = float(prices[int(selection)-1])
total_price = int(amount) * current_price

#printing price
print("Total Cost: ${0:.2f}".format(total_price))
print("Thank you! Have a wonderful day!\n")

#way to exit shop without it closing immediately after the receipt is printed
input("{0}\nPress any key to exit.\n{0}".format(line))
