class CoffeeMachine:
    """
    A coffee machine simulator that processes user input based on its current state.
    """

    def __init__(self):
        """
        Initialize the coffee machine with default resources and state.
        """
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"

    def print_state(self):
        """
        Print the current resources of the coffee machine.
        """
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def process_input(self, user_input):
        """
        Process a single line of user input according to the current state.

        Args:
            user_input (str): Input provided by the user.
        """
        if self.state == "action":
            if user_input == "buy":
                self.state = "buy"
                print(
                    "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:"
                )
            elif user_input == "fill":
                self.state = "fill_water"
                print("Write how many ml of water you want to add:")
            elif user_input == "take":
                print(f"I gave you {self.money}")
                self.money = 0
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "exit":
                return False

        elif self.state == "buy":
            if user_input == "back":
                self.state = "action"
                return True

            recipes = {
                "1": (250, 0, 16, 4),
                "2": (350, 75, 20, 7),
                "3": (200, 100, 12, 6),
            }

            water, milk, beans, price = recipes[user_input]

            if self.water < water:
                print("Sorry, not enough water!")
            elif self.milk < milk:
                print("Sorry, not enough milk!")
            elif self.beans < beans:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= water
                self.milk -= milk
                self.beans -= beans
                self.cups -= 1
                self.money += price

            self.state = "action"

        elif self.state == "fill_water":
            self.water += int(user_input)
            self.state = "fill_milk"
            print("Write how many ml of milk you want to add:")

        elif self.state == "fill_milk":
            self.milk += int(user_input)
            self.state = "fill_beans"
            print("Write how many grams of coffee beans you want to add:")

        elif self.state == "fill_beans":
            self.beans += int(user_input)
            self.state = "fill_cups"
            print("Write how many disposable cups of coffee you want to add:")

        elif self.state == "fill_cups":
            self.cups += int(user_input)
            self.state = "action"

        return True


def main():
    """
    Run the coffee machine using the CoffeeMachine class.
    """
    machine = CoffeeMachine()

    while True:
        if machine.state == "action":
            user_input = input("Write action (buy, fill, take, remaining, exit):\n> ")
        else:
            user_input = input("> ")

        if not machine.process_input(user_input):
            break



if __name__ == "__main__":
    main()
