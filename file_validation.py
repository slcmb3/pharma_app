# from config import *
import numpy as np
import pandas as pd
import os

csv_dir = 'MED_DATA_20210701'
csv_file_name = os.path.join(csv_dir, 'MED_DATA_20210701153942.csv')
df = pd.read_csv(csv_file_name)

header_names = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5",
                "reading6", "reading7", "reading8", "reading9", "reading10"]

# this list will need to get all id's of downloaded files, when application starts
all_batch_ids = []


def get_row_count(csv_file):
    return df.shape[0]


def check_headers(csv_file):
    headers = list(df)
    if headers == header_names:
        return True
    else:
        return False


def check_missing_data(csv_file):
    for header in header_names:
        for i in range(get_row_count(df)):
            if pd.isnull(df.loc[i, header]):
                print(f'{header}: missing value in row {i}')

def check_batch_id(csv_file):
    for batch_id in df['batch_id']:
        if batch_id not in all_batch_ids:
            all_batch_ids.append(batch_id)
            return True
        else:
            print("this batch file already exists")
            return False


def check_malformed(csv_file):
    if csv_file.lower().endswith('.csv'):
        return True
    else:
        return False


check_headers(df)