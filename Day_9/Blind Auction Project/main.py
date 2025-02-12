# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

silent_auction = {

}

def find_highest_bidder():
    max_bid = 0
    winner = ""
    for key in silent_auction:
        if silent_auction[key] > max_bid:
            max_bid = silent_auction[key]
            winner = key
    print(f"{winner} won with a bid of {max_bid}")

print(art.logo)

run = True
while run:
    name = input("Enter your name\n")
    bid = int(input("Enter your bid \n"))
    silent_auction[name] = bid
    run_again = input("Are there others to run? y for yes, n for no")
    if run_again == "n":
        run = False
        find_highest_bidder()
    else:
        print("\n" * 25)
