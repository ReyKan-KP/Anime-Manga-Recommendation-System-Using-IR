import numpy as np
import math
from collections import defaultdict
from preprocessingAndIndexing import *


def weigthcal(indexmap, Stringarr):
    weighta = {}
    for token in Stringarr:
        if token in weighta:
            continue
        else:
            tfa = 1+math.log(count_string_occurrences(token, Stringarr), 2)
            idfa = math.log(total_doc/(len(indexmap.get(token, {}))+1), 2)
            weighta[token] = tfa*idfa

    return weighta


def weightindex(qweight, indexmap):
    weightindex = {}
    for token in qweight:
        if token in indexmap:
            idf = math.log(total_doc/(len(indexmap.get(token, {}))+1), 2)
            for key in indexmap[token]:
                tf = 1+math.log(indexmap[token][key], 2)
                weightindex.setdefault(key, {})
                weightindex[key][token] = tf*idf

    return weightindex


def Uweightindex(indexmap):
    weightindex = defaultdict(dict)

    for token, doc_dict in indexmap.items():
        idf = math.log(total_doc / (len(doc_dict) + 1), 2)

        for key, tf in doc_dict.items():
            tf_weight = 1 + math.log(tf, 2)
            weightindex[key][token] = tf_weight * idf

    return weightindex


def getMagnitude(vector):
    return np.linalg.norm(list(vector.values()))


def Similarity(qweight, weightindex):
    weightsimilarity = {}

    qMagnitude = getMagnitude(qweight)

    for key, doc_vector in weightindex.items():
        weightMagnitude = getMagnitude(doc_vector)

        if weightMagnitude == 0 or qMagnitude == 0:
            weightsimilarity[key] = 0
        else:
            common_tokens = set(qweight.keys()) & set(doc_vector.keys())
            q_vector = np.array([qweight[token] for token in common_tokens])
            doc_vector = np.array([doc_vector[token]
                                  for token in common_tokens])

            weightsimilarity[key] = np.dot(
                doc_vector, q_vector) / (weightMagnitude * qMagnitude)

    return dict(sorted(weightsimilarity.items(), key=lambda item: item[1], reverse=True))

