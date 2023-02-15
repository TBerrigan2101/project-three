import random

WORD = ['adult', 'agent', 'anger', 'apple', 'award', 'basis', 'beach', 'birth', 'block', 'blood', 'board', 'brain', 'bread', 'break', 'brown',
  'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child', 'china', 'claim', 'class', 'clock', 'coach', 'coast', 'court', 'cover', 'cream',
  'crime', 'cross', 'crowd', 'crown', 'cycle', 'dance', 'death', 'depth', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'earth',
  'enemy', 'entry', 'error', 'event', 'faith', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'front', 'fruit', 'glass', 
  'grant', 'grass', 'green', 'group', 'guide', 'heart', 'horse', 'hotel', 'house', 'image', 'index', 'input', 'issue', 'judge', 'knife', 'layer', 
  'level', 'light', 'limit', 'lunch', 'major', 'march', 'match', 'metal', 'model', 'money', 'month', 'motor', 'mouth', 'music', 'night', 'noise', 
  'north', 'novel','nurse', 'offer', 'order', 'other', 'owner', 'panel', 'paper', 'party', 'peace', 'phase', 'phone', 'piece', 'pilot', 'pitch', 
  'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'prize', 'proof', 'queen', 'radio', 'range', 'ratio', 
  'reply', 'right', 'river', 'round', 'route', 'rugby', 'scale', 'scene', 'scope', 'score', 'sense', 'shape', 'share', 'sheep', 'sheet', 'shift', 
  'shirt', 'shock', 'sight', 'skill', 'sleep', 'smile', 'smoke', 'sound', 'south', 'space', 'speed', 'spite', 'sport', 'squad', 'staff', 'stage', 
  'start', 'state', 'steam', 'steel', 'stock', 'stone', 'store', 'study', 'stuff', 'style', 'sugar', 'table', 'taste', 'theme', 'thing', 'title', 
  'total', 'touch', 'tower', 'track', 'trade', 'train', 'trend', 'trial', 'trust', 'truth', 'uncle', 'union', 'unity', 'value',
  'video', 'visit', 'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman', 'world', 'youth'
]

def play_game():

  """
     Selects a word using the random module from the global list 'Words'
     Once the word is selected, its letters are also passed to a dictionary so the letters can be assesed individually.
     Asks the user to input a letter to start guessing the selected word for that round and validates the input.
     Runs a while loop until the user has exhausted all of their attempts to guess the word"
  
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
     Once the guess has been validated it is reviewed to see if the word contains that letter.
     If it is, it's display where it occurs in the letter and the user is given a contgatulatory message.
     Any remaning letters are dispalyed as '_'
     If the letter is not in the word, all of the spaces are left blank and the user is given a commiseration message.
     The user is then made aware that they have lost one of their attempts and they have a certain amount remaining.
    
    """

    if guess in selected_word:
      if guess in selected_word_dict:
        selected_word_dict.pop(guess)
      elif guess == ' ':
        guess.strip(guess)
      else:
        print(
          'this letter has already been guessed, please guess another letter')
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

    """
    If the user has guessed all 5 letters correctly, the hidden word is displayed, the user is given a contgatulatory message.
    A point is then added to the score for tallying once the game is finished.
    If the user has used all their attempts and has still not guessed the word the hidden word is displayed, the user is given a commiseration message and gains no points.
    
    """  

    if correct_letter == 5:
      print(f"\nWell done! You correctly guessed the word:'{selected_word}'.")
      print(f"You have scored a point.")
      return 1
    elif available_attempts == 0:
      print(f"\nHard luck! The hidden word is'{selected_word}'")
      return 0