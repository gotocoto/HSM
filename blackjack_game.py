# blackjack_game.py
import random

def deal_initial_hand():
    return [deal_card(), deal_card()]

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def determine_winner(player_hand, dealer_hand):
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print(f"Your final score: {player_score}")
    print(f"Dealer's final score: {dealer_score}")

    if player_score > 21:
        print("Bust! You lose.")
        return False
    elif dealer_score > 21 or player_score > dealer_score:
        print("Congratulations! You win.")
        return True
    elif player_score < dealer_score:
        print("Oops! You lose.")
        return False
    else:
        print("It's a draw.")
        return False

def update_player_stats(player, win):
    if win:
        print("Your performance was outstanding! You gain some skills.")
        player.strategy_skills += 2  # New strategy skill improvement
    else:
        print("It was a tough game, but you'll get them next time.")

# Introducing the new strategy skill

def play_blackjack(player):
    print("You decide to play a quick game of Blackjack on your phone.")

    player_hand = deal_initial_hand()
    dealer_hand = deal_initial_hand()

    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand[0]} and [Hidden]")

    while sum(player_hand) < 21:
        hit_or_stand = input("Do you want to Hit or Stand? ").lower()

        if hit_or_stand == 'hit':
            player_hand.append(deal_card())
            print(f"Your hand: {player_hand}")
        elif hit_or_stand == 'stand':
            break
        else:
            print("Invalid choice. Please enter Hit or Stand.")

    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    print(f"Your final hand: {player_hand}")
    print(f"Dealer's final hand: {dealer_hand}")

    win = determine_winner(player_hand, dealer_hand)
    update_player_stats(player, win)

if __name__ == "__main__":
    # This block is for testing the blackjack game independently
    player = Player()
    play_blackjack(player)