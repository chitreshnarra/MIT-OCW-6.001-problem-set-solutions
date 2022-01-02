import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10,'*':0
}


WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    l_word = word.lower()
    word_length = len(word)
    first_component = 0
    for x in l_word :
        first_component += (SCRABBLE_LETTER_VALUES[x])    
    if 7*word_length - 3*(n-word_length) >= 1 :
        second_component = 7*word_length - 3*(n-word_length)
    else :
        second_component = 1
    
    return first_component*second_component

    


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      
    print()                              


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={'*':1}
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    n_hand = {}

    for letter in hand.keys():
        n_hand[letter]= n_hand.get(letter,0)+hand[letter]
    for x in word :
        n_hand[x] = n_hand.get(x,0) - 1
    
    for letter in n_hand.keys() :
        if n_hand[letter] < 0 :
            n_hand[letter] = 0
    
    return n_hand

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    if '*' not in word :
        if word in word_list :
            in_word_list = True
        else :
            in_word_list = False
        if len(hand) == len(update_hand(hand,word)) :
            in_hand = True
        else :
            in_hand = False
    
    else :
        if len(hand) == len(update_hand(hand,word)) :
            in_hand = True
        else :
            in_hand = False
        
        word_valid = 0
        
        for x in VOWELS :
            
            llist = list(word)
            n_list = llist.copy()
            for i in range(len(llist)) :
                if llist[i] == '*' :
                    n_list[i] = x
                    n_word = ''
                    for l in n_list :
                        n_word = n_word + l
                    if n_word in word_list :
                        word_valid += 1            
                        print(n_word)
        if word_valid >= 1 :
            in_word_list = True
        else :
            in_word_list = False
    
    
    
    return in_word_list and in_hand


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_len = []
    for letter in hand.keys() :
        hand_len.append(hand[letter])
    
    return sum(hand_len)


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    
    total_score = 0
    n_hand = hand.copy()
    
    while True :
        x=0
        for key in  n_hand.keys() :
            x += n_hand[key]
        if x == 0 :
            break
        
        display_hand(n_hand)

        word = input("enter word or '!!' to indicate that you are finished:")

        if word == '!!':
            break
        
        else :
            if is_valid_word(word,n_hand,word_list) == True :
                print('points earned are :',get_word_score(word,calculate_handlen(n_hand)))
                total_score = total_score + get_word_score(word,calculate_handlen(n_hand))
            else :
                print("enter a valid word")
            
            n_hand = update_hand(n_hand,word)
            
    print('game over,total score:',total_score)
    return total_score
        

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    n_hand = hand.copy()
    
    if letter in n_hand.keys() :        
        letter_list = []
    
        for l in hand.keys() :
    
            if l not in letter_list :
                letter_list.append(l)
    
        choose_from = list(VOWELS+CONSONANTS)
        letter_list.remove('*')
    
        for x in letter_list :
            choose_from.remove(x)
    
        n_letter = random.choice(choose_from)
        hand[n_letter] = n_hand[letter]
        hand[letter] = 0
    
    return hand
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    no_of_rounds = int(input('how many rounds do you want to play?'))
    score = 0
    substitutions =  1
    replay = 1
    
    while no_of_rounds != 0 :
        hand = deal_hand(10)       
        display_hand(hand) 
    
        if substitutions == 1 :
            ans = input('would you like to substitute a letter ?:(y/n)')
    
            if ans == 'y':
                letter=input('which letter do you want to substitute: ')
                substitute_hand(hand,letter)
                substitutions = substitutions - 1
    
        total_score = play_hand(hand,word_list)
    
        if replay == 1 :
            score_2 = 0
            ans = input('do you want to play this hand again:(y/n) ')
    
            if ans == 'y' :
                score_2 = play_hand(hand,word_list)
                replay = replay - 1
        score = score+max(total_score,score_2)
        no_of_rounds -= 1
 
    print(score)
    

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
