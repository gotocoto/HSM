import time
import random
import sys
import re
import blackjack_game
from player import Player
import os

QUESTION_DIR = "questions"

'''
def introduction(player):
    print("Welcome to the High School Musical Adventure!")
    time.sleep(1)
    print("You are a student at East High School, and the school is buzzing with excitement for the winter musical.")
    time.sleep(1)
    print(f"Your current stats: Academic Knowledge - {player.academic_knowledge}, Singing Skills - {player.singing_skills}, Basketball Skills - {player.basketball_skills}")
    time.sleep(1)
    print("You can choose to focus on your studies and science club (1), audition for the musical (2), try out for the basketball team (3), or study for exams (4).")
'''
def make_choice(player):
    choice = input("Enter your choice (1, 2, 3, or 4): ")
    return choice

def focus_on_studies(player):
    print("You've decided to focus on your studies and join the science club.")
    time.sleep(1)
    print("While you excel academically, you miss out on the excitement of the musical and the basketball team.")
    time.sleep(1)
    print("The musical is a success, and you have a great time in the science club, but you wonder about the paths not taken.")
    player.academic_knowledge += 3

def audition_for_musical(player):
    print("🎭 Audition for the school musical! 🎤")
    time.sleep(2)

    # Display information about the audition
    print("The school musical auditions are here, and the stage is set.")
    time.sleep(3)
    print(f"You see Troy across the stage. He is also auditioning?")
    time.sleep(4)

    # Simulate the initial audition scenario
    print("\nSharpay and Ryan Evans walk onto the stage.")
    time.sleep(4)
    print("\nSharpay and Ryan Evans start singing...\n ")
    time.sleep(1)
    print("It's hard to believe\nThat I couldn't see...")
    time.sleep(7)

    # Indicate the end of Sharpay and Ryan Evans' song
    print("\nSharpay and Ryan Evans finish their song.")

    # Display the hesitation of Troy and the player
    print(f"\nTroy and you watch the performance but are hesitant to audition.")
    time.sleep(4)
    print("As the auditions are unofficially declared 'over', you gain the confidence to step forward.")
    time.sleep(4)

    # Internal dialogue - Player's nervous thoughts
    print("\nYou take a deep breath, your heart racing.")
    time.sleep(3)
    print("This is it, your first time ever auditioning. You can't help but feel a mix of excitement and nerves.")
    time.sleep(4)
    print("Your palms are sweaty, and your mind is a whirlwind of doubts and hopes.")
    time.sleep(4)
    print("But there's no turning back now. You've got to step up and take this chance.")

    # Offer Troy to sing with the player
    troy_offer = input(f"Troy offers to sing with you. Do you accept? (yes/no): ").lower()
    time.sleep(3)

    if troy_offer == 'yes':
        print(f"\nYou and Troy step forward to audition together.")
        time.sleep(4)
    else:
        print(f"\nYou decide not to audition with Troy.")
        time.sleep(3)
        print("Without a co-singer, you can't proceed with the audition.")
        print("Unfortunately, your journey at East High School ends here.")
        return  # End the story

    # Drama teacher Ms. Darbus declares them too late and leaves
    print("Ms. Darbus declares that you are too late and leaves the stage.")
    time.sleep(5)

    # Kelsi drops her music sheets on the stage
    print("\nSuddenly, you hear the unmistakable sound of paper fluttering down.")
    time.sleep(4)
    print("Kelsi Nielsen, the musical's composer, has dropped her music sheets on the stage.")
    time.sleep(4)
    print("The sheets scatter like leaves in the wind, creating an unexpected moment of chaos.")
    time.sleep(5)
    print(f"You and Troy rush to help her and decide to sing the same song together.")
    time.sleep(4)

    # Simulate singing together
    print(f"\nTroy and {player.name}: (singing) It's hard to believe\nThat I couldn't see...")
    time.sleep(6)

    

    # Singing mini-game with Troy and get the score
    print("\nGet ready to sing with Troy! Complete the lyrics:\n")
    song_file_name = 'what_ive_been_looking_for'
    singing_result = player.singing_mini_game(song_file_name)

    # Determine Ms. Darbus's impression based on the score
    if singing_result:
        print("\nMs. Darbus is impressed with your singing performance!")
        player.singing_skills += 10
        player.musical_member = True
    else:
        print("\nUnfortunately, your performance did not impress Ms. Darbus. Better luck next time.")


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
        return 3
    else:
        print("While not perfect, your performance was still impressive. Keep practicing for the big night.")
        return 1



def try_out_for_basketball(player):
    print("You've decided to try out for the basketball team, Wildcats!")
    time.sleep(1)
    print("The tryouts are intense, and you need to showcase your basketball skills.")
    time.sleep(1)
    print("Do you want to practice shooting hoops before tryouts (yes/no)?")
    practice_choice = input().lower()

    if practice_choice == 'yes':
        print("Let's practice your shooting skills!")
        time.sleep(1)
        player.basketball_skills += practice_basketball_mini_game()

    print("Now, it's time for the actual tryouts.")
    time.sleep(1)
    print("Let's play the basketball mini-game!")

    # If the player practiced, adjust the success rate for the actual tryouts
    success_rate = 0.7 if practice_choice == 'yes' else 0.5
    player.basketball_skills += practice_basketball_mini_game()

    if player.basketball_skills >= 15:
        print("Congratulations! You made it onto the basketball team!")
        player.basketball_team_member = True
    else:
        print("Sadly you didn't make it on the basketball team try again soon!")


def practice_basketball_mini_game():
    print("Press the enter key when shooting a shot. Hit the enter key again at the perfect time to make a shot")
    time.sleep(1)

    baskets_made = 0
    for _ in range(10):
        input("Get ready to shoot! Hold 'Enter' to shoot.")
        start_time = time.time()

        while True:
            if input() == '':
                end_time = time.time()
                break

        time_held = end_time - start_time

        if time_held < 1.5:  # Time required to make a basket
            print("Oops! You didn't hold the key long enough. Try again.")
        elif time_held > 2.5:
            print("Ohh no! You held the key too long enough. Try again.")
        else:
            print("Swish! You made the basket!")
            baskets_made += 1

    return (baskets_made / 10) * 10  # Convert to a score out of 10


def practice_singing(player):
    print("You decide to practice singing for the upcoming musical.")

    # List of available High School Musical songs (replace with your song names)
    song_list = [
        "start_of_something_new",
        "what_ive_been_looking_for",
        "breaking_free",
        "stick_to_the_status_quo",
        "getcha_head_in_the_game",
        "bop_to_the_top",
        "were_all_in_this_together",
    ]

    # Display available songs
    print("Available songs:")
    for i, song in enumerate(song_list, start=1):
        print(f"{i}. {song.replace('_', ' ').title()}")  # Display in title case

    # Get user's choice of song
    while True:
        try:
            song_choice = int(input("Choose a song to practice (1-7): "))
            if 1 <= song_choice <= 7:
                selected_song = song_list[song_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # File path for the selected song lyrics (replace with your file path)
    song_file_path = f"{selected_song}"
    success = player.singing_mini_game(song_file_path)

    if success:
        print(f"Your singing skills on '{selected_song.replace('_', ' ').title()}' have improved through practice!")
    else:
        print(f"Keep practicing '{selected_song.replace('_', ' ').title()}', and you'll get better!")
    '''
    else:
        print(f"Error: Song file not found for '{selected_song}'. Please check the file path.")'''

def study_for_exams(player):
    print("You've decided to study. What would you like to study for?")
    print("1. Academic Exams")
    print("2. Life-related Questions")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        questions_file = "exam_questions.txt"
    elif choice == '2':
        questions_file = "life_questions.txt"
    else:
        print("Invalid choice. Defaulting to Academic Exams.")
        questions_file = "academic_exam_questions.txt"

    print("Let's play the studying mini-game!")

    all_questions = load_questions(questions_file)
    selected_questions = random.sample(all_questions, 5)

    correct_answers = 0

    for question in selected_questions:
        print(question['question'])
        for option in question['options']:
            print(option)

        user_answer = input("Enter your answer (A, B, C, or D): ").upper()

        if user_answer == question['correct_answer']:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {question['correct_answer']}.")

    player.academic_knowledge += correct_answers

    print(f"You answered {correct_answers} out of {len(selected_questions)} questions correctly.")
    if correct_answers == len(selected_questions):
        print("Congratulations! You are well-prepared.")
    else:
        print("Keep studying, and you'll do great.")

def load_questions(file_path):
    file_path = f'{QUESTION_DIR}/{file_path}'
    with open(file_path, 'r') as file:
        lines = file.readlines()

    questions = []
    current_question = {}

    for line in lines:
        line = line.strip()

        if not line:
            questions.append(current_question)
            current_question = {}
        elif line.startswith('Q: '):
            current_question['question'] = line[3:]
        elif line.startswith('A. ') or line.startswith('B. ') or line.startswith('C. ') or line.startswith('D. '):
            current_question.setdefault('options', []).append(line)
        elif line.startswith('Correct Answer: '):
            current_question['correct_answer'] = line.split(': ')[1]

    return questions

# Function to handle chatting with friends

def chat_with_friends(player):
    print("You join your friends at a table and start chatting.")

    # Simulate a conversation with friends
    conversation_options = [
        "1. Talk about the upcoming school musical.",
        "2. Discuss the latest basketball game.",
        "3. Share your plans for the weekend.",
        "4. Bring up a recent movie you watched.",
        "5. Discuss a trending topic from social media.",
        "6. Share a funny story from school.",
        "7. Express your thoughts on a controversial topic.",
    ]

    for option in conversation_options:
        print(option)

    conversation_choice = input("Choose a topic to discuss (1-7): ")

    if conversation_choice == '1':
        print("Your friends are excited about the musical. You share your interest and become more involved.")
        player.musical_member = True
        player.social_status += 10
    elif conversation_choice == '2':
        print("Your friends discuss the basketball game. You join in, and your basketball skills improve.")
        player.basketball_skills += 5
        player.social_status += 5
    elif conversation_choice == '3':
        print("You talk about your plans for the weekend. Your friends find it interesting, and your social status improves.")
        player.social_status += 8
    elif conversation_choice == '4':
        print("You bring up a recent movie you watched. Your friends enjoy the discussion.")
        player.social_status += 5
    elif conversation_choice == '5':
        print("You discuss a trending topic from social media. Your friends appreciate your insights.")
        player.social_status += 7
    elif conversation_choice == '6':
        print("You share a funny story from school. Your friends laugh, and your social status improves.")
        player.social_status += 8
    elif conversation_choice == '7':
        print("You express your thoughts on a controversial topic. Some friends disagree, and your social status may decrease.")
        player.social_status -= 5
    else:
        print("Invalid choice. The conversation continues without a significant impact.")

    print(f"Your social status is now {player.social_status}.")


def go_to_cafeteria(player):
    print("\nYou head to the cafeteria to grab a bite.")

    # Add cafeteria scene logic here
    print("In the cafeteria, you have a few options:")
    print("1. Chat with friends")
    print("2. Get food")
    print("3. Find a quiet spot to study")
    print("4. Play a quick game on your phone")

    cafeteria_choice = input("Enter your choice (1, 2, 3, or 4): ")
    print("")
    if cafeteria_choice == '1':
        chat_with_friends(player)
    elif cafeteria_choice == '2':
        get_food_sub_option(player)
    elif cafeteria_choice == '3':
        player.play_memory_minigame()
    elif cafeteria_choice == '4':
        blackjack_game.play_blackjack(player)
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")


def get_food_sub_option(player):
    print("You decide to grab some food.")

    # Add food options logic here
    print("Food options:")
    print("1. Healthy Salad (increases energy by 10) - $5")
    print("2. Pizza Slice (increases energy by 5) - $3")
    print("3. Energy Drink (increases energy by 15) - $8")
    print("4. Sandwich (increases energy by 7) - $4")
    print("5. Fruit Smoothie (increases energy by 12) - $6")

    food_choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if food_choice == '1':
        cost = 5
        food_name = "Healthy Salad"
        energy_increase = 10
    elif food_choice == '2':
        cost = 3
        food_name = "Pizza Slice"
        energy_increase = 5
    elif food_choice == '3':
        cost = 8
        food_name = "Energy Drink"
        energy_increase = 15
    elif food_choice == '4':
        cost = 4
        food_name = "Sandwich"
        energy_increase = 7
    elif food_choice == '5':
        cost = 6
        food_name = "Fruit Smoothie"
        energy_increase = 12
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        return

    # Check if the player has enough money to buy the selected food
    if player.money >= cost:
        print(f"You chose the {food_name}. It boosts your energy.")
        player.energy += energy_increase
        player.money -= cost
        print(f"You paid ${cost}. Your current balance: ${player.money}")
    else:
        print("Sorry, you don't have enough money to buy that.")

    # Limit energy to a maximum value (e.g., 100)
    player.energy = min(player.energy, 100)
# You can expand and customize this function based on your game's requirements.
def introduction():
    print("🌟 Welcome to East High! 🌟")
    print("Get ready to embark on a musical journey filled with friendship, love, and unforgettable moments.")
    
    # Prompt the user for their name
    player_name = input("Before we begin, what's your name? ")

    # Create a player object with the user's name
    player = Player(name=player_name)

    print(f"Great, {player.name}! You are now a student at East High, where the air is buzzing with excitement and the halls are alive with the sound of music.")
    print("As you navigate through classes, interact with friends, and face the challenges of high school life, remember that we're all in this together.")
    print("It's time to discover your talents, break free from the status quo, and create a high school experience you'll cherish forever.")
    print("Let the Wildcats adventure begin!\n")
    
    # Prompt the user to press Enter to start the game
    input("Press Enter to start your high school adventure...\n")
    return player

def introduction_cut_scene(player):
    print("🌟 Welcome to the High School Musical Adventure! 🌟")
    time.sleep(2)
    print("On New Year's Eve, you, a high school junior, find yourself at a lively ski lodge party during winter break.")
    time.sleep(4)
    print("Amid the celebration, you meet a fellow party-goer named Troy Bolton.")
    time.sleep(3)
    print("As fate would have it, the two of you are called upon to sing a duet together for karaoke, marking the 'Start of Something New.'")
    time.sleep(5)

    # Construct the full file path for the chosen song
    song_name = 'start_of_something_new'
    
    # Singing mini-game with Troy and get the score
    singing_result = player.singing_mini_game(song_name)

    if singing_result:
        print("The duet concludes, leaving both you and Troy in awe of the musical connection you share.")
        time.sleep(3)
    else:
        print("Despite a few hiccups, the duet concludes. It seems there's room for improvement, but you've made it through.")
        time.sleep(3)

    print("The holiday break comes to an end, and you return to school, only to find Troy in your homeroom.")
    time.sleep(4)
    print("He shows you around East High School, and you explain that you've just moved to Albuquerque, New Mexico, and transferred to East High over the break.")
    time.sleep(5)
    print("Little do you know, drama club president Sharpay Evans is already plotting to secure the lead roles in the school musical.")
    time.sleep(4)
    print("Sharpay, fearing competition, discovers your impressive academic achievements and anonymously informs scholastic decathlon captain Taylor McKessie.")
    time.sleep(5)
    print("Taylor, impressed by your achievements, recruits you for the scholastic decathlon team, leading to an unexpected friendship between you and Taylor.")
    time.sleep(4)
    print("Now, with the stage set, your journey at East High School is about to unfold. Are you ready for the adventure?\n")

    input("")
    return player

def game_loop():
    player_data_file = "player_data.json"  # Replace with your desired file name
    player = Player("Dummy") 

    # Check if the player data file exists
    if os.path.exists(player_data_file):
        # If the file exists, load player data
        player.load_from_file(player_data_file)
        print("Welcome back, {}!".format(player.name))
    else:
        player = introduction()
        player = introduction_cut_scene(player)
    continue_story(player)
    while True:
        print("\nOptions:")
        print("1. Continue the story")
        print("2. View player stats")
        print("3. Save player data")
        print("4. Quit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            # Call a function to continue the story
            continue_story(player)
        elif choice == '2':
            # Call a function to display player stats
            display_stats(player)
        elif choice == '3':
            # Save player data
            player.save_to_file(player_data_file)
            print("Player data saved.")
        elif choice == '4':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def continue_story(player):
    print("\nYou find yourself at East High School facing various challenges and opportunities.")
    
    while True:
        print("\nOptions:")
        if player.musical_member:
            print("1. Attend musical rehearsal")
        else:
            print("1. Audition for the school musical")
        if player.basketball_team_member:
            print("2. Attend basketball practice")
        else:
            print("2. Attend basketball tryouts")
        print("3. Study for exams")
        print("4. Go to the cafeteria")
        print("5. Back to main menu")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        
        if choice == '1':
            if player.musical_member:
                print("You decide to attend musical rehearsal.\n")
                practice_singing(player)
            else:
                print("You decide to audition for the school musical.")
                audition_for_musical(player)
        elif choice == '2':
            if player.basketball_team_member:
                print("You decide to attend basketball practice.")
                practice_basketball_mini_game(player)
            else:
                print("You decide to attend basketball tryouts.")
                try_out_for_basketball(player)
        elif choice == '3':
            study_for_exams(player)
        elif choice == '4':
            go_to_cafeteria(player)
        elif choice == '5':
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def display_stats(player):
    # Display player stats
    print("\nPlayer Stats:")
    print(f"Academic Knowledge: {player.academic_knowledge}")
    print(f"Singing Skills: {player.singing_skills}")
    print(f"Basketball Skills: {player.basketball_skills}")
    print(f"Basketball Team Member: {player.basketball_team_member}")
    print(f"Musical Member: {player.musical_member}")
    print(f"Energy: {player.energy}")

# Example usage:
if __name__ == "__main__":
    game_loop()
