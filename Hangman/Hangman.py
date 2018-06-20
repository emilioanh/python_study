from PickAWord import pick_a_word
from GuessLetter import guess_letter

def draw_hang_man(inc_guess):
    print("+=====+")
    print("|     |")
    if inc_guess>0:
        print("|     O")
    else:
        print("|      ")
    if inc_guess>1:
        if inc_guess==2:
            print("|     |")
        elif inc_guess==3:
            print("|    /|")
        else:
            print("|    /|\\ Fucking die soon t.t")
    else:
        print("|      ")
    if inc_guess>4:
        if inc_guess==5:
            print("|    / ")
        else:
            print("|    / \\")
    else:
        print("|      ")
    print("|      ")

if __name__ == "__main__":
    while True:
        inc_guess = 0
        guess_word = pick_a_word()
        result = list('_'*len(guess_word))
        guessed_letter = []
        print(guess_word)
        print("Fuckin' welcome to Hangman!")
        while inc_guess<6:
            letter = input("Input your guess letter:")
            indices = guess_letter(letter, guess_word, guessed_letter)
            if indices:
                for index in indices:
                    result[index] = letter.upper()
                print(''.join(result))
            else:
                if indices!=0:
                    print("Your guess is wrong!")
                    inc_guess += 1
                    draw_hang_man(inc_guess)
            if '_' not in result:
                print("Congratulations, you have won the game!")
                break
        opt = input("Do you want to cont(y/n)?")
        if opt.lower() in ["no",'n']:
            break