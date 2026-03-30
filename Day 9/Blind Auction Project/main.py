from art import logo
print(logo)

bid_over = False
while not bid_over:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if more_bidders == "yes":
        print("\n" * 200)
    else:
        bid_over = True

    bidder_data = {
        name: bid,
    }

    best_pair = max(bidder_data.items())
    print(f"The winner is {best_pair[0]} with a bid of ${best_pair[1]}")