import plotly.graph_objects as go

def PRcurve(total_docs, relevant_docs_id, top_10):
    relevant_docs = len(relevant_docs_id)
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
        print(i, ":", round(precision_values[i], 3), "->", round(recall_values[i], 3))

    print("Interpolated Precision: ", interpolated_precision)
    print("Recall Levels: ", recall_levels)

    # Plotting with Plotly
    fig = go.Figure()

    # Precision-Recall Curve
    fig.add_trace(go.Scatter(x=recall_values, y=precision_values,
                             mode='markers+lines', name='Precision-Recall Curve',
                             marker=dict(size=8)))

    # 11-point Interpolation
    fig.add_trace(go.Scatter(x=recall_levels, y=interpolated_precision,
                             mode='lines+markers', name='11-point Interpolation'))

    # Update layout
    fig.update_layout(
        title='Precision-Recall Curve with 11-point Interpolation',
        xaxis_title='Recall',
        yaxis_title='Precision',
        xaxis=dict(tickvals=recall_levels),
        yaxis=dict(tickvals=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]),
        showlegend=True
    )

    # Show the figure
    fig.show()

    print("Total Docs :" + str(total_docs))
    print("Relevant Docs :" + str(relevant_docs))
