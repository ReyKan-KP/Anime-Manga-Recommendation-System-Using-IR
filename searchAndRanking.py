from similarity import *


## Merge Documents


def mergedoc_user(read, uweight):
    weight = {}
    for doc in read:
        for token in uweight[doc]:
            if token in weight:
                weight[token] += uweight[doc][token]
            else:
                weight[token] = uweight[doc][token]

    return weight

## Get Document from UserID

import csv
import ast


def extract_watch_or_read(user_id, csv_file):
    watch_or_read_list = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['User ID']) == user_id:
                watch_or_read_list = [
                    int(item) for item in ast.literal_eval(row['watch or read'])]
                break

    return watch_or_read_list

## Get Name of Document from ID

import time
import pandas as pd


# def get_document_names(csv_file, doc_ids):
#     try:
#         df = pd.read_csv(csv_file)
#     except FileNotFoundError:
#         print(f"Error: File not found - {csv_file}")
#         return None
#     except pd.errors.EmptyDataError:
#         print(f"Error: Empty DataFrame - {csv_file}")
#         return None
#     except pd.errors.ParserError:
#         print(f"Error: Unable to parse CSV - {csv_file}")
#         return None

#     if 'ID' not in df.columns:
#         print("Error: 'ID' column not found in the DataFrame.")
#         return None

#     filtered_df = df[df['ID'].isin(doc_ids)]

#     id_to_name = dict(zip(filtered_df['ID'], filtered_df['Title']))

#     return id_to_name


def get_document_info(csv_file, doc_ids):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: File not found - {csv_file}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: Empty DataFrame - {csv_file}")
        return None
    except pd.errors.ParserError:
        print(f"Error: Unable to parse CSV - {csv_file}")
        return None

    if 'ID' not in df.columns:
        print("Error: 'ID' column not found in the DataFrame.")
        return None

    filtered_df = df[df['ID'].isin(doc_ids)]

    id_to_info = dict(zip(filtered_df['ID'], zip(
        filtered_df['Title'], filtered_df['Description'])))

    return id_to_info
## Searching and Ranking
time.sleep(2)


def userRecommendation(read):
    uweight = Uweightindex(indexmap)
    qweigth = mergedoc_user(read, uweight)
    sim = Similarity(qweigth, uweight)
    return sim


def searchQuery(query):
    queryToken = preProcess(query)
    qweigth = weigthcal(indexmap, queryToken)
    weightindexa = weightindex(qweigth, indexmap)
    sim = Similarity(qweigth, weightindexa)
    return sim

# def searchAndRank(query,userID):
#     if query == "":
#         csv_file_path = 'main dataset//user_profiles.csv'
#         read = extract_watch_or_read(userID, csv_file_path)
#         start_time = time.time()
#         sim = userRecommendation(read)
#         end_time = time.time()
#     else:
#         start_time = time.time()
#         sim = searchQuery(query)
#         end_time = time.time()
#     top_10 = dict(list(sim.items())[:10])
#     print(top_10)

#     csv_file_path_main = 'main dataset//main.csv'
#     doc_names_dict = get_document_names(csv_file_path_main, top_10)

#     for doc_id, similarity_score in top_10.items():
#         doc_name = doc_names_dict.get(doc_id, "Name not found")

#         print(
#             f'Doc ID: {doc_id}, Name: {doc_name}, Similarity: {similarity_score}')

#     print(f"Total time for Searching is {end_time-start_time}")

# def searchAndRank(query, userID,pageNo):
#     if query == "":
#         csv_file_path = 'main dataset//user_profiles.csv'
#         read = extract_watch_or_read(userID, csv_file_path)
#         start_time = time.time()
#         sim = userRecommendation(read)
#         end_time = time.time()
#     else:
#         start_time = time.time()
#         sim = searchQuery(query)
#         end_time = time.time()

#     top_10 = dict(list(sim.items())[:10])

#     csv_file_path_main = 'main dataset//main.csv'
#     doc_info_dict = get_document_info(csv_file_path_main, top_10)

#     results_table = "<table border='1'><tr><th>Ranking</th><th>ID</th><th>Name</th><th>Combined Similarity Score</th><th>Description</th></tr>"

#     for rank, (doc_id, similarity_score) in enumerate(top_10.items(), start=1):
#         doc_info = doc_info_dict.get(
#             doc_id, ("Name not found", "Description not found"))
#         doc_name, doc_description = doc_info

#         results_table += f"<tr><td>{rank}</td><td>{doc_id}</td><td>{doc_name}</td><td>{similarity_score}</td><td>{doc_description}</td></tr>"

#     results_table += "</table>"

#     print(results_table)
#     print(f"Query: {query}")
#     print(f"User ID: {userID}")

#     print(f"Total time for Searching is {end_time - start_time}")

#     return results_table


def searchAndRank(query, userID, pageNo):
    if query == "":
        csv_file_path = 'main dataset//user_profiles.csv'
        read = extract_watch_or_read(userID, csv_file_path)
        start_time = time.time()
        sim = userRecommendation(read)
        end_time = time.time()
    else:
        start_time = time.time()
        sim = searchQuery(query)
        end_time = time.time()

    results_per_page = 10
    start_index = (pageNo - 1) * results_per_page
    end_index = pageNo * results_per_page

    top_10 = dict(list(sim.items())[start_index:end_index])

    csv_file_path_main = 'main dataset//main.csv'
    doc_info_dict = get_document_info(csv_file_path_main, top_10)

    results_table = "<table border='1'><tr><th>Ranking</th><th>ID</th><th>Name</th><th>Combined Similarity Score(similarity+normalized evaluation)</th><th>Description</th></tr>"

    for rank, (doc_id, similarity_score) in enumerate(top_10.items(), start=start_index + 1):
        doc_info = doc_info_dict.get(
            doc_id, ("Name not found", "Description not found"))
        doc_name, doc_description = doc_info

        results_table += f"<tr><td>{rank}</td><td>{doc_id}</td><td>{doc_name}</td><td>{similarity_score}</td><td>{doc_description}</td></tr>"

    results_table += "</table>"

    print(results_table)
    print(f"Query: {query}")
    print(f"User ID: {userID}")
    print(f"Page Number: {pageNo}")

    print(f"Total time for Searching is {end_time - start_time}")

    return results_table
