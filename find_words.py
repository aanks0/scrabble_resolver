from itertools import permutations
import enchant


# currently, only working for founding word with len(user_letter)
def find_words(user_letter: str):
    full_list_of_words = []
    with open("my_scrabble_dic.txt", "r") as fd:
        full_list_of_words.extend(iter(fd.read().splitlines()))

    user_possible_words = ["".join(possible_words) for possible_words in permutations(user_letter)]
    print(user_possible_words)
    for words in user_possible_words:
        if words.upper() in full_list_of_words:
            print(words)


def find_words_with_enchant(user_letter: str):
    d = enchant.request_pwl_dict("my_scrabble_dic.txt")
    founded_words = set()
    for i in range(len(user_letter) + 1):
        for possible_words in list(permutations(user_letter, i)):
            user_possible_words = "".join(possible_words)
            try:
                if d.check(user_possible_words.upper()):
                    founded_words.add(user_possible_words)
            except ValueError:
                pass

    return sorted(founded_words, key=len)


if __name__ == "__main__":
    find_words_with_enchant("goulioazr")
