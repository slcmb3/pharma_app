import pandas as pd
import os

csv_download = 'file_downloads'
csv_validated = 'file_validated'

header_names = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5",
                "reading6", "reading7", "reading8", "reading9", "reading10"]

all_batch_ids = []


def convert_to_df(csv_file):
    df = pd.read_csv(csv_file)
    return df


def get_row_count(df):
    # return number of rows in file
    return df.shape[0]


def check_headers(df):
    # confirm no headers missing
    headers = list(df)
    if headers == header_names:
        return 'Headers correct'
    else:
        return 'Incorrect headers'


def check_missing_data(df):
    # return any missing cell values
    for header in header_names:
        for i in range(get_row_count(df)):
            if pd.isnull(df.loc[i, header]):
                return f'Missing value in column: {header}, in row {i}'


def check_valid_entry(df):
    # check no values over 9.9
    for header in header_names[2:]:
        for i in range(get_row_count(df)):
            cell = df.loc[i, header]
            cell = str(cell)
            if cell != 'nan':
                cell = float(cell)
                if cell >= 10:
                    return 'Error', df.loc[i, header]


def get_batch_ids():
    # get all validated batch id's and append to list
    os.chdir('file_validated')
    for file in os.listdir('.'):
        df = pd.read_csv(file)
        for batch_id in df['batch_id']:
            all_batch_ids.append(batch_id)


def check_batch_id(df):
    # confirm batch id is not a duplicate
    for batch_id in df['batch_id']:
        if batch_id not in all_batch_ids:
            # all_batch_ids.append(batch_id)
            return 'This batch file is not a duplicate'
        else:
            return 'This batch file already exists'


def check_malformed(csv_file):
    # check for any file malformations
    if csv_file.endswith('.csv'):
        return 'File correct'
    else:
        return 'File malformed'


def validate_downloaded_csvs():
    # create log of validation
    downloaded_csvs = os.listdir('.')
    if len(downloaded_csvs) == 0:
        print('Folder Empty')
    else:
        for file in downloaded_csvs:
            with open('validation_log.txt', 'a') as f:
                print('---------', file=f)
                print(file, file=f)
                print(check_malformed(file), file=f)
                df = pd.read_csv(file)
                print(check_headers(df), file=f)
                print(check_missing_data(df), file=f)
                print(check_valid_entry(df), file=f)
                print(check_batch_id(df), file=f)
                print('---------', file=f)


