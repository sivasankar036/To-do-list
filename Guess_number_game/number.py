import random
import time

def get_player_name():
    name = input("May I ask you for your name? ")
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def play_game(number, name):
    guesses_taken = 0

    while guesses_taken < 6:
        try:
            guess = int(input("Guess: "))
            
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < number:
                    print("The guess of the number that you have entered is too low.")
                elif guess > number:
                    print("The guess of the number that you have entered is too high.")
                else:
                    print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                    return
                if guesses_taken < 6:
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("I don't think that is a number. Sorry.")
    
    print(f'Nope. The number I was thinking of was {number}.')

def main():
    play_again = "yes"
    
    while play_again.lower() in ["yes", "y"]:
        number = random.randint(1, 200)
        name = get_player_name()
        play_game(number, name)
        play_again = input("Do you want to play again? ")

if __name__ == "__main__":
    main()
