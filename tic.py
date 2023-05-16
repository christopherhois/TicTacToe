def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    """
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_winner(board):
    """
    Checks if there's a winner and returns the symbol of the winner ('X' or 'O') if there is one.
    If there's no winner yet, returns None.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]

    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def tic_tac_toe():
    """
    Runs a game of Tic Tac Toe.
    """
    # Initialize the board
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    current_player = 'X'

    # Game loop
    while True:
        # Print the board
        print_board(board)

        # Get the current player's move
        print(f"Player {current_player}, it's your turn.")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] != ' ':
            print("Invalid move. That spot is already taken.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for a tie
        if all([spot != ' ' for row in board for spot in row]):
            print_board(board)
            print("Tie game!")
            break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ == '__main__':
    tic_tac_toe()