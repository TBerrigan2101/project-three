import random

WORD = ['adult', 'agent', 'anger', 'apple', 'award', 'basis']


def play_game():

    """
    ask user for guess check the guess letter
    add a point if word guess is correct
    reduce the guess count if letter is incorrect
    """


available_attempts = 5
guessed_letter = ' '

selected_word = random.choice(WORD)
selected_word_dict = {}
for letter in selected_word:
    if letter in selected_word_dict:
        selected_word_dict[letter] += 1
    else:
        selected_word_dict[letter] = 0

while available_attempts > 0:
    correct_letter = 0
    guess = input('\nGuess a letter in the hidden word: ').lower()
    validate_input(guess)

    if guess in selected_word:
        if guess in selected_word_dict:
            selected_word_dict.pop(guess)
        elif guess == ' ':
            guess.strip(guess)
        else:
            print('this letter has already been guessed please guess again')
            continue

    print(f"\nNice job, '{guess}' is in the word")
    guessed_letter = guessed_letter + guess

    for letter in selected_word:
        if letter in guessed_letter:
            print(f"{letter}", end="")
            correct_letter += 1
        else:
            print(f"_", end="")

    else:
        available_attempts -= 1
        print(f"Wrong! You have {available_attempts} attempts remaining")

    if correct_letter == 5:
        print(f"\nWell done! You correctly guessed:'{selected_word}'.")
        print(f"You have scored a point.")
        return 1
    elif available_attempts == 0:
        print(f"\nHard luck! The hidden word is'{selected_word}'")
        return 0
        


def validate_input(user_input):
    if user_input.isnumeric():
        print('You entered a number by accident')
    elif user_input.isspace():
        print('Your entry contains a blank space')
    elif not user_input.isalpha():
        print('Your entry must contain a letter')
    else:
        None

    """
    Function to run the game and collect and tally scores from each round.
    """


def run_game():
    score = 0
    for x in range(5):
        print('\nROUND ' + str(x + 1))
        score += play_game()
        print(f"\nYour total score is {score}")


print("Welcome to 5-5-5!")
print("How to play:")
print("You will have 5 attempts to guess 5 words, each containing 5 letters.")
print("Enter a lowercase letter to see if the word contains that letter.")
print("A wrong guess results in losing one of your 5 attempts for that word.")
run_game()
