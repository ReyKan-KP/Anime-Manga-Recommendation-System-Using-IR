# from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/process_user_input', methods=['POST'])
# def process_user_input():
#     is_existing_user = request.json['isExistingUser']
#     user_id = request.json['userID']
#     query = request.json['query']

#     if user_id == "":
#         user_id = 1

#     result = f"Is Existing User: {is_existing_user}, User ID: {user_id}, Query: {query}"
#     return jsonify({'result': result})


# if __name__ == '__main__':
#     app.run(debug=True)

#app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import csv
import numpy as np

app = Flask(__name__)
CORS(app)

dataset_path = 'main dataset\\main.csv'
user_profiles_path = 'main dataset\\user_profiles.csv'
results_per_page = 10


def get_recommendations(user_id, query):
    with open(dataset_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        data = list(reader)

    descriptions = [row[2] for row in data]
    ids = [row[0] for row in data]
    normalized_evaluations = [float(row[6]) for row in data]

    with open(user_profiles_path, 'r', encoding='utf-8') as user_file:
        user_reader = csv.reader(user_file)
        next(user_reader)
        user_data = list(user_reader)

    user_id_to_exclude = user_id
    watched_or_read = set()
    for user_row in user_data:
        if user_row[0] == user_id_to_exclude and user_row[2] != '[]':
            watched_or_read = set(eval(user_row[2]))

    def get_watch_or_read(user_id):
        with open(user_profiles_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['User ID'] == str(user_id):
                    watch_or_read_str = row['watch or read']
                    watch_or_read_list = eval(watch_or_read_str.replace(
                        "'", "")) if watch_or_read_str else []
                    return watch_or_read_list
        return None

    x = get_watch_or_read(user_id_to_exclude)
    ids_to_exclude = set(map(str, x))

    filtered_data = [row for row in data if row[0]
                     not in watched_or_read and row[0] not in ids_to_exclude]

    descriptions = [row[2] for row in filtered_data]
    ids = [row[0] for row in filtered_data]
    normalized_evaluations = [float(row[6]) for row in filtered_data]

    user_query = re.findall(r'\b\w+\b', query.lower())

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(
        descriptions + [' '.join(user_query)])

    cosine_similarities = cosine_similarity(
        tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    cosine_similarities = np.append(cosine_similarities, [0])
    normalized_evaluations = np.append(normalized_evaluations, [0])

    combined_scores = np.add(cosine_similarities, normalized_evaluations)
    ranking = np.argsort(combined_scores)[::-1]

    start_index = 0
    end_index = start_index + results_per_page

    formatted_results = []
    for i in range(min(results_per_page, len(ranking))):
        index = ranking[i]
        result_entry = {
            'ID': ids[index],
            'Title': filtered_data[index][1],
            'Combined Score': f"{combined_scores[index]:.10f}",
            'Description': filtered_data[index][2],
        }
        formatted_results.append(result_entry)

    return formatted_results


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_user_input', methods=['POST'])
def process_user_input():
    is_existing_user = request.json['isExistingUser']
    user_id = request.json['userID']
    query = request.json['query']

    result = get_recommendations(user_id, query)
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
