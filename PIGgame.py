import random

def roll():
    roll=random.randint(1,6)
    return roll

while True:
    players=input("How many players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Players must be between 2-4.")
    else:
        print("Invalid. Try again.")

max_score=50
players_scores=[0 for i in range(players)]

while max(players_scores)<max_score:
    for player_index in range(players):
        print(f"Player No {player_index+1} its your turn.")
        print(f"Your current score is {players_scores[player_index]}")
        c_score=0
        while True:
            should_roll=input("You will only get one chance so type carefully.\n" \
            "Do you want to roll the dice (y/n): ")
            if should_roll!="y":
                break
            value=roll()
            if value==1:
                print("You rolled a 1. Your turn is over")
                players_scores[player_index]=0
                c_score=0
                break
            else:
                c_score+=value
                print(f"You rolled a {value}")
            print(f"Your score is {c_score}")
        players_scores[player_index]+=c_score
        print(f"Your total score is {players_scores[player_index]}")
max_score=max(players_scores)
winner_index=players_scores.index(max_score)
print(f"Player no {player_index+1} won the game with a score of {max_score}")