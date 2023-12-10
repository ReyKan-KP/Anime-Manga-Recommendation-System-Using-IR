# Anime/Manga Recommendation System with IR Algorithm

This Flask-based Anime/Manga recommendation system utilizes an IR
similarity algorithm to provide personalized suggestions based on user
preferences, including descriptions, ratings, interactions, and viewing
history. Built with Flask, it features document search, ranking, spell
correction, and user feedback, offering Anime/Manga enthusiasts a
comprehensive platform for seamless content discovery.

## Table of Contents

-   [Description](##Description)
-   [Installation](##Installation)
-   [Run the Application](##RunthApplication)
-   [Usage](##Usage)
-   [Components](##Component)
-   [Features](##Features)
-   [Contributing](##Contributing)
-   [License](##License)
-   [Note](##Note)

## Description

This web application serves as an information retrieval system for
Anime/Manga recommendations, integrating features that enable users to
input their preferences and receive personalized suggestions. The system
leverages an Information Retrieval (IR) similarity algorithm to match
user preferences with Anime/Manga in the dataset. Recommendations are
generated based on various factors, including anime/manga descriptions,
ratings, user interactions, and the user's viewing history.

Built with Flask, the application also incorporates functionalities such
as document search and ranking, spell correction for user queries, and a
user feedback system. Users can explore and interact with the system
through a web-based interface.

This integration offers a comprehensive platform for Anime/Manga
enthusiasts, providing a seamless experience for discovering new content
tailored to their tastes. Whether users are seeking recommendations
based on descriptions, ratings, or personal viewing history, the system
aims to enhance the overall Anime/Manga discovery process.

## Installation

1.  **Clone the repository :**

    ``` bash
    git clone https://github.com/ReyKan-KP/Anime-Manga-Recommendation-System-Using-IR.git
    ```

2.  **Install dependencies :**

    ``` bash
    pip install -r requirements.txt
    ```

## Run the Application

1.  **Run main.py :**

    ``` bash
    python main.py runserver
    ```

2.  **Open index.html:**
    `Click on http://127.0.0.1:5000 (as shown in  terminal)`

## Usage

1.  Execute the script and follow the link to access the Anime/Manga
    Recommendation page.
2.  Specify your user status:
    -   If you're an existing user,Select Yes and provide your User ID
        (greater than 1).
    -   If you're a guest,Select No then the User ID is set to 1.
3.  Based on your input, you can:
    -   Enter the description of the Anime/Manga you wish to explore.
    -   Receive recommendations based on the previous user's watched or
        read list (weighted terms of the user watch or read document are
        considered, and cosine similarity is calculated based on the
        resulting weight index).
4.  Enter the Page Number and click submit.
5.  Review the ranking determined by the combined score (cosine
    similarity + normalized evaluation).
    -   Normalized evaluation is calculated as (evaluation/totalDocs) \*
        100, where evaluation is the product of feedback and rating.
6.  In the feedback box, enter relevant document IDs following the
    provided instructions.
7.  Upon submitting feedback, the feedback count for the specified
    document ID will increment by 1, and the normalized evaluation will
    be updated in the dataset.
8.  For the Assessment of the IR system, a PR curve and an 11-point
    interpolated precision graph will be displayed for the top 10
    documents based on the relevance document entered by the user in the
    feedback box.
9.  For a new query or recommendation, reload the page.

## Components

1.  ### DataSet - Collected from My Anime List dataset from Kaggle

    -   **main.csv**

        -   This CSV file contains a list of 87,316 anime/manga entries.
        -   **Path:** `main dataset/main.csv`
        -   **Columns:**
            `ID, Title, Description, Rating, Feedback, Evaluation, Normalized Evaluation`

    -   **user_profiles.csv**

        -   This CSV file contains a list of 75,989 user profiles.
        -   **Path:** `main dataset/user_profiles.csv`
        -   **Columns:** `User ID, Profile, Watch or Read`

2.  ### PreProcessing

    -   **Lowercasing:**
        -   Converts all text to lowercase to ensure consistency and
            avoid case-sensitive discrepancies.
    -   **Tokenization:**
        -   Breaks down sentences or paragraphs into individual words or
            tokens, essential for text-based analysis.
    -   **Stopwords Removal:**
        -   Removes common words (stopwords) that do not contribute
            significantly to the meaning of the text, reducing noise in
            the data.
    -   **Stemming:**
        -   Reduces words to their base or root form, grouping together
            words derived from the same root, even with different
            inflections or suffixes.

3.  ### Indexing

    -   **Index File Format:**

        -   **Path:** `index.txt`
        -   The index file is a `.txt` file storing term information in
            the format: `term - (doc_id, term_frequency)`.

    -   **Indexer Function:**

        -   The `makeIndex()` function is crucial for indexing
            anime/manga descriptions, processing each description and
            creating entries in the index file.

    -   **Index Loading:**

        -   At runtime, the program loads the `index.txt` file to access
            the pre-built index.

    -   **makeIndexMap() Function:**

        -   The `makeIndexMap()` function generates a dictionary
            containing term, doc_ID, and frequency without reading the
            entire document.

4.  ### Search and Ranking

    -   **Types of Search:**

        1.  **Query Search:**
            -   Involves searching based on user-provided queries.
        2.  **Recommendation Search:**
            -   Provides recommendations based on the user's watch/read
                history.

    -   **Term Frequency Calculation:**

        -   Term frequency is calculated using the formula:
            `1 + log2(tf)`.

    -   **Inverse Document Frequency Calculation:**

        -   Inverse Document Frequency (IDF) is calculated as:
            `1 + log2(total_Doc/Doc_freq)`.

    -   **Weight Index:**

        -   The weight index for each term is determined by multiplying
            the term frequency (tf) and inverse document frequency
            (idf): `tf * idf`.

    -   **Recommendation Search Workflow:**

        1.  **User Watch/Read History:**
            -   The system gathers the watch/read history of the user.
        2.  **Weight Index Calculation:**
            -   Calculates the weight index of each document that the
                user has watched/read.
        3.  **Query Weight Index:**
            -   Obtains the query weight index by summing the weight
                indices of the user's watch/read history.
        4.  **Cosine Similarity:**
            -   Calculates cosine similarity to determine the similarity
                between each document's weight index and the query
                weight index.

    -   **Cosine Similarity:**

        -   Measures the cosine of the angle between two vectors,
            providing a similarity score.

    -   **Search Optimization:**

        -   Utilizes weighted indices, term frequency, and inverse
            document frequency for accurate and relevant search results.
        -   Cosine similarity ensures efficient comparison and ranking
            of documents based on their relevance.

    -   **Result Presentation:**

        -   Presents search results in a ranked order, with higher
            cosine similarity scores indicating higher relevance.

5.  ### Spell Checking

    -   The `correct_spelling` function is a spell checker designed to
        identify and correct misspelled words in a given query.
    -   **Library Used:** The function utilizes the `enchant` library,
        specifically the English (U.S.) dictionary, to check word
        spelling.
    -   **Input:** Accepts a query (text) string as input.
    -   **Processing:**
        -   Splits the input query into individual words.
        -   Checks if each word is misspelled using the `enchant`
            dictionary.
        -   If misspelled, suggests a correction using the first
            suggestion from the dictionary.
        -   Assembles corrected words into a new query string.
    -   **Output:** Returns the corrected query.

6.  ### Feedback

    -   **Feedback IDs Extraction:**
        -   The system accepts a list of feedback IDs from the user,
            obtained from the JSON payload using
            `request.json.get('feedbackIDs', [])`.
    -   **Feedback Function:**
        -   The `feedback()` function processes received feedback IDs,
            updating the dataset by incrementing feedback count,
            recalculating evaluation based on rating, and computing
            normalized evaluation. The updated dataset is saved to 'main
            dataset/main.csv', and feedback IDs are printed for
            confirmation.
    -   **Normalized Evaluation Map:**
        -   The function retrieves the normalized evaluation map using
            the `getNormalizedEvaluation` function from the
            'preprocessingAndIndexing' module.
    -   By incorporating this feedback component, the system allows
        users to provide feedback on specific IDs, updating the dataset
        for continuous improvement in recommendations or search results.

7.  ### Assessment: Information Retrieval (IR) Evaluation

    -   **Precision-Recall Curve Generation:**
        -   The `PRcurve` module generates Precision-Recall curves to
            evaluate the performance of the Information Retrieval (IR)
            system.
    -   **PRcurve Function:**
        -   Takes parameters including total_docs, relevant_docs_id, and
            top_10 to calculate precision and recall at each rank in the
            top 10. Interpolation is applied, and the resulting curve is
            plotted using Matplotlib.
    -   **Workflow:**
        1.  **Relevance Annotation:**
            -   Determines the relevance of each document in the top 10
                based on provided relevant document IDs.
        2.  **Precision and Recall Calculation:**
            -   Calculates precision and recall at each rank, providing
                insights into system performance.
        3.  **Interpolation:**
            -   Interpolates precision values at 11 recall levels,
                producing a smooth Precision-Recall curve.
        4.  **Curve Plotting:**
            -   Plots the Precision-Recall curve for visualization.
    -   **Result Interpretation:**
        -   Precision and recall values breakdown the performance at
            each rank in the top 10.
        -   Interpolated precision values offer a comprehensive view of
            the system's behavior across different recall levels, aiding
            in evaluation and comparison of retrieval strategies.

8.  ### User Interface (UI) Component

    The UI component of the Anime/Manga Recommendation System employs
    Flask, HTML, CSS, and JavaScript for an interactive user experience.
    Key elements include a spell checker, Flask routes for processing
    user input and feedback, HTML templates, and JavaScript for user
    interactions.

    1.  **Components**

        1.  **Spell Checker :**

            -   The `correct_spelling` function corrects misspelled
                words using the `enchant` library.

        2.  **Flask Routes :**

            -   `/`: Renders the main HTML page.
            -   `/process_user_input`: Processes user queries and
                recommendations.
            -   `/process_feedback_input`: Handles user feedback.

        3.  **HTML Templates :**

            -   The main template (`index.html`) defines the UI
                structure, including forms, loading indicators, and
                result containers.

        4.  **JavaScript Interaction:**

            -   JavaScript functions handle user interactions like user
                type selection, entering IDs, and form submissions.

    2.  **User Interaction Workflow**

        1.  **User Type Selection:**

            -   Users choose existing or guest status.

        2.  **User ID and Options:**

            -   For existing users, ID entry and dynamic options for
                query or recommendations are provided.

        3.  **Query and Page Input:**

            -   Users enter queries or page numbers.

        4.  **Search Execution:**

            -   Clicking search triggers Flask to process input and
                display results.

        5.  **Feedback Submission:**

            -   Users can submit feedback, updating the system dataset.

    3.  **Loading and Feedback**

        -   Loading indicators signal ongoing processes.
        -   Feedback prompts are presented after search results for user
            contribution.

## Features

1.  **Data collection for comprehensive content coverage.**

2.  **Preprocessing for data optimization**

3.  **Indexing for efficient data retrieval.**

4.  **Document search and ranking.**

    -   **Search based on user query.**
    -   **Recommendation based on user's previous watch or read
        history.**

5.  **Spell correction for user queries.**

6.  **User feedback handling.**

7.  **Assessment Evaluation with PR Curve.**

8.  **Web-based interface using Flask.**

## Contributing

We welcome contributions from the community! If you'd like to contribute
to this project, here's how:

### To contribute, follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/your-feature-name`).
5.  Open a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Note

-   Make sure to have the necessary CSV files ('main dataset\\main.csv'
    and 'main dataset\\user_profiles.csv') in the specified directory
    for data retrieval.

This README provides an overview of the Anime Recommendation System. For
more details on the code and functionality, please refer to the code
comments and documentation within the script.
