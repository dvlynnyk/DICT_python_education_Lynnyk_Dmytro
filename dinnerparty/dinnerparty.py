import random

def create_friends_list():
    """
    Prompt the user for the number of friends and their names.
    
    Returns:
        dict or None: Dictionary with names as keys and 0 as initial balance.
                      Returns None if number of friends is invalid (<=0).
    """
    num = int(input("Enter the number of friends joining (including you):\n> "))
    if num <= 0:
        print("No one is joining for the party")
        return None

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num):
        name = input("> ")
        friends[name] = 0

    return friends

def split_bill_evenly(friends):
    """
    Divide the total bill evenly among all friends.

    Parameters:
        friends (dict): Dictionary of names with initial balance.

    Returns:
        tuple: Updated dictionary with calculated shares, and total bill amount.
    """
    total_amount = int(input("Enter the total amount:\n> "))
    split_amount = round(total_amount / len(friends), 2)

    for name in friends:
        friends[name] = split_amount

    return friends, total_amount

def choose_lucky_one(friends):
    """
    Ask the user if they want to select a lucky person.
    The lucky person pays 0; others share the cost.

    Returns:
        str or None: Name of lucky person, or None if skipped.
    """
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n> ')
    if answer.lower() == "yes":  # case-insensitive comparison
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        return lucky_one

    print("No one is going to be lucky")
    return None

def recalculate_with_lucky(friends, total_amount, lucky_one):
    """
    Recalculate each person's share if someone is lucky and pays nothing.

    Parameters:
        friends (dict): Original dictionary of friends.
        total_amount (int): Total bill amount.
        lucky_one (str): Name of the lucky person.

    Returns:
        dict: Updated dictionary with the lucky person paying 0.
    """
    if lucky_one is None:
        return friends  # No change if no lucky one

    new_split_amount = round(total_amount / (len(friends) - 1), 2)
    for person in friends:
        friends[person] = new_split_amount
    friends[lucky_one] = 0
    return friends

def main():
    """
    The main function on program.
    Controls the flow:
    1. Create friends list
    2. Split bill evenly
    3. Optionally choose a lucky one
    4. Recalculate the bill
    5. Display final dictionary
    """

    friends = create_friends_list()

    if friends is not None:
        friends, total_amount = split_bill_evenly(friends)
        lucky = choose_lucky_one(friends)

        if lucky is not None:
            friends = recalculate_with_lucky(friends, total_amount, lucky)

        print(friends)

if __name__ == "__main__":
    main()
