import time
import random
import sys
import re

def introduction():
    print("Welcome to the High School Musical Adventure!")
    time.sleep(1)
    print("You are a student at East High School, and the school is buzzing with excitement for the winter musical.")
    time.sleep(1)
    print("You can choose to focus on your studies and science club (1), audition for the musical (2), or try out for the basketball team (3).")

def make_choice():
    choice = input("Enter your choice (1, 2, or 3): ")
    return choice

def focus_on_studies():
    print("You've decided to focus on your studies and join the science club.")
    time.sleep(1)
    print("While you excel academically, you miss out on the excitement of the musical and the basketball team.")
    time.sleep(1)
    print("The musical is a success, and you have a great time in the science club, but you wonder about the paths not taken.")

def audition_for_musical():
    print("You've decided to audition for the winter musical, 'High School Musical'!")
    time.sleep(1)
    print("The auditions are coming up, and you need to choose a song to perform.")
    time.sleep(1)
    print("Do you perform 'Start of Something New' (1), 'Get'cha Head in the Game' (2), or 'Breaking Free' (3)?")
    choice = make_choice()

    if choice == '1':
        perform_song('Start of Something New', 'Troy', 'Gabriella')
    elif choice == '2':
        perform_song('Get\'cha Head in the Game', 'Basketball Team')
    elif choice == '3':
        perform_song('Breaking Free', 'Troy', 'Gabriella')

def perform_song(song, *characters):
    print(f"You've chosen to perform '{song}'!")
    time.sleep(1)
    print(f"Get ready to impress the audience with your performance as {' and '.join(characters)}!")
    time.sleep(1)
    print("Let's play the song performance mini-game!")

    score = song_performance_mini_game(song)
    print(f"Your performance score for '{song}' is {score}/10!")

    if score >= 9:
        print("Congratulations! You stole the show with your incredible performance.")
    else:
        print("While not perfect, your performance was still impressive. Keep practicing for the big night!")

def song_performance_mini_game(song):
    print("Complete the lyrics by typing the correct word when prompted.")
    time.sleep(1)

    lyrics = load_lyrics(f"{song.lower().replace(' ', '_')}_lyrics.txt")

    correct_words = 0
    total_words = len(lyrics)
    start_index = random.randint(0, total_words - 5)

    for word in lyrics[start_index:start_index + 4]:
        print(word, end=' ')

    for _ in range(3):
        user_input = input("\nEnter the next line: ")
        expected_input = ' '.join(lyrics[start_index + 4:start_index + 8]).lower().strip()

        if user_input.lower().strip() == expected_input:
            print("Correct!")
            correct_words += 4
            break
        else:
            print("Wrong! Try again.")

    return (correct_words / total_words) * 10  # Convert to a score out of 10

def load_lyrics(file_path):
    with open(file_path, 'r') as file:
        lyrics = re.findall(r'\b\w+\b', file.read())
    return lyrics

def try_out_for_basketball():
    print("You've decided to try out for the basketball team, Wildcats!")
    time.sleep(1)
    print("The tryouts are intense, and you need to showcase your basketball skills.")
    time.sleep(1)
    print("Do you want to practice shooting hoops before tryouts? (yes/no)")
    practice_choice = input().lower()

    if practice_choice == 'yes':
        print("Let's practice your shooting skills!")
        time.sleep(1)
        practice_basketball_mini_game()

    print("Now, it's time for the actual tryouts.")
    time.sleep(1)
    print("Let's play the basketball mini-game!")

    # If the player practiced, adjust the success rate for the actual tryouts
    success_rate = 0.7 if practice_choice == 'yes' else 0.5
    score = basketball_mini_game(success_rate)
    print(f"Your basketball skills score is {score}/10!")

    if score >= 8:
        print("Congratulations! You made the team and are ready to dominate on the court.")
    else:
        print("While not perfect, your performance was still solid. Keep practicing for the big games!")

def basketball_mini_game(success_rate):
    print("You have 10 attempts to make as many baskets as you can.")
    time.sleep(1)

    baskets_made = 0
    for _ in range(10):
        print("Get ready to shoot! Press 'Enter' to shoot.")
        input()

        if random.random() < success_rate:
            print("Swish! You made the basket!")
            baskets_made += 1
        else:
            print("Oops! You missed the basket.")

    return (baskets_made / 10) * 10  # Convert to a score out of 10

def practice_basketball_mini_game():
    print("You have 5 attempts to practice your shooting skills.")
    time.sleep(1)

    for _ in range(5):
        print("Get ready to shoot! Press 'Enter' to shoot.")
        input()

        if random.random() < 0.5:  # 50% chance of making a basket during practice
            print("Nice shot! You made the basket!")
        else:
            print("Oops! You missed the basket.")

def practice_singing():
    print("You've decided to practice your singing skills.")
    time.sleep(1)
    print("Do you want to practice singing 'Start of Something New' (1), 'Get'cha Head in the Game' (2), or 'Breaking Free' (3)?")
    choice = make_choice()

    if choice == '1':
        practice_song('Start of Something New', 'Troy', 'Gabriella')
    elif choice == '2':
        practice_song('Get\'cha Head in the Game', 'Basketball Team')
    elif choice == '3':
        practice_song('Breaking Free', 'Troy', 'Gabriella')

def practice_song(song, *characters):
    print(f"You've chosen to practice singing '{song}'!")
    time.sleep(1)
    print(f"Get ready to improve your singing skills as {' and '.join(characters)}!")
    time.sleep(1)
    print("Let's play the singing practice mini-game!")

    lyrics = load_lyrics(f"{song.lower().replace(' ', '_')}_lyrics.txt")
    start_index = random.randint(0, len(lyrics) - 4)

    for word in lyrics[start_index:start_index + 4]:
        print(word, end=' ')

    user_input = input("\nEnter the next line: ")
    expected_input = ' '.join(lyrics[start_index + 4:start_index + 8]).lower().strip()

    if user_input.lower().strip() == expected_input:
        print("Correct! Your singing is getting better.")
    else:
        print(f"Wrong! The correct line is: {' '.join(lyrics[start_index + 4:start_index + 8])}")

# Add this at the end of your script to initiate the program
introduction()
choice = make_choice()

if choice == '1':
    focus_on_studies()
elif choice == '2':
    audition_for_musical()
elif choice == '3':
    try_out_for_basketball()

