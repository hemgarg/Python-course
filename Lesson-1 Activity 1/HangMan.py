import random
Hangman_board = []
completingword = ['_','_','_','_','_']
times = 0
wrong_guesses = []

words = ["about", "other", "which", "their", "there", "could", "these", "would", "after", "first", "think", "right", "where", "being", "under", "never", "while", "might", "every", "those", "often", "again", "great", "small", "large", "since", "among", "begin", "order", "found", "means", "three", "place", "white", "green", "times", "young", "money", "music", "power", "happy", "short", "write", "world", "story", "clear", "voice", "human", "heart", "light", "above", "value", "bring", "build", "water", "leave", "field", "stand", "north", "south", "learn", "woman", "child", "point", "brown", "black", "given", "truth", "force", "peace", "lives", "class", "round", "based", "local", "piece", "reach", "board", "agree", "close", "known", "count", "paint", "enjoy", "enter", "offer", "guess", "using", "third", "share", "years", "whole", "focus", "guard", "crazy", "trust", "faith", "plant", "earth", "fruit", "place", "under", "might", "think", "happy", "about", "their", "music", "world", "never", "order", "write", "place", "which", "under", "water", "story", "above", "after", "those", "small", "bring", "light", "child", "happy", "three", "power", "great", "often", "place", "write", "heart", "think", "music", "north", "times", "where", "brown", "force", "based", "black", "board", "based", "known", "small", "green", "bring", "based", "north", "child", "truth", "happy", "guard", "value", "whole", "reach", "earth", "fruit", "light", "peace", "heart", "round", "truth", "piece", "earth", "reach", "faith", "fruit", "child", "north", "piece", "guess", "whole", "guard", "years", "great", "leave", "class", "write", "light", "brown", "above", "value", "think", "fruit", "where", "about", "times", "round", "order", "field", "music", "north", "faith", "never", "peace", "learn", "under", "known", "based", "often", "above", "times", "never", "round", "known", "count", "black", "leave", "happy", "great", "guard", "bring", "brown", "write", "light", "reach", "class", "small", "force", "earth", "truth", "based", "peace", "water", "their", "board", "under", "north", "heart", "learn", "whole", "piece", "power", "story", "earth", "fruit", "think", "guard", "north", "where", "brown", "field", "based", "truth", "crown", "lemon", "bliss", "glory", "draft", "honey", "ocean", "valve", "chaos", "glaze", "crisp", "plush", "blend", "drama", "flair", "pixel", "adore", "rover", "globe", "fleet", "quake", "venom", "witty", "jolly", "covet", "scoop", "dizzy", "gloom", "blast", "chill", "whale", "swirl", "flare", "chant", "sleek", "clown", "penny", "weave", "scout", "roast", "spear", "clasp", "quilt", "vivid", "frank", "pulse", "meadow", "ember", "creep"]

actualword = random.choice(words)

actualword = list(actualword)

a = ""

def gameover():
    print("You have guessed too much and have lost!")
    print("The word was --",actualword)
    print("Now exiting the program")
    quit()

    

while actualword != completingword:
    try:
        a = str(input("Please enter a letter to match the word"))
    except:
        print("Wrong Guess! Try again")
        a = ""

    if a in completingword:
        print("You already guess that letter! Try again")
    elif a == actualword[0]:
        completingword[0] = a
        print("You got some information! Here are the letters that are correct:", completingword)
    elif a == actualword[1]:
        completingword[1] = a
        print("You got some information! Here are the letters that are correct:", completingword)
    elif a == actualword[2]:
        completingword[2] = a
        print("You got some information! Here are the letters that are correct:", completingword)
    elif a == actualword[3]:
        completingword[3] = a
        print("You got some information! Here are the letters that are correct:", completingword)
    elif a == actualword[4]:
        completingword[4] = a
        print("You got some information! Here are the letters that are correct:", completingword)
    else:
        if a in wrong_guesses:
            print("You already guessed that wrong letter! Try again.")

    
        else:
            times += 1
            if times == 1:
                print("The man is now")
                print("O")
                wrong_guesses.append(a)
                print("Wrong guesses are -",wrong_guesses)

            elif times == 2:
                print("The man is now ")
                print("O")
                print("|")
                wrong_guesses.append(a)
                print("Wrong guesses are -",wrong_guesses)

            elif times == 3:
                print("The man is now ")
                print("  O")
                print("--|")
                wrong_guesses.append(a)
                print("Wrong guesses are -",wrong_guesses)

            elif times == 4:
                print("The man is now ")
                print("  O")
                print("--|--")
                wrong_guesses.append(a)
                print("Wrong guesses are -",wrong_guesses)

            elif times == 5:
                print("  O")
                print("--|--")
                print(" /")
                wrong_guesses.append(a)
                print("Wrong guesses are -",wrong_guesses)

            elif times == 6:
                print("The man is now")
                print("  O")
                print("--|--")
                print(" / \\")
                gameover()

    if completingword == actualword:
        print("You won!")  
        print("Exiting...")
        quit()
            