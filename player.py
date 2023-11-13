# player.py

import random
import os
import getpass
import time


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

    def study_for_exams(self):
        print("You find a quiet corner, take out your books, and study for a while.")
        # Add studying logic here
        # For simplicity, let's just increase academic knowledge
        self.academic_knowledge += 5
        self.energy -= 10  # Studying consumes energy
        print("You've gained some academic knowledge, but you feel a bit tired.")

    def preprocess_line(self, line):
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans("", "", string.punctuation)).lower()
        return line

    def rate_line_correctness(self, user_line, correct_line):
        user_line_processed = self.preprocess_line(user_line)
        correct_line_processed = self.preprocess_line(correct_line)

        if user_line_processed == correct_line_processed:
            return 2  # Full score for a completely correct line
        elif user_line_processed in correct_line_processed or correct_line_processed in user_line_processed:
            return 1  # Partial score for a partially correct line
        else:
            return 0  # No score for an incorrect line

    def singing_mini_game(self, song_name):
        # File path for the lyrics folder
        lyrics_folder = "lyrics"

        # File path for the selected song lyrics
        song_file_path = f"{lyrics_folder}/{song_name}_lyrics.txt"

        # Load the lyrics from the file
        with open(song_file_path, 'r') as file:
            lyrics = file.read().splitlines()

        # Choose a random starting point in the lyrics
        start_index = random.randint(0, len(lyrics) - 5)
        lines_to_display = 4 + self.difficulty  # Adjust the number of lines based on difficulty
        lines_to_sing = lyrics[start_index:start_index + lines_to_display]

        # Display the starting lines to the player
        print("\nGet ready to sing! Complete the lyrics:")
        for line in lines_to_sing:
            print(line)
            time.sleep(1)

        # User input for singing
        if self.difficulty > 0:
            correct_lines = lyrics[start_index:start_index + lines_to_display]
            user_input_lines = []

            for _ in range(lines_to_display):
                user_input = input("\nEnter the next line: ")
                user_input_lines.append(user_input)

            # Check the correctness of the user's input
            correct_lines_lower = [line.lower() for line in correct_lines]
            user_input_lines_lower = [line.lower() for line in user_input_lines]

            if user_input_lines_lower == correct_lines_lower:
                print("Great job! You sang it perfectly.")
                self.singing_skills += 5  # Adjust the score based on your preference
                return True
            else:
                print("Oops! It seems you made a mistake in the lyrics.")
                return False
        else:
            # If difficulty is 0, the player doesn't need to enter any lines
            input("\nPress Enter to continue...")

        return True  # For simplicity, consider it a success without user input
