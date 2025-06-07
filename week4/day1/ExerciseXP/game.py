import random


class Game:
    def get_user_item(self):
        valid_items = ['1', '2', '3']
        item_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        while True:
            user_input = input(
                "Choose rock(1), paper(2) or scissors(3): ").lower()
            if user_input in valid_items:
                return item_map[user_input]
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == 'rock' and computer_item == 'scissors') or
            (user_item == 'paper' and computer_item == 'rock') or
            (user_item == 'scissors' and computer_item == 'paper')
        ):
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(
            f'You selected {user_item} The computer selected {computer_item}.')
        if result == 'draw':
            print("It's a draw!")
        elif result == 'win':
            print("You win!")
        else:
            print("You lose!")

        return result
