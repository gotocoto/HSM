# player.py

import random
import os
import getpass
import time
import json
import re
# Constant for the lyrics folder path
LYRICS_FOLDER = "lyrics/"

class Player:
    def __init__(self, name="Player", difficulty=1):
        self.name = name
        self.academic_knowledge = 0
        self.singing_skills = 0
        self.basketball_skills = 0
        self.strategy_skill = 0
        self.basketball_team_member = False
        self.musical_member = False
        self.energy = 50
        self.money = 20  # Default starting money
        self.social_status = 50  # Default starting social status
        self.difficulty = difficulty
    def save_to_file(self, filename):
        # Save player data to a JSON file
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)
    def load_from_file(self, filename):
        # Load player data from a JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
        self.__dict__.update(data)
    def study_for_exams(self):
        print("You find a quiet corner, take out your books, and study for a while.")
        # Add studying logic here
        # For simplicity, let's just increase academic knowledge
        self.academic_knowledge += 5
        self.energy -= 10  # Studying consumes energy
        print("You've gained some academic knowledge, but you feel a bit tired.")

    def preprocess_line(self, line):
        # Remove punctuation and convert to lowercase
        return re.sub(r'[^\w\s]', '', line).lower()

    def singing_mini_game(self, song_name):
        # Construct the full file path for the chosen song
        file_path = os.path.join(LYRICS_FOLDER, f"{song_name}_lyrics.txt")

        # Load the lines from the chosen file, excluding empty lines
        with open(file_path, 'r') as file:
            lyrics = [line.strip() for line in file if line.strip()]

        # Choose a random starting point in the lyrics
        start_index = random.randint(0, len(lyrics) - self.difficulty - 4)  # Subtract 4 to ensure at least 4 lines are displayed
        lines_to_display = 4  # Adjust the number of lines based on difficulty

        print(f"\nIt's time to sing {song_name.replace('_', ' ').title()}")
        print("Complete the lyrics:\n")

        # User input for singing
        while start_index + lines_to_display + self.difficulty < len(lyrics):
            lines_to_sing = lyrics[start_index:start_index + lines_to_display]

            # Display the lines to the player
            for line in lines_to_sing:
                print(line)

            correct_lines = lyrics[start_index + lines_to_display: start_index + lines_to_display + self.difficulty]

            for line in correct_lines:
                # Check if the line is wrapped in brackets
                if "[" in line and "]" in line:
                    singer = re.search(r'\[.*?\]', line).group(0)
                    print(f"\n{singer} {line.replace(singer, '').strip()}")

                user_input = input("\nEnter the next line: ")
                # Check if the user's input is correct, excluding empty lines
                correct_line = self.preprocess_line(correct_lines.pop(0))
                user_input_processed = self.preprocess_line(user_input)

                if user_input_processed != correct_line:
                    print(f"**SCREECH** You said the wrong line. Let's try again...")
                    user_input = input("\nEnter the correct line: ")
                    user_input_processed = self.preprocess_line(user_input)

                    if user_input_processed != correct_line:
                        print("Oops! You said the wrong line again. Better luck next time!\n")
                        return False

                print("Correct!\n")

            start_index += lines_to_display + self.difficulty

        print("Congratulations! You sang it perfectly.")
        return True




    
    def play_memory_minigame(self):
        print("You decide to challenge your memory with a quick mini-game.")

        # Generate a sequence of numbers
        sequence = [random.randint(1, 9) for _ in range(5)]

        # Display the sequence for the player to see
        print("Memorize the sequence:", sequence)

        # Player's turn to recall and type the sequence
        print("Enter the numbers in the sequence in numerical order:")

        # Construct the correct sequence string for validation
        correct_sequence_str = ' '.join(map(str, sorted(sequence)))

        # Player types the sequence without seeing what they are typing
        user_input = getpass.getpass(prompt="Type the numbers (separated by spaces): ")

        # Check if the player's input matches the correct sequence
        if user_input == correct_sequence_str:
            print("Congratulations! You correctly entered the sequence.")
            # Add any rewards or stat improvements here
            self.academic_knowledge += 5
            self.energy -= 5
        else:
            print("Oops! It seems like you made a mistake in the sequence.")
