import time
import string

s = list (string.ascii_lowercase) 
secretWord = "programming"
lettersGuessed =[]
guessWord =[]

def start():
    print ("Welcome to Hangaroo! Are you gonna kill the kangaroo or let it LIVE? Let's find out!")
    time.sleep(1.0)
start()

def word():
    for i in secretWord:
        guessWord.append("_")
        
    print ("The word you are guessing is related on this subject. You have 5 trials")
    print (' '.join(guessWord))
        
def guess():
    turns = 0
    while turns < 5:
        print ("\n", ' '.join(s))
        IL = input("Letter: \n").lower()
        
        if IL not in s:
            print ("Please enter a letter")
            turns +=1
            print("You made ", turns, "mistake/s. Enter a letter again")
        else:
            lettersGuessed.append(IL)
            
            if IL in secretWord:
                print ("Enter another letter")
                for x in range(0, 11):
                    if secretWord[x] == IL:
                        guessWord[x] = IL
                        print(' '.join(guessWord))
                s.remove(IL)
            else:
                s.remove(IL)
                turns += 1
                print("You made ", turns, "mistake/s.")
            
            if turns == 5:
                print("The kangaroo has been killed. The word was ", secretWord)
                break
        if '_' not in guessWord:
            print("You guessed the word!")
            break              
word()
guess()