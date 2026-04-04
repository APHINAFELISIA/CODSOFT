import math

# Board representation
board = [" " for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(b):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # cols
        [0,4,8],[2,4,6]           # diagonals
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] and b[cond[0]] != " ":
            return b[cond[0]]
    return None

# Check if board is full
def is_full(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    winner = check_winner(b)
    
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def best_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "X"

# Human move
def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "O"
                break
            else:
                print("Position already taken!")
        except:
            print("Invalid input! Try again.")

# Game loop
def play_game():
    print("Tic-Tac-Toe: You (O) vs AI (X)")
    print("Positions are numbered 1 to 9\n")
    
    print_board()
    
    while True:
        player_move()
        print_board()

        if check_winner(board) == "O":
            print("You win!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        best_move()
        print_board()

        if check_winner(board) == "X":
            print("AI wins!")
            break
        elif is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()