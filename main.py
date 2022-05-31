import os
from time import sleep

from find_words import find_words_with_enchant,find_words
from get_words import init_scrabble_dictionary

if __name__ == "__main__":
    folder_name = os.path.dirname(__file__)
    if "my_scrabble_dic.txt" in os.listdir(folder_name):
        print("Dictionary found, can continue ...")
    else:
        print("Dictionary not found, it will be generating now")
        sleep(3)
        init_scrabble_dictionary()

    words = find_words_with_enchant(input("Enter your letters: "))
    print("Find below the word you can do with the letters you enter :")
    for word in words:
        print(word)



