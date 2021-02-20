import random


class Game:
    def __init__(self, mistakecount, predicted_letter, word):
        self.mistakecount = mistakecount
        self.predicted_letter = predicted_letter
        self.word = word

    def letter_presentation(self):  # dislaying the word with full asterisks(*) at first
        word_encry = ''
        for i in range(len(self.word)):
            word_encry = word_encry + '*'

        print(word_encry)
        return word_encry

    def word_encrypter(self, word_encry):  # encrypting the word after user guesses correctly.

        for i in range(len(self.word)):
            if self.word[i] in self.predicted_letter:
                word_encry = word_encry[:i] + self.predicted_letter + word_encry[i + 1:]

        print(word_encry)

        return word_encry

    def currentboard(self):  # displaying the current situation of the board
        width = 20
        flag = 0
        if self.mistakecount == 1:
            print('___'.center(width, ' '))
            print('|'.center(width, ' '))
            print('|'.center(width, ' '))
            print('|'.center(width, ' '))
            print('|'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 2:
            print('/|'.center(width, ' '))
            print('/ |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 3:
            print('/|'.center(width, ' '))
            print('/ |'.center(width, ' '))
            print('O |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 4:
            print('/|'.center(width, ' '))
            print('/ |'.center(width, ' '))
            print('O |'.center(width, ' '))
            print('| |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print(' |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 5:
            print('  /|'.center(width, ' '))
            print(' / |'.center(width, ' '))
            print(' O |'.center(width, ' '))
            print('/| |'.center(width, ' '))
            print('  | |'.center(width, ' '))
            print('   |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 6:
            print('  /|'.center(width, ' '))
            print(' / |'.center(width, ' '))
            print('O  |'.center(width, ' '))
            print('/|\ |'.center(width, ' '))
            print(' |  |'.center(width, ' '))
            print('   |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 7:
            print('  /|'.center(width, ' '))
            print(' / |'.center(width, ' '))
            print('O  |'.center(width, ' '))
            print('/|\ |'.center(width, ' '))
            print(' |  |'.center(width, ' '))
            print('/   |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 0
        elif self.mistakecount == 8:
            print('  /|'.center(width, ' '))
            print(' / |'.center(width, ' '))
            print('O  |'.center(width, ' '))
            print('/|\ |'.center(width, ' '))
            print(' |  |'.center(width, ' '))
            print('/ \ |'.center(width, ' '))
            print('______'.center(width, ' '))
            flag = 1
            print("You are dead\n")
        return flag


def random_word():  # selecting one of the words to be guessed.
    wordList = ["pudding", "baklava", "profiterole", "chocolate", "cake"]
    word = random.choice(wordList)
    return word


print("Welcome to the HangMan Game\n")
flag = 0
rand_word = random_word()
board = Game(0,'',rand_word)
mis_count = 0
word_encry = ''
print(rand_word)
word_encry = board.letter_presentation()
while flag == 0 and mis_count < 8:
    pre_let = input("Please enter a letter\n")
    if pre_let in rand_word:
        board = Game(mis_count, pre_let, rand_word)
        word_encry = board.word_encrypter(word_encry)

    else:
        mis_count = mis_count+1
        board = Game(mis_count, pre_let, rand_word)
        word_encry = board.word_encrypter(word_encry)
    flag = board.currentboard()
    yes_or_no = int(input("Would you like to guess? Press 1 for yes and 2 for no\n"))
    if yes_or_no == 1:
        word_guess = input("Please guess the word")
        if word_guess == rand_word:
            print("You are survived.Congrats...")
            flag = 1
        else:
            print("Try again later...")
            flag = 0
    else:
        flag = 0