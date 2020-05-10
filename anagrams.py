import pandas as pd
from collections import Counter

def find_anagrams(word, dict_file="dict.csv"):
    print("Trying to find anagrams for:", word)
    dict_df = pd.read_csv(dict_file, names = ["Words"])
    lword = word.lower()
    word_set = set(lword)
    word_counter = Counter(lword)
    possible_anagrams = []
    for w in dict_df["Words"].values:
        current_word = str(w).lower()
        if len(current_word) == len(lword):
            if set(current_word) == word_set:
                if Counter(current_word) == word_counter:
                    possible_anagrams.append(current_word)

    print("Possible anagrams are:",possible_anagrams)
    return possible_anagrams

if __name__ == "__main__"
    find_anagrams("alpnE")
