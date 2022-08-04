# from config import *
import numpy as np
import pandas as pd

df = pd.read_csv('MED_DATA_20210701/MED_DATA_20210701153942.csv')

all_batch_ids = []


def check_batch_id(csv_file):
    for batch_id in df['batch_id']:
        if batch_id not in all_batch_ids:
            all_batch_ids.append(batch_id)
            return True
        else:
            print("this batch file already exists")
            return False

