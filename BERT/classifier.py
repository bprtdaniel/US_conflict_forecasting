import pandas as pd
import numpy as np
import torch
from transformers import pipeline
from transformers import RobertaModel, RobertaTokenizer, RobertaForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer





classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")

model = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"

candidate_labels = ["environment", "unions", "gun-violence", "healthcare"]



def get_labels(notes_with_ids, model, candidate_labels):
    results = []

    classifier = pipeline("zero-shot-classification", model=model)

    for index, row in notes_with_ids.iterrows():
        event_id = row['event_id']
        note = row['note']  # Adjust this line if your column name is different
        sequence_to_classify = note
        output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
        scores_for_note = {label: score for label, score in zip(output["labels"], output["scores"])}
        scores_for_note['Event ID'] = event_id
        results.append(scores_for_note)

    # Convert results to DataFrame
    df = pd.DataFrame(results)

    # Set 'Event ID' as the index
    df.set_index('Event ID', inplace=True)

    # Transpose the DataFrame
    df = df.T

    return df
