import objets 
selection1 = "PLAYER 1 \n SELECT: \n 1 - Rock \n 2 - Paper \n 3 - Scissors"
selection2 = "PLAYER 2 \n SELECT: \n 1 - Rock \n 2 - Paper \n 3 - Scissors"


# SELECTION 1

player1 =  objets.player()
print(selection1)
player1.pick_piece(int(input()))

# SELECTION 2

player2 =  objets.player()
print(selection2)
player2.pick_piece(int(input()))
   


# WHEN THE GAME IS DRAW

if player1.choice == player2.choice:
    player1.status = "draw"
    player2.status = "draw"
    print("This game is draw")

#WHEN THE GAME IS NOT DRAW

else:

# WHEN THE WINNER IS PLAYER 1: 

        if player2.choice == "rock" and player1.choice == "paper":
            player1.status = "winner"
            player2.status = "loser"
            print("The winner is Player 1")

        elif player2.choice == "scissors" and player1.choice == "rock":
            player1.status = "winner"
            player2.status = "loser"
            print("The winner is Player 1")

        elif player2.choice == "paper" and player1.choice == "scissors":
            player1.status = "winner"
            player2.status = "loser"
            print("The winner is Player 1")

# WHEN THE WINNER IS PLAYER 2:

        elif player1.choice == "rock" and player2.choice == "paper":
            player2.status = "winner"
            player1.status = "loser"
            print("The winner is Player 2")

        elif player1.choice == "scissors" and player2.choice == "rock":
            player2.status = "winner"
            player1.status = "loser"
            print("The winner is Player 2")

        elif player1.choice == "paper" and player2.choice == "scissors":
            player2.status = "winner"
            player1.status = "loser"
            print("The winner is Player 2")