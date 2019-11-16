def getGuessedWord(secretWord, lettersGuessed):

    word = " "
    
    for x in secretWord:
        if x in letterGuessed:
            word += x
        else:
            word+= "_"
        
        return 
    print ()