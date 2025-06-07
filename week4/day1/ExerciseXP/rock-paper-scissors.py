from game import Game
logo = """

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

"""

print(logo)
print("Welcome to a game of Rock, Paper, Scissors!")


def get_user_menu_choice():
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")

    choice = input("Please enter your choice (1-3): ")
    if choice in ['1', '2', '3']:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return None


def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results.get('win', 0)}")
    print(f'Losses: {results.get('loss', 0)}')
    print(f'Draws: {results.get('draw', 0)}')
    print("Thanks for playing!")


def main():
    results = {'win': 0, 'loss': 0, 'draw': 0, 'total': 0}

    while True:
        choice = get_user_menu_choice()
        if not choice:
            continue

        if choice == '1':
            game = Game()
            result = game.play()
            if result in results:
                results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == '3':
            print_results(results)
            break


if __name__ == "__main__":
    main()
