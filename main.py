from searchAndRanking import *

import enchant


def correct_spelling(text):
    english_dict = enchant.Dict("en_US")

    words = text.split()

    corrected_words = [english_dict.suggest(
        word)[0] if not english_dict.check(word) else word for word in words]

    corrected_text = ' '.join(corrected_words)

    return corrected_text


userId = 4
query = "horror"
pageNumber = 1
query = correct_spelling(query)
searchAndRank(query, userId)

