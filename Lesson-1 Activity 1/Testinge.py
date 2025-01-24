import random
Hangman_board = []
completingword = []
times = 0
words = ["about", "other", "which", "their", "there", "could", "these", "would", "after", "first", "think", "right", "where", "being", "under", "never", "while", "might", "every", "those", "often", "again", "great", "small", "large", "since", "among", "begin", "order", "found", "means", "three", "place", "white", "green", "times", "young", "money", "music", "power", "happy", "short", "write", "world", "story", "clear", "voice", "human", "heart", "light", "above", "value", "bring", "build", "water", "leave", "field", "stand", "north", "south", "learn", "woman", "child", "point", "brown", "black", "given", "truth", "force", "peace", "lives", "class", "round", "based", "local", "piece", "reach", "board", "agree", "close", "known", "count", "paint", "enjoy", "enter", "offer", "guess", "using", "third", "share", "years", "whole", "focus", "guard", "crazy", "trust", "faith", "plant", "earth", "fruit", "place", "under", "might", "think", "happy", "about", "their", "music", "world", "never", "order", "write", "place", "which", "under", "water", "story", "above", "after", "those", "small", "bring", "light", "child", "happy", "three", "power", "great", "often", "place", "write", "heart", "think", "music", "north", "times", "where", "brown", "force", "based", "black", "board", "based", "known", "small", "green", "bring", "based", "north", "child", "truth", "happy", "guard", "value", "whole", "reach", "earth", "fruit", "light", "peace", "heart", "round", "truth", "piece", "earth", "reach", "faith", "fruit", "child", "north", "piece", "guess", "whole", "guard", "years", "great", "leave", "class", "write", "light", "brown", "above", "value", "think", "fruit", "where", "about", "times", "round", "order", "field", "music", "north", "faith", "never", "peace", "learn", "under", "known", "based", "often", "above", "times", "never", "round", "known", "count", "black", "leave", "happy", "great", "guard", "bring", "brown", "write", "light", "reach", "class", "small", "force", "earth", "truth", "based", "peace", "water", "their", "board", "under", "north", "heart", "learn", "whole", "piece", "power", "story", "earth", "fruit", "think", "guard", "north", "where", "brown", "field", "based", "truth", "crown", "lemon", "bliss", "glory", "draft", "honey", "ocean", "valve", "chaos", "glaze", "crisp", "plush", "blend", "drama", "flair", "pixel", "adore", "rover", "globe", "fleet", "quake", "venom", "witty", "jolly", "covet", "scoop", "dizzy", "gloom", "blast", "chill", "whale", "swirl", "flare", "chant", "sleek", "clown", "penny", "weave", "scout", "roast", "spear", "clasp", "quilt", "vivid", "frank", "pulse", "meadow", "ember", "creep"]

actualword = random.choice(words)

actualword = list(actualword)

a = ""

def gameover():
    print("You have guessed too much and have lost!")
    print("The word was --",actualword)
    print("Now exiting the program")
    quit()

while completingword != actualword:
    try:
        a = str(input("Please enter a letter to match the word"))
    except ValueError:
        print("Wrong Guess! Try again")
        a = ""

    if a == actualword[0]:
        completingword.insert(0,a)
        print("You Got some information! Heres the letters that are correct",completingword)
    elif a == actualword[1]:
        completingword.insert(1,a)
        print("You Got some information! Heres the letters that are correct",completingword)
    elif a == actualword[2]:
        completingword.insert(2,a)
        print("You Got some information! Heres the letters that are correct",completingword)
    elif a == actualword[3]:
        completingword.insert(3,a)
        print("You Got some information! Heres the letters that are correct",completingword)
    elif a == actualword[4]:
        completingword.insert(4,a)
        print("You Got some information! Heres the letters that are correct",completingword)
    
    else:
        times += 1
        if times == 1:
            Hangman_board = ["O"]
            print("The man is now -",Hangman_board)
        elif times == 2:
            Hangman_board = ["O", "\n" "|"]
            print("The man is now -",Hangman_board)
        elif times == 3:
            Hangman_board = ["O"  "\n" "--|"]
            print("The man is now -",Hangman_board)
        elif times == 4:
            Hangman_board = ["O" , "\n" , "--|--"]
            print("The man is now -",Hangman_board)
        elif times == 5:
            Hangman_board = ["O" , "\n" , "--|--" , "\n", "/"]
            print("The man is now -",Hangman_board)
        elif times == 6:
            Hangman_board = ["O" , "\n" , "--|--", "\n", "/ \\ "]
            print("The man is now -",Hangman_board)
            gameover()

    if completingword == actualword:
        print("You won!")  
        print("Exiting...")
        quit()
            