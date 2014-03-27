## Christopher Gilles
## Started 24 March 2014

## Verison 2.0

## TODO:
## User def turns - DONE (.1) 
## User def size - DONE (.1)
## Rework main / split to main/menu and initalization functs - DONE (.1)

## 'Unlimited turns' (limit = possible positions)
##  Multiple ships (size = 1), user def (1) - NEEDS TESTING
##    - overhaul ship creation funct (will make replay easier) NEEDS TESTING
##       - remove from init / new funct DONE
##    - make overlap preventer funct - NEEDS TESTING
##    - overhaul hit dection funct - NEEDS TESTING

##  multiplayer (2p) (1)
##      - single pool of targets
##      - teams of targets
##  adative ship num (.5)
##  multi length ships
##  special weapons
##  hide/find bonuses
##  score system

##  Ships as class/objects

##  Graphical Interface



from random import randint

# This makes the board. User defined size. Replay will prob need default size in argument eg(x=5)
def make_board(x):
    board = []
    for a in range(x):
        board.append(["O"] * x)
    return board

# Prints the board with no formatting
def print_board(board):
    for row in board:
        print(" ".join(row))

# Generates random ship cordinates [row,col] // will be removed/overhauled with multiship
def random_pos(board):
    return [randint(0, len(board) - 1), randint(0, len(board) - 1)]
    None

# Makes list of n ships
def ship_maker(n):
    ships = []
    for a in range(n):
        ships.append(['',''])
    return ships

# Checks to prevent overlap of ships    
def pos_assigner(ships, board):
    for ns in range(len(ships)):
        print(range(len(ships)))
        print(ns)
        if ns == 0:
            ships[ns][0] = random_pos(board)[0]
            ships[ns][1] = random_pos(board)[1]
            print(ships)
            print()

        elif ships.count(ships[ns]) > 1:
            while ships.count(ships[ns]) > 1:
                ships[ns][0] = random_pos(board)[0]
                ships[ns][1] = random_pos(board)[1]
        else:
            ships[ns][0] = random_pos(board)[0]
            ships[ns][1] = random_pos(board)[1]


    return ships        

# Game option initalizer
def init():
    print()
    dim = input("What size board would you like? (default = 5): ")
    if dim == '':
        dim = 5
    else:
        dim = int(dim)

    n =  input("How many ships do you want?: (default = 1) ")
    if n == '':
        n = 1
    else:
        n = int(n)

    turns = input("How many turns do you want to play? (default = 4): ")
    if turns == '':
        turns = 4
    else:
        turns = int(turns)
    # Starts the game (creates board and 1 random single len ship prior)
    board = make_board(dim)
    #ship_row = random_pos(board)[0]
    #ship_col = random_pos(board)[1]
    ships = pos_assigner(ship_maker(n), board)
    
    game(board, turns, ships)

def target(guess, targets):
    for i in range(len(targets)):
        if guess[0] == targets[i][0] and guess[1] == targets[i][1]:
            return True # User hit an enemy ship
        else:
            a = 1 # Pointless placeholder to keep loop cycling.
    return False

# Actual game play code
def game(board, turns, ships):
    #print(ship_row + 1, ship_col + 1) # rework for multi ships
    print(ships)
    print("Turn 1")
    print_board(board)
    print()
    guess = ['','']
    for turn in range(turns):
        guess[0] = int(input("Guess Row:")) - 1
        guess[1] = int(input("Guess Col:")) - 1
        print()

        if target(guess, ships):
            print("Congratulations! You sunk a battleship!")
            board[guess[0]][guess[1]] = '$'
            ships.remove(guess)
            if len(ships) == 0:
                print("You destoyed all the enemies!!")
                print("YOU WIN!!")
                break
        else:
            # Out of bounds
            if (guess[0] < 0 or guess[0] > (len(board) - 1)) or (guess[1] < 0 or guess[1] > (len(board) - 1)): 
                print("Oops, that's not even in the ocean.")
                print()
            # Already guessed cords
            elif(board[guess[0]][guess[1]] == "X"):
                print("You guessed that one already.")
                print()
            # Normal Miss
            else:
                print("You missed my battleship!")
                board[guess[0]][guess[1]] = "X"
                print()
        # Ends game after turn limit
        if turn == turns - 1:
            print("No More Turns Left")
            print("Game Over")
            break
        print ("Turn", turn + 2)
        print_board(board)

# Main Menu
def main():
    print("Hello user. Welcome to BATTLESHIP!!")
    print()
    print("MAIN MENU")
    print("--------------")
    print("1) Play game")
    print("2) Credits")
    print()
    choice = int(input("Please choose an option: "))
    if choice == 1: # Launches game starter
        init()
    elif choice == 2: # Credits
        print()
        print("Game created by Christopher Gilles")
        main()








