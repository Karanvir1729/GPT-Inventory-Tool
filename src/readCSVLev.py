import csv
import pandas as pd
import openai
import os
from readCSVChatGPT import read_csv_file
import Levenshtein


def detectDuplicatesLev(str):
    csv_data = read_csv_file(str)
    similar_pairs = []
    for i in range(len(csv_data[0])):
        name1 = csv_data[0][i]
        for j in range(i + 1, len(csv_data[0])):
            name2 = csv_data[0][j]

            # Calculate Levenshtein distance between the names
            distance = Levenshtein.distance(name1, name2)

            # Check if the distance is below the threshold
            if distance <= 2:
                similar_pairs.append((name1, name2))
    if similar_pairs:
        for i in similar_pairs:
            if i[0] in csv_data[0]:
                # fix not in list error
                csv_data[0].remove(i[0])

    while len(csv_data[1]) != len(csv_data[0]):
        csv_data[1].append('')

    filename = 'output.csv'
    root = os.path.dirname(os.path.abspath(__file__))
    fileoutput = os.path.join(root, "output", filename)

    df = pd.DataFrame(csv_data)
    df.to_csv(fileoutput, index=False)
