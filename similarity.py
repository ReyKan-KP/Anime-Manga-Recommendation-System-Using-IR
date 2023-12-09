# import numpy as np
# import math
# from collections import defaultdict
# from preprocessingAndIndexing import *


# def weigthcal(indexmap, Stringarr):
#     weighta = {}
#     for token in Stringarr:
#         if token in weighta:
#             continue
#         else:
#             tfa = 1+math.log(count_string_occurrences(token, Stringarr), 2)
#             idfa = math.log(total_doc/(len(indexmap.get(token, {}))+1), 2)
#             weighta[token] = tfa*idfa

#     return weighta


# def weightindex(qweight, indexmap):
#     weightindex = {}
#     for token in qweight:
#         if token in indexmap:
#             idf = math.log(total_doc/(len(indexmap.get(token, {}))+1), 2)
#             for key in indexmap[token]:
#                 tf = 1+math.log(indexmap[token][key], 2)
#                 weightindex.setdefault(key, {})
#                 weightindex[key][token] = tf*idf

#     return weightindex


# def Uweightindex(indexmap):
#     weightindex = defaultdict(dict)

#     for token, doc_dict in indexmap.items():
#         idf = math.log(total_doc / (len(doc_dict) + 1), 2)

#         for key, tf in doc_dict.items():
#             tf_weight = 1 + math.log(tf, 2)
#             weightindex[key][token] = tf_weight * idf

#     return weightindex


# def getMagnitude(vector):
#     return np.linalg.norm(list(vector.values()))


# def Similarity(qweight, weightindex):
#     weightsimilarity = {}

#     qMagnitude = getMagnitude(qweight)

#     for key, doc_vector in weightindex.items():
#         weightMagnitude = getMagnitude(doc_vector)

#         if weightMagnitude == 0 or qMagnitude == 0:
#             weightsimilarity[key] = 0
#         else:
#             common_tokens = set(qweight.keys()) & set(doc_vector.keys())
#             q_vector = np.array([qweight[token] for token in common_tokens])
#             doc_vector = np.array([doc_vector[token]
#                                   for token in common_tokens])

#             weightsimilarity[key] = np.dot(
#                 doc_vector, q_vector) / (weightMagnitude * qMagnitude)

#     return dict(sorted(weightsimilarity.items(), key=lambda item: item[1], reverse=True))
import csv
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
            tfa = 1 + math.log(count_string_occurrences(token, Stringarr), 2)
            idfa = math.log(total_doc / (len(indexmap.get(token, {})) + 1), 2)
            weighta[token] = tfa * idfa

    return weighta


def weightindex(qweight, indexmap):
    weightindex = {}
    for token in qweight:
        if token in indexmap:
            idf = math.log(total_doc / (len(indexmap.get(token, {})) + 1), 2)
            for key in indexmap[token]:
                tf = 1 + math.log(indexmap[token][key], 2)
                weightindex.setdefault(key, {})
                weightindex[key][token] = tf * idf

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
            # print(NormalizedEvalMap[key])
            weightsimilarity[key] = np.dot(
                doc_vector, q_vector) / (weightMagnitude * qMagnitude) + NormalizedEvalMap[key]

    return dict(sorted(weightsimilarity.items(), key=lambda item: item[1], reverse=True))


# file_path = 'main dataset//main.csv'


# def find_normalized_evaluation_by_id(file_path, key):
#     with open(file_path, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if int(row['ID']) == key:
#                 return float(row['Normalized Evaluation'])
#     return None


# def updatedSimilarity(qweight, weightindex):



#     # main_df = pd.read_csv('main dataset//main.csv')

#     # normalized_evaluations = dict(
#     #     zip(main_df['ID'], main_df['Normalized Evaluation']))

#     similarity = Similarity(qweight, weightindex)

#     for key in similarity:
#         normalized_evaluation = find_normalized_evaluation_by_id(file_path, key)
#         similarity[key] += normalized_evaluation

#     return similarity
