import random

#A list of possible words, 2 empty lists, and the ammount of lives the player has
word=random.choice([
    "alert",
    "boost",
    "carry",
    "dance",
    "early",
    "fault",
    "globe",
    "happy",
    "issue",
    "juice",
    "known",
    "light",
    "mixer",
    "novel",
    "arise",
    "brain",
    "child",
    "dream",
    "enjoy",
    "field",
    "grand",
    "house",
    "input",
    "joint",
    "knock",
    "level",
    "meals",
    "noise",
    "actor",
    "brown",
    "close",
    "drive",
    "empty",
    "flash",
    "great",
    "human",
    "index",
    "jelly",
    "knife",
    "leave",
    "marry",
    "newly",
    "adult",
    "built",
    "count",
    "drink",
    "enter",
    "fluid",
    "gross",
    "heavy",
    "image",
    "jeans",
    "kills",
    "learn",
    "magic",
    "night"
])
guessed=[]
wrong=[]
lives=10

while True:
    #Controlling what words you've guess right and wrong
    out=""
    for a in word:
        #Puts a letter in out if it's the same letter in both the word and guessed
        if a in guessed:
            out+=a
        #Puts a _ for every letter you haven't guessed
        else:
            out+="_"
    
    print(out)
    print(f"You have {lives} lives left.")
    
    #The part that lets you try to guess the word
    if out!=word:
        guess=input("Guess a letter: ")
        if guess in guessed or guess in wrong:
            print("It's already guessed.")
        elif guess==word:
            print("You guessed the word!")
            out=guess #If you guessed the word out will become your guess
        elif guess in word:
            print("yes")
            guessed.append(guess) #Puts guess in guessed list
        else:
            print("no")
            wrong.append(guess) #Puts guess in wrong list
            lives-=1
    
    #When you win or lose this will happen
    if out==word:
        print("You won!")
        break
    elif lives==0:
        print(f"You lost, the word was '{word}'.")
        break

input()
