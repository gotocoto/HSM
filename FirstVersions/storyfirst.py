import time
import random
import sys

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

    score = song_performance_mini_game()
    print(f"Your performance score for '{song}' is {score}/10!")

    if score >= 9:
        print("Congratulations! You stole the show with your incredible performance.")
    else:
        print("While not perfect, your performance was still impressive. Keep practicing for the big night!")

def song_performance_mini_game():
    print("Press 'Enter' when you see 'X' to hit the right note!")
    time.sleep(1)

    notes = ["X"] * 10  # Simulating 10 notes in the song
    user_input = input("Start the song by pressing 'Enter'!")
    start_time = time.time()

    correct_notes = 0
    for note in notes:
        print(note, end="", flush=True)
        time.sleep(1)  # Delay between notes
        user_input = input()
        if user_input == "":
            end_time = time.time()
            reaction_time = end_time - start_time
            if 0.5 <= reaction_time <= 1.5:  # Adjust the timing window as needed
                correct_notes += 1
            else:
                print("Missed the timing!")

            start_time = time.time()

    return (correct_notes / len(notes)) * 10  # Convert to a score out of 10

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

    score = singing_practice_mini_game()
    print(f"Your singing practice score for '{song}' is {score}/10!")

    if score >= 7:
        print("Great job! Your singing skills are improving.")
    else:
        print("Keep practicing to reach your full singing potential!")

def singing_practice_mini_game():
    print("Press 'Enter' when you see 'Lip Sync' to match the correct lip-syncing timing!")
    time.sleep(1)

    cues = ["Lip Sync"] * 10  # Simulating 10 cues in the singing practice
    user_input = input("Start the singing practice by pressing 'Enter'!")
    start_time = time.time()

    correct_cues = 0
    for cue in cues:
        print(cue, end="", flush=True)
        time.sleep(1)  # Delay between cues
        user_input = input()
        if user_input == "":
            end_time = time.time()
            reaction_time = end_time - start_time
            if 0.5 <= reaction_time <= 1.5:  # Adjust the timing window as needed
                correct_cues += 1
            else:
                print("Missed the timing!")

            start_time = time.time()

    return (correct_cues / len(cues)) * 10  # Convert to a score out of 10

def study_mini_game():
    print("You've decided to study for your exams.")
    time.sleep(1)
    print("Let's play the study mini-game!")

    score = study_mini_game_logic()
    print(f"Your study session score is {score}/10!")

    if score >= 8:
        print("Fantastic! You've mastered the material and feel confident for your exams.")
    else:
        print("While not perfect, your study session was still productive. Keep it up!")

def study_mini_game_logic():
    print("Answer the following questions to test your knowledge:")
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is the powerhouse of the cell?", "Mitochondria"),
        ("Who wrote 'Romeo and Juliet'?", "William Shakespeare"),
        ("What is the chemical symbol for water?", "H2O"),
        ("How many continents are there?", "7")
    ]

    correct_answers = 0
    for question, correct_answer in questions:
        user_answer = input(f"{question}: ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    return (correct_answers / len(questions)) * 10  # Convert to a score out of 10

def main():
    introduction()
    choice = make_choice()

    if choice == '1':
        focus_on_studies()
    elif choice == '2':
        audition_for_musical()
    elif choice == '3':
        try_out_for_basketball()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
