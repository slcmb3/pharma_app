# from config import *
import numpy as np
import pandas as pd
import os

csv_dir = 'MED_DATA_20210701'
csv_file_name = os.path.join(csv_dir, 'MED_DATA_20210701153942.csv')
df = pd.read_csv(csv_file_name)

header_names = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5",
                "reading6", "reading7", "reading8", "reading9", "reading10"]

# this list will need to get all id's of downloaded files from allocated directory, when application starts
all_batch_ids = []


def get_row_count(csv_file):
    # return number of rows in file
    return df.shape[0]


def check_headers(csv_file):
    # confirm no headers missing
    headers = list(df)
    if headers == header_names:
        return True
    else:
        return False


def check_missing_data(csv_file):
    # return any missing cell values
    for header in header_names:
        for i in range(get_row_count(df)):
            if pd.isnull(df.loc[i, header]):
                print(f'Missing value in column: {header}, in row {i}')
                # return boolean


def check_valid_entry(csv_file):
    for header in header_names[2:]:
        for i in range(get_row_count(df)):
            cell = df.loc[i, header]
            cell = str(cell)
            if cell != 'nan':
                cell = float(cell)
                if cell >= 10:
                    print('error', df.loc[i, header])
                    return False


def check_batch_id(csv_file):
    # confirm batch id is not a duplicate
    for batch_id in df['batch_id']:
        if batch_id not in all_batch_ids:
            all_batch_ids.append(batch_id)
            return True
        else:
            print("This batch file already exists")
            return False


def check_malformed(csv_file):
    # check for any file malformations
    if csv_file.lower().endswith('.csv'):
        # check other malformations
        return True
    else:
        return False


check_valid_entry(df)

# if not check_valid_entry(df):
#     print('invalid entries')

# create function for invalid entry etc..
# create validation function that calls each sub-function