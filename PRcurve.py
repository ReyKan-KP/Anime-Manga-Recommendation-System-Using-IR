# PRcurve.py
import matplotlib.pyplot as plt


def PRcurve(total_docs, relevant_docs_id, top_10):

    relevant_docs = len(relevant_docs_id)
    # total_docs = 100
    print("PR curve Starts from here")
    print(total_docs)
    print(relevant_docs_id)
    ranked_list = []
    for doc_id in top_10:
        if doc_id in relevant_docs_id:
            ranked_list.append({"DocID": doc_id, "Relevance": 1})
        else:
            ranked_list.append({"DocID": doc_id, "Relevance": 0})

    precision_values = []
    recall_values = []

    relevant_in_top_n = 0
    retrieved_relevant = 0

    for i, entry in enumerate(ranked_list):
        if entry["Relevance"] == 1:
            retrieved_relevant += 1

        precision = retrieved_relevant / (i + 1)
        recall = retrieved_relevant / relevant_docs

        precision_values.append(precision)
        recall_values.append(recall)

    # Interpolating 11 points
    interpolated_precision = []
    recall_levels = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    for level in recall_levels:
        max_precision = 0
        for recall_val, precision_val in zip(recall_values, precision_values):
            if recall_val >= level:
                max_precision = max(max_precision, precision_val)
        interpolated_precision.append(max_precision)

    for i in range(len(precision_values)):
        print(i, ":", round(precision_values[i], 3),
              "->", round(recall_values[i], 3))

    print("Interpolated Precision: ", interpolated_precision)
    print("Recall Levels: ", recall_levels)

    plt.plot(recall_values, precision_values,
             marker='.', label='Precision-Recall Curve')
    plt.plot(recall_levels, interpolated_precision, marker='o',
             linestyle='-', label='11-point Interpolation')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve with 11-point Interpolation')
    plt.legend()
    plt.grid(True)

    plt.xticks(recall_levels)
    plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    print("Total Docs :" + str(total_docs))
    print("Relevant Docs :" + str(relevant_docs))
    plt.show()
