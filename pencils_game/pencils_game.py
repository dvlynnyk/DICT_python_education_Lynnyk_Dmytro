import random

def read_pencils_valid():
    """
    Read and validate the initial number of pencils.

    The function requests input from the user until the value is:
    - numeric (digits only)
    - positive (> 0)

    Returns:
        int: Validated positive number of pencils.
    """
    while True:
        raw = input("How many pencils would you like to use:\n> ")
        if not raw.isdigit():
            print("The number of pencils should be numeric")
            continue
        n = int(raw)
        if n <= 0:
            print("The number of pencils should be positive")
            continue
        return n

def read_first_player_valid():
    """
    Ask the user to choose the first player.

    Only two names are allowed: 'John' or 'Jack'.
    The function keeps asking until a valid name is entered.

    Returns:
        str: Either 'John' or 'Jack'.
    """
    valid = ("John", "Jack")
    while True:
        name = input("Who will be the first (John, Jack):\n> ")
        if name not in valid:
            print("Choose between 'John' and 'Jack'")
            continue
        return name

def read_move_valid(pencils, player):
    """
    Read and validate the human player's move.

    Rules:
    - the move must be one of: '1', '2', '3'
    - the move must not exceed the number of remaining pencils

    Args:
        pencils (int): Number of pencils currently on the table.
        player (str): The name of the current player.

    Returns:
        int: Validated number of pencils the player takes (1–3).
    """
    while True:
        raw = input(f"{player}'s turn:\n> ")
        if raw not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        taken = int(raw)
        if taken > pencils:
            print("Too many pencils were taken")
            continue
        return taken

def bot_move(pencils):
    """
    Compute the bot's move according to the optimal game strategy.

    Strategy:
        - If the current number of pencils N satisfies N % 4 == 1,
          this is a losing position for the bot, so it chooses randomly.
        - Otherwise, the bot takes enough pencils to force the opponent
          into a losing position (i.e., a state where remaining % 4 == 1).

    Args:
        pencils (int): Current number of pencils on the table.

    Returns:
        int: Number of pencils the bot takes (1–3), limited by remaining pencils.
    """
    if pencils % 4 == 1:
        choice = random.randint(1, 3)
        return min(choice, pencils)

    if pencils % 4 == 0:
        return min(3, pencils)
    if pencils % 4 == 3:
        return min(2, pencils)

    # covers pencils % 4 == 2
    return min(1, pencils)

def main():
    """
    Run the main game loop for the Pencil Game.

    This function:
        - Reads and validates the starting number of pencils.
        - Determines who plays first.
        - Alternates turns between 'John' (human) and 'Jack' (bot).
        - Applies validation to human moves.
        - Executes optimal strategy for the bot.
        - Prints the winner when all pencils are taken.
    """
    pencils = read_pencils_valid()
    first = read_first_player_valid()

    players = ["John", "Jack"]
    turn = 0 if first == players[0] else 1

    while pencils > 0:
        print("|" * pencils)
        current = players[turn % 2]

        if current == "Jack":
            print("Jack's turn:")
            taken = bot_move(pencils)
            print(taken)
        else:
            taken = read_move_valid(pencils, current)

        pencils -= taken

        if pencils == 0:
            winner = players[(turn + 1) % 2]
            print(f"{winner} won!")
            break

        turn += 1

if __name__ == "__main__":
    main()
