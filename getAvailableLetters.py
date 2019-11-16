import string
def getAvailableLetters(lettersGuessed):
    
    s = list (string.ascii_lowercase)
    
    for x in lettersGuessed:
        s.remove(x)
        
    print (s)