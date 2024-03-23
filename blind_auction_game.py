import os 
from art import logo
print(logo)
bids={}

def highest_bidder(bidding_record):
    highest_bid=0
    winner=''
    for bidding in bidding_record:
        current_bid=bids[bidding]
        if current_bid>highest_bid:
            highest_bid=current_bid
            winner=bidding
    print(f"The winner is {winner} with bid of {highest_bid}")

auction_finish=False
while not auction_finish:
    user= input("Enter Your Name :")
    bid=int(input("Enter Bid Amount:"))
    bids[user]=bid
    bid_continue=input("Any One Else Want to Bid Type 'yes' or 'no':")
    if bid_continue=='no':
        auction_finish=True
        os.system("CLS")
        highest_bidder(bids)
    elif bid_continue=='yes':
        os.system("CLS")
