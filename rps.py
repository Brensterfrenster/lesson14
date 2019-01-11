import random

print("Rock paper scissors says shoot")
user_pick = input("User has to pick: ")
c_pick = random.choice(["Rock", "Paper", "Scissors"])

print('User picked: ' + user_pick)
print('Computer picked: ' + c_pick)

if user_pick== "Scissors" and c_pick=="Scissors":
	print("You tied, both picked scissors.")
elif user_pick== "Rock" and c_pick=="Scissors":
	print("You win, rock breaks scissors.")
elif user_pick== "Paper" and c_pick=="Scissors":
	print("You lose, scissors cuts paper.")

elif user_pick== "Paper" and c_pick=="Rock":
	print("You win, paper covers rock.")
elif user_pick== "Paper" and c_pick=="Paper":
	print("You tied, both picked paper.")
elif user_pick== "Rock" and c_pick=="Rock":
	print("You tied, both picked rock.")
elif user_pick== "Scissors" and c_pick=="Rock":
	print("You lose, rock breaks scissors.")
elif user_pick== "Scissors" and c_pick=="Paper":
	print("You win, scissors cuts paper.")
elif user_pick== "Rock" and c_pick=="Paper":
	print("You lose, paper covers rock.")