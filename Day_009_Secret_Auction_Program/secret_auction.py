import os

# Auction logo for display at the start of the program
logo = '''
           _
          ( )
   ___   _(_)_
  / __| (_) (_)
 | (__   _  _
  \___| (_) (_)
           (_)
'''

# Dictionary to store all the bids. Key: bidder's name, Value: bid amount.
bids = {}
# Flag to control the bidding process loop.
bidding_finished = False

# Function to find the highest bidder from the 'bids' dictionary.
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    # Iterate through each bidder in the dictionary.
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        # If the current bid amount is greater than the highest_bid found so far,
        # update highest_bid and set the current bidder as the winner.
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    # Print the winner and their winning bid.
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo)
print("Welcome to the secret auction program.")

# Loop to collect bids until no more bidders are present.
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    # Add the bidder's name and bid to the 'bids' dictionary.
    bids[name] = price
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # If there are no more bidders, set bidding_finished to True to exit the loop.
    if other_bidders == "no":
        bidding_finished = True
        # Call the function to determine and print the winner.
        find_highest_bidder(bids)
    elif other_bidders == "yes":
        # Clear the console screen for the next bidder.
        # 'cls' for Windows, 'clear' for Linux/macOS.
        # Note: This command might not work in all integrated development environments or web-based consoles.
        os.system('cls' if os.name == 'nt' else 'clear')

