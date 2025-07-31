bidders = {}

process = True

name = str(input("What is Your Name: "))
amount = int(input("How much do you want to bid: "))

bidders[name] = amount

while process:
    option = int(input("Is there any othe bidder?\n 1)Yes\n 2)No\n "))
    if option == 2:
        process = False
    elif option == 1:
        name = str(input("What is Your Name: "))
        amount = int(input("How much do you want to bid: "))
        bidders[name] = amount
    else:
        print("Invalid Option")

maximum = 0
winners = [0, 'No Bid']
for bidder in bidders:
    if bidders[bidder] > winners[0]:
        winners[0] = bidders[bidder]
        winners[1] = bidder
    elif bidders[bidder] == winners[0]:
        winners[1] += f" And {bidder}"
    else:
        pass
print(f"The Winner(s) is/are {winners[1]} \n And The Amount is {winners[0]}")
