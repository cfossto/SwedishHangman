import random

print("\n Välkommen! Här gissar vi bokstäver till det blir rätt..")
print("             ..annars hänger vi den djefeln!.. \n \n")
print("För att avsluta: Skriv 'exit' i lösningen nedan")


## Main Game Loop
main_loop = True
while main_loop == True:

    game = True

    game_tries = 3

    words = ['test','low','christmas']
    word_list_length = len(words)

    random_number = random.randrange(0,word_list_length)

    solution = words[random_number]
    solution_list = list(solution)
    solution_list_length = len(solution_list)
    
    #Wordhint-format
    word_hint = solution_list_length*"_"
    word_hint_list = list(word_hint)

    throw_list = list(solution)

    #Exit functionality
    if solution == "exit":
        print("___Tack för att du spelade!___")
        main_loop = False





    ## Start game
    while game == True and main_loop == True:
        print("\nDu har just nu "+str(game_tries)+" försök.")
        print("\nHint: ")
        for x in word_hint_list:
            print(x,end="")

        guess = input("\nTesta en bokstav: ").lower()

        # Sanitize input. One char only. Only from the alphabet.
        while len(guess) == 0 or len(guess)>1 or not guess.isalpha():
            guess = input("Bara en Bokstav krävs. Testa en bokstav: ")
  
        counter = 0
        # Find character in word
        for character in throw_list:
            if character == guess:
                position = throw_list.index(character)
                # Throw list switch
                throw_list.pop(position)
                throw_list.insert(position,"_")
                # Word hint list switch
                word_hint_list.pop(position)
                word_hint_list.insert(position,guess)
            
        if solution.find(guess) <0:
            game_tries -= 1


        theWord = ""

        if len(word_hint_list) == len(solution):
            for x in word_hint_list:
                theWord += x
        
        if theWord == solution:
            print("\n ___Rätt svar: "+ theWord+"___")
            print("\n ___Du vann! Spela igen?___")
            game = False
            

        if game_tries == 0:
            print("Game over")
            solution = ""
            game = False
