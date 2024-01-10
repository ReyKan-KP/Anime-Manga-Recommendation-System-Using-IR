from flask_cors import CORS
from flask import Flask, render_template, request, jsonify, render_template_string
from searchAndRanking import *
import enchant
# import webbrowser
from feedback import *
from PRcurve import *

# main.py


def correct_spelling(text):
    english_dict = enchant.Dict("en_US")

    words = text.split()

    corrected_words = [english_dict.suggest(
        word)[0] if not english_dict.check(word) else word for word in words]

    corrected_text = ' '.join(corrected_words)
    if corrected_text != text:
        print("Did you mean: " + corrected_text + "?")
    return corrected_text


# userId = 4
# query = ""
# query = correct_spelling(query)
# searchAndRank(query, userId)

# feedbackIDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8729]
# feedback(feedbackIDs)


app = Flask(__name__)
CORS(app)

# browser_opened = False

# if not browser_opened:
#     webbrowser.open_new_tab('http://127.0.0.1:5500/index.html')
#     browser_opened = True

@app.route('/')
def index():
    return render_template('index.html')

top_10=[]

@app.route('/process_user_input', methods=['POST'])
def process_user_input():
    global top_10
    is_existing_user = request.json['isExistingUser']
    userID = request.json['userID']
    query = request.json['query']
    pageNo = request.json['pageNo']

    if userID == "":
        userID = 1
    else:
        userID = int(userID)
    if pageNo == "":
        pageNo = 1
    else:
        pageNo = int(pageNo)
    correctedQuery = correct_spelling(query)

    did_you_mean = ""
    if correctedQuery != query:
        did_you_mean = "Did you mean " + '<span class = green>' + correctedQuery + "</span>?" + \
            '<br>'+'showing results for <span class = green>' + \
            correctedQuery+'</span> instead of <span class = red>'+query+'</span>'
        search_results_table, top_10 = searchAndRank(correctedQuery, userID, pageNo)
    else:
        search_results_table, top_10 = searchAndRank(query, userID, pageNo)

    return render_template_string(
        '''
        <center>
        <h1>Results</h1>
        <div id="result-container"><sub>{{ did_you_mean | safe }}</sub></div>
        <div id="result-container">{{ result | safe }}</div>
        </center>
        ''',
        did_you_mean=did_you_mean,
        result=search_results_table
    )


@app.route('/process_feedback_input', methods=['POST'])
def process_feedback_input():

    feedback_ids = request.json.get('feedbackIDs', [])

    feedback_ids = [int(fid) for fid in feedback_ids]

    feedback(feedback_ids)
    PRcurve(total_doc,feedback_ids,top_10)

    return jsonify(success=True, message="<h2>Feedback processed successfully")


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
