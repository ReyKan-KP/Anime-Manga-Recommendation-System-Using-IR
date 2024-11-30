import plotly.graph_objects as go


def PRcurve(total_docs, relevant_docs_id, top_10):
    # Validate input
    if not total_docs or not relevant_docs_id or not top_10:
        print("Invalid input provided to PRcurve.")
        return {"success": False, "message": "Invalid input for PRcurve generation."}

    try:
        # Count relevant documents
        relevant_docs = len(relevant_docs_id)
        print("Starting PR Curve Calculation")
        print(
            f"Total Docs: {total_docs}, Relevant Docs IDs: {relevant_docs_id}, Top 10: {top_10}")

        # Rank documents based on relevance
        ranked_list = []
        for doc_id in top_10:
            ranked_list.append(
                {"DocID": doc_id, "Relevance": 1 if doc_id in relevant_docs_id else 0})

        # Initialize precision and recall values
        precision_values = []
        recall_values = []
        retrieved_relevant = 0

        for i, entry in enumerate(ranked_list):
            if entry["Relevance"] == 1:
                retrieved_relevant += 1

            precision = retrieved_relevant / (i + 1)
            recall = retrieved_relevant / relevant_docs if relevant_docs > 0 else 0

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

        # Log results
        for i in range(len(precision_values)):
            print(
                f"Rank {i + 1}: Precision = {round(precision_values[i], 3)}, Recall = {round(recall_values[i], 3)}")
        print(f"Interpolated Precision: {interpolated_precision}")
        print(f"Recall Levels: {recall_levels}")

        # Create the PR Curve
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
            yaxis=dict(tickvals=[0.0, 0.1, 0.2, 0.3, 0.4,
                       0.5, 0.6, 0.7, 0.8, 0.9, 1.0]),
            showlegend=True
        )

        # Save the figure as HTML
        file_path = "templates/pr_curve.html"
        fig.write_html(file_path)
        print(f"PR Curve saved to {file_path}")

        return {"success": True, "message": "PR Curve generated successfully.", "file_path": file_path}

    except Exception as e:
        print(f"Error in PRcurve function: {e}")
        return {"success": False, "message": f"Error generating PR Curve: {str(e)}"}
