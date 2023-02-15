import random

WORD = ['adult', 'agent', 'anger', 'apple', 'award', 'basis']


def play_game():
    """
    Selects a word using the random module from the global
    list 'Words'.Once the word is selected, its letters are also
    passed to a dictionary so the letters are assessed individually
    Asks the user to input a letter to start guessing the selected
    word for that round and validates the input Runs a while loop
    until the user has exhausted all of their attempts to guess the word"
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

    """
    Once the guess has been validated it is reviewed to see if the word
    contains that letter. If it is, it's displayed where it occurs in the
    letter and the user is given a congratulatory message. Any remaining
    letters are displayed as '_'. If the letter is not in the word,
    all of the spaces are left blank and the user is given a commiseration
    message. The user is then made aware that they have lost one of their
    attempts and they have a certain amount remaining.
    """

    if guess in selected_word:
        if guess in selected_word_dict:
            selected_word_dict.pop(guess)
        elif guess == ' ':
            guess.strip(guess)
    else:
        print('this letter has already been guessed, please guess again')
        continue

    print(f"\nNice job, '{guess}' is in the word")
    guessed_letter = guessed_letter + guess

    for letter in selected_word:
        if letter in guessed_letter:
            print(f"{letter}", end="")
            correct_letter += 1
        elif print(f"_", end=""):
            else:
            available_attempts -= 1
            print(f"Wrong! You have {available_attempts} attempts left")

    """
    If the user has guessed all 5 letters correctly, the hidden word is
    displayed, the user is given a congratulatory message. A point is then
    added to the score for tallying once the game is finished. If the user
    has used all their attempts and has still not guessed the word the
    hidden word is displayed, the user is given a commiseration message and
    gains no points.
    """

    if correct_letter == 5:
        print(f"\nWell done! You correctly guessed:'{selected_word}'.")
        print(f"You have scored a point.")
        return 1
    elif available_attempts == 0:
        print(f"\nHard luck! The hidden word is'{selected_word}'")
        return 0

    """
    Validates user input to check for numbers, blank spaces, 
    special characters and alerts user what has happened.
    """    

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
    Function to run the game and collect and 
    tally scores from each round.
    """   

def run_game():
  score = 0
  for x in range(5):
    print('\nROUND ' + str(x + 1))
    score += play_game()
  print(f"\nYour total score is {score}")    