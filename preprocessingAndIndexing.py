## preprocessingAndIndexing.py
from collections import defaultdict
import re
import pandas as pd


def preProcess(pattern):
    w = tokenize_without_numbers(pattern)
    w2 = removal_of_stop_words(w, stop_words)
    w3 = stemming(w2)
    return w3


def tokenize_without_numbers(text):
    text = text.strip()
    pattern = r'\b[a-zA-Z]+\b'

    tokens = re.findall(pattern, text)
    newTokens = []
    for token in tokens:
        newTokens.append(token.lower())
    return newTokens


def load_stop_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = set(word.strip() for word in file)
    return stop_words



def removal_of_stop_words(words, stop_words):
    all_words = [w for w in words if w.lower() not in stop_words]
    return all_words


stop_words_path = 'stopwords.txt'

stop_words = load_stop_words(stop_words_path)

stemming_rules = [
    ("sses", "ss"),
    ("ies", "i"),
    ("ss", "ss"),
    ("s", ""),
    ("tions", "t"),
    ("ative", ""),
    ("atives", ""),
    ("ize", ""),
    ("izes", "ize"),
    ("izing", "ize"),
    ("ized", "ize"),
    ("izing", "ize"),
    ("izing", "ize"),
    ("izing", "ize"),
    ("ized", "ize"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("tive", ""),
    ("tives", ""),
    ("ic", ""),
    ("ics", ""),
    ("ical", ""),
    ("ically", ""),
    ("icity", ""),
    ("ionize", "ion"),
    ("ionizes", "ionize"),
    ("ionizing", "ionize"),
    ("ionized", "ionize"),
    ("ional", ""),
    ("ionally", ""),
    ("ioning", "ion"),
    ("ionings", "ioning"),
    ("ioned", "ion"),
    ("ioner", "ion"),
    ("ioners", "ioner"),
    ("ionable", "ion"),
    ("ionables", "ionable"),
    ("ioning", "ion"),
    ("ionings", "ioning"),
    ("ization", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("izational", "ize"),
    ("izationally", "ize"),
    ("izationing", "ize"),
    ("izationings", "ize"),
    ("izations", "ize"),
    ("izationed", "ize"),
    ("izations", "ize"),
    ("ishly", ""),
    ("ishness", ""),
    ("ishnesses", "ishness"),
    ("ism", ""),
    ("ist", ""),
    ("istic", ""),
    ("istically", ""),
    ("istical", "ist"),
    ("istically", "ist"),
    ("istical", "ist"),
    ("istication", "ist"),
    ("istications", "istication"),
    ("isticated", "isticate"),
    ("isticate", "ist"),
    ("istically", "ist"),
    ("istical", "ist"),
    ("isticatedly", "isticate"),
    ("isticatedness", "isticate"),
    ("istication", "isticate"),
    ("istications", "isticate"),
    ("evening", "evening"),
    ("morning", "morning"),
    ("ism", ""),
    ("isms", "ism"),
    ("ist", ""),
    ("ist", ""),
    ("ists", "ist"),
    ("ist", ""),
    ("ist", ""),
    ("ists", "ist"),
    ("ist", ""),
    ("al", ""),
    ("ally", ""),
    ("al", ""),
    ("ally", ""),
    ("ed", ""),
    ("ing", ""),
    ("er", ""),
    ("or", ""),
    ("ar", ""),
    ("ary", ""),
    ("ery", ""),
    ("ful", ""),
    ("less", ""),
    ("ness", ""),
    ("ship", ""),
    ("sion", ""),
    ("tion", "t"),
    ("ive", ""),
    ("ize", ""),
    ("izing", "ize"),
    ("ized", "ize"),
    ("al", ""),
    ("ally", ""),
    ("ed", ""),
    ("ing", ""),
    ("er", ""),
    ("or", ""),
    ("ar", ""),
    ("ary", ""),
    ("ery", ""),
    ("ful", ""),
    ("less", ""),
    ("ness", ""),
    ("ship", ""),
    ("sion", ""),
    ("tion", "t"),
    ("ive", ""),
    ("ize", ""),
    ("izing", "ize"),
    ("ized", "ize"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("ise", ""),
    ("ises", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("ise", ""),
    ("ises", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("ise", ""),
    ("ises", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("ise", ""),
    ("ises", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("ate", ""),
    ("en", ""),
    ("ify", ""),
    ("ise", ""),
    ("ises", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ising", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ised", "ise"),
    ("ish", ""),
    ("ism", ""),
    ("ist", ""),
    ("al", ""),
    ("tive", ""),
    ("tives", ""),
    ("ic", ""),
    ("ics", ""),
    ("ical", ""),
    ("ically", ""),
    ("icity", ""),
    ("ionize", "ion"),
    ("ionizes", "ionize"),
    ("ionizing", "ionize"),
    ("ionized", "ionize"),
    ("ional", ""),
    ("ionally", ""),
    ("ioning", "ion"),
    ("ionings", "ioning"),
    ("ioned", "ion"),
    ("ioner", "ion"),
    ("ioners", "ioner"),
    ("ionable", "ion"),
    ("ionables", "ionable"),
    ("ioning", "ion"),
    ("ionings", "ioning"),
    ("ization", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("izational", "ize"),
    ("izationally", "ize"),
    ("izationing", "ize"),
    ("izationings", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("izationed", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("izations", "ize"),
    ("ish", ""),
    ("ishly", ""),
    ("ishness", ""),
    ("ishnesses", "ishness"),
    ("ism", ""),
    ("ist", ""),
    ("istic", ""),
    ("istically", ""),
    ("istical", "ist"),
    ("istically", "ist"),
    ("istical", "ist"),
    ("istication", "ist"),
    ("istications", "istication"),
    ("isticated", "isticate"),
    ("isticate", "ist"),
    ("istically", "ist"),
    ("istical", "ist"),
    ("isticatedly", "isticate"),
    ("isticatedness", "isticate"),
    ("isticatednesses", "isticatedness"),
    ("istication", "isticate"),
    ("istications", "isticate"),
    ("ism", ""),
    ("isms", "ism"),
    ("ist", ""),
    ("ist", ""),
    ("ists", "ist"),
    ("ist", ""),
    ("ist", ""),
    ("ists", "ist"),
    ("ist", ""),
    ("ational", "ate"),
    ("tional", "tion"),
    ("enci", "ence"),
    ("anci", "ance"),
    ("izer", "ize"),
    ("alli", "al"),
    ("entli", "ent"),
    ("eli", "e"),
    ("ousli", "ous"),
    ("ization", "ize"),
    ("ation", "ate"),
    ("ator", "ate"),
    ("alism", "al"),
    ("iveness", "ive"),
    ("fulness", "ful"),
    ("ousness", "ous"),
    ("aliti", "al"),
    ("iviti", "ive"),
    ("biliti", "ble"),
    ("icate", "ic"),
    ("ative", ""),
    ("alize", "al"),
    ("iciti", "ic"),
    ("ical", "ic"),
    ("ful", ""),
    ("ness", ""),
    ("al", ""),
    ("ance", ""),
    ("ence", ""),
    ("er", ""),
    ("ic", ""),
    ("able", ""),
    ("ible", ""),
    ("ant", ""),
    ("ement", ""),
    ("ment", ""),
    ("ent", ""),
    ("ou", ""),
    ("ism", ""),
    ("ate", ""),
    ("iti", ""),
    ("ous", ""),
    ("ive", ""),
    ("ize", ""),

]


def stemming(all_words):
    stemmed_word = []
    for w in all_words:
        for rules in stemming_rules:
            suffix, replace = rules
            if w.endswith(suffix):
                w = w[:-len(suffix)] + replace
        stemmed_word.append(w)
    return stemmed_word

# preProcess("By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.")


inverted_index = defaultdict(dict)

data = pd.read_csv('main dataset/main.csv')
userData = pd.read_csv('main dataset/user_profiles.csv')


def count_string_occurrences(string, array_of_strings):
    count = 0
    for string_in_array in array_of_strings:
        if string_in_array == string:
            count += 1
    return count


inverted_index = defaultdict(dict)
terms = []
tokenindex = []


def makeIndex():
    if 'Description' in data.columns:
        for index, row in data.iterrows():
            document = str(row['Description'])
            predoc = preProcess(document)
            tokenindex.append(predoc)
            terms = list(set(terms + predoc))

    else:
        print("The 'text' column does not exist in the CSV file. Please check the column name.")

    with open("index.txt", "w") as file:
        for term in terms:
            di = []
            i = 0
            for i in range(len(tokenindex)):
                if term in tokenindex[i]:
                    # tf=tf.get(term,0)+1
                    docid = str(i+1)
                    tf = count_string_occurrences(term, tokenindex[i])
                    di.append("({}, {})".format(str(docid), str(tf)))
            ditf = "{} -> {}\n".format(term, ", ".join(map(str, di)))
            file.write(ditf)


total_doc = 0
indexmap = 0
NormalizedEvalMap=[]

import pandas as pd


def getNormalizedEvaluation(csv_file):
    df = pd.read_csv(csv_file)
    NormalizedEval = dict(zip(df['ID'], df['Normalized Evaluation']))
    return NormalizedEval

NormalizedEvalMap = getNormalizedEvaluation('main dataset//main.csv')
# Now you can access values using NormalizedEvalMap[1]
# print(NormalizedEvalMap)



def makeindexmap():
    global total_doc
    term_doc_freq_map = defaultdict(dict)

    with open('index.txt', 'r') as file:
        for line in file:
            term, doc_freq_part = map(str.strip, line.split('->'))
            doc_freq_pairs = [pair.strip('()')
                              for pair in doc_freq_part.split('), ')]

            for pair in doc_freq_pairs:
                parts = pair.strip('()').split(', ')

                try:
                    doc_id, freq = map(int, parts)
                    term_doc_freq_map[term][doc_id] = freq

                    if total_doc < doc_id:
                        total_doc = doc_id
                except ValueError:
                    print(f"Error parsing pair: {pair}")
    # print(total_doc)
    return term_doc_freq_map



indexmap = makeindexmap()
