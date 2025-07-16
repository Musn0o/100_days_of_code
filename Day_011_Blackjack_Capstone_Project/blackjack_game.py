import random
import os


# Function to deal a random card from the deck
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate score with Ace handling
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    temp_cards = cards[:]
    if sum(temp_cards) == 21 and len(temp_cards) == 2:
        return 0  # Blackjack
    while 11 in temp_cards and sum(temp_cards) > 21:
        temp_cards.remove(11)
        temp_cards.append(1)
    return sum(temp_cards)

# Function to compare user and computer scores
def compare(user_score, computer_score):
    """Compares user and computer scores to determine the winner."""
    if user_score == computer_score:
        return "It's a draw 🤝"
    elif computer_score == 0:
        return "Lose, computer has Blackjack 😤"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Computer went over. You win 😁"
    elif user_score > computer_score:
        return "You win 🥳"
    else:
        return "You lose 😤"

# Main game function
def play_game():
    # Clear console
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial card dealing
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    # User's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_another == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn only if user hasn't busted
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17 and user_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("-" * 50 + "\n")

# Game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()

print("Thanks for playing! 👋")
