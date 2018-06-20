def guess_letter(letter, word, guessed_letters):
    temp_word = list(word)
    temp_guess = ['_' for i in range(len(temp_word))]
    indices = []
    while True:
        if letter.upper() in guessed_letters:
            print("Already guessed!")
            break
        elif letter.upper() in temp_word:
            index =  temp_word.index(letter.upper())
            temp_word[index] = '_'
            indices.append(index)
        else:
            guessed_letters.append(letter.upper())
            return indices
    return 0

if __name__ == "__main__":
    guessed_letter = []
    a = guess_letter('e', "EVAPORATE", ['E'])
    if a:
        print(a)
    else:
        print(a)
        print("empty")