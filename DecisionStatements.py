#How many votes did you get?
my_votes = int(input("How many votes did you get in the election?"))
#How many votes were there
total_votes = int(input("What is the total votes in the election?"))
# Calculate the percentage of votes you received
percentage_votes = (my_votes/total_votes)*100
if percentage_votes>50:
    print("You won")
elif percentage_votes<50:
    print("You lose")    
