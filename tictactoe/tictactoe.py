def print_board(board):
    """
    Print the Tic Tac Toe board.

    Parameters:
        board (List[List[str]]): 3x3 board containing 'X', 'O', or '_'.
    """
    print("-" * 9)
    for row in board:
        print("|", " ".join(row), "|")
    print("-" * 9)

def board_from_string(cells: str):
    """
    Convert a 9-character string into a 3x3 board.

    Parameters:
        cells (str): String of length 9 containing 'X', 'O', or '_'.

    Returns:
        List[List[str]]: 3x3 board.
    """
    if len(cells) != 9 or any(c not in "XO_" for c in cells):
        raise ValueError("Input must be 9 characters containing only X, O, _")
    return [list(cells[i*3:(i+1)*3]) for i in range(3)]

def analyze_board(board):
    """
    Analyze the current board and return the game state.

    Parameters:
        board (List[List[str]]): 3x3 Tic Tac Toe board.

    Returns:
        str: Game state. One of:
            - "X wins"
            - "O wins"
            - "Draw"
            - "Game not finished"
            - "Impossible"
    """
    lines = []

    # Rows and columns
    for i in range(3):
        lines.append(board[i])  # row
        lines.append([board[0][i], board[1][i], board[2][i]])  # column

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    flat = [c for row in board for c in row]
    x_count = flat.count("X")
    o_count = flat.count("O")
    empty_count = flat.count("_")

    x_wins = any(line == ["X", "X", "X"] for line in lines)
    o_wins = any(line == ["O", "O", "O"] for line in lines)

    if x_wins and o_wins:
        return "Impossible"
    if abs(x_count - o_count) >= 2:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"
    if empty_count > 0:
        return "Game not finished"
    return "Draw"

def get_move(board, player):
    """
    Prompt the player for a move and validate input.

    Parameters:
        board (List[List[str]]): Current 3x3 board.
        player (str): "X" or "O"

    Returns:
        Tuple[int, int]: (row_index, col_index)
    """
    while True:
        move = input(f"{player} turn. Enter the coordinates: ").replace(" ", "")
        if len(move) != 2 or not move.isdigit():
            print("You should enter numbers!")
            continue

        x, y = int(move[0]), int(move[1])
        if not (1 <= x <= 3 and 1 <= y <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        # Map to board indices: (1,1) → top-left → board[0][0]
        row, col = x - 1, y - 1
        if board[row][col] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        return row, col

def play_game():
    """
    Run a single Tic Tac Toe game between two players.
    """

    board = [["_"] * 3 for _ in range(3)]
    print_board(board)
    players = ["X", "O"]
    turn = 0

    while True:
        current_player = players[turn % 2]
        row, col = get_move(board, f"Player {turn % 2 + 1}")
        board[row][col] = current_player
        print_board(board)
        state = analyze_board(board)
        if state != "Game not finished":
            print(state)
            break
        turn += 1

def main():
    """
    Main loop to start new games or exit.
    """
    while True:
        action = input("Type 'play' to start a new game or 'exit' to quit: ").lower()
        if action == "play":
            play_game()
        elif action == "exit":
            break
        else:
            print("Invalid input! Type 'play' or 'exit'.")

if __name__ == "__main__":
    main()
