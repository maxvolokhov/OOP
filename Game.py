import random
import time


class GuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.highscore = float('inf')

    def __str__(self):
        return "Guessing Game"

    def __repr__(self):
        return f"GuessingGame(secret_number={self.secret_number}, attempts={self.attempts})"

    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def show_highscore(self):
        if self.highscore == float('inf'):
            print("No highscore recorded yet.")
        else:
            print(f"The current highscore is: {self.highscore} attempts.")

    def play(self):
        while True:
            guess = int(input("Take a guess: "))
            self.attempts += 1

            if guess < self.secret_number:
                print("Too low! Try again.")
            elif guess > self.secret_number:
                print("Too high! Try again.")
            else:
                if self.attempts < self.highscore:
                    self.highscore = self.attempts
                print(f"Congratulations! You guessed the number in {self.attempts} attempts!")
                break

    def start_game(self):
        print("Welcome to the Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            print("\n1. Play Game")
            print("2. Restart Game")
            print("3. Show Highscore")
            print("4. Quit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.play()
            elif choice == 2:
                self.restart_game()
                print("Game restarted.")
            elif choice == 3:
                self.show_highscore()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")

        print("Goodbye!")


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Game duration: {duration:.2f} seconds")
        return result

    return wrapper


if __name__ == '__main__':
    game = GuessingGame()
    game.start_game()
