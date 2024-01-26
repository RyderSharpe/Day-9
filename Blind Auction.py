from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo

bidders = True
bidders_list = []

while bidders:

    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))  # Convert bid to float

    bid_dict = {}
    bid_dict['name'] = name
    bid_dict['bid'] = bid
    bidders_list.append(bid_dict)
    print(bid_dict)
    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if bidders == 'yes':
        clear()
    else:
        winner = max(bidders_list, key=lambda x: x['bid'])
        # winner = max(bid_dict, key=bid_dict.get)
        bidders = False

# print(bidders_list)
# print(winner)
print(f"The winner is {winner['name']} with a bid of ${winner['bid']}")
