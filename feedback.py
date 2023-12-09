import pandas as pd
from preprocessingAndIndexing import *
data = pd.read_csv('main dataset//main.csv')


def feedback(feedback_ids):
    for feedback_id in feedback_ids:
        # Use .any() to check if any element matches
        if (data['ID'] == feedback_id).any():
            data.loc[data['ID'] == feedback_id, 'Feedback'] += 1
            data.loc[data['ID'] == feedback_id, 'Evaluation'] = data.loc[data['ID'] ==feedback_id, 'Feedback'] * data.loc[data['ID'] == feedback_id, 'Rating']
            data.loc[data['ID'] == feedback_id, 'Normalized Evaluation'] = data.loc[data['ID']==feedback_id, 'Evaluation'] / 87316*100
    data.to_csv('main dataset//main.csv', index=False)
    print(feedback_ids)
    NormalizedEvalMap = getNormalizedEvaluation('main dataset//main.csv')
