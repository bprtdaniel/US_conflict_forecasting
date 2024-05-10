import pandas as pd
import numpy as np
import torch
from transformers import pipeline
from transformers import RobertaModel, RobertaTokenizer, RobertaForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer


def get_labels(notes_with_ids, model, candidate_labels):
    results = []

    classifier = pipeline("zero-shot-classification", model=model)

    for index, row in notes_with_ids.iterrows():
        event_id = row['event_id']
        note = row['note']  
        sequence_to_classify = note
        output = classifier(sequence_to_classify, candidate_labels, multi_label=False)
        scores_for_note = {label: score for label, score in zip(output["labels"], output["scores"])}
        scores_for_note['Event ID'] = event_id
        results.append(scores_for_note)

    df = pd.DataFrame(results)
    df.set_index('Event ID', inplace=True)
    return df


# Define the model
model = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli"

# Define the classifier pipeline
classifier = pipeline("zero-shot-classification", model = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")

# Create the topics to classify on
candidate_labels = ["environment", "unions", "gun-violence", "healthcare", "racial-justice"]

# Load the input data
notes = pd.read_csv("notes.csv")


# Run the classifier
topics = get_labels(notes, model, candidate_labels)

# Assign 1 to the highest score and 0 to the rest
topics = topics.apply(lambda row: row == row.max(), axis=1).astype(int)

# Add categotical label variable to the topics dataframe
topics['label'] = topics.idxmax(axis=1)

# Add additional numerical label variable to the topics dataframe
topics['label_num'] = topics['label'].map({'environment': 1, 'unions': 2, 'gun-violence': 3, 'healthcare': 4, 'racial-justice': 5})

# Save to csv
topics.to_csv("topics.csv")
