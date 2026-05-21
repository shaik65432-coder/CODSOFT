import math

# Create board
board = [" " for _ in range(9)]


# Display board
def print_board():
    print()

    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")

        if i < 6:
            print("---|---|---")

    print()


# Check winner
def check_winner(player):

    win_positions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for position in win_positions:

        if all(board[i] == player for i in position):
            return True

    return False


# Check draw
def is_draw():
    return " " not in board


# Human move
def human_move():

    while True:

        try:
            move = int(input("Enter position (1-9): ")) - 1

            if move >= 0 and move < 9 and board[move] == " ":
                board[move] = "X"
                break

            else:
                print("Invalid move. Try again.")

        except:
            print("Enter a valid number.")


# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


# AI move
def ai_move():

    best_score = -math.inf
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main game loop
print("=== TIC TAC TOE AI ===")
print("You are X")
print("AI is O")

while True:

    print_board()

    human_move()

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print_board()
        print("Match Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if is_draw():
        print_board()
        print("Match Draw!")
        break