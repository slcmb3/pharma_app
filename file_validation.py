# from config import *
import numpy as np
import pandas as pd
import os

csv_dir = 'MED_DATA_20210701'
csv_file_name = os.path.join(csv_dir, 'MED_DATA_20210701153942.csv')

df = pd.read_csv(csv_file_name)

# this list will need to get all id's of downloaded files, when application starts
all_batch_ids = []


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


