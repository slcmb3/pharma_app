import os
import pandas as pd

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
        print('Headers correct')
        return True
    else:
        print('Incorrect headers')
        return False


def check_missing_data(df):
    # return any missing cell values
    for header in header_names:
        for i in range(get_row_count(df)):
            if pd.isnull(df.loc[i, header]):
                print(f'Missing value in column: {header}, in row {i}')
                return False


def check_valid_entry(df):
    # check no values over 9.9
    for header in header_names[2:]:
        for i in range(get_row_count(df)):
            cell = df.loc[i, header]
            cell = str(cell)
            if cell != 'nan':
                cell = float(cell)
                if cell >= 10:
                    print('Error', df.loc[i, header])
                    return False


def check_batch_id(df):
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
    if csv_file.endswith('.csv'):
        print('File correct')
        return True
    else:
        print('File malformed')
        return False


def validate_downloaded_csvs():
    for file in os.listdir('file_downloads'):
        print('---------')
        print(file)
        csv_file_name = os.path.join(csv_download, file)
        check_malformed(csv_file_name)
        df = pd.read_csv(csv_file_name)
        check_headers(df)
        check_missing_data(df)
        check_valid_entry(df)
        check_batch_id(df)
        print('---------')


validate_downloaded_csvs()

# verify batch ids from downloads
# push validated files to validated folder
# task schedule
