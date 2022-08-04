import datetime
from file_validation import *


def interactive():
    date_entry = input('Enter date in YYYY-MM-DD format')
    try:
        year, month, day = map(int, date_entry.split('-'))
        csv_date = datetime.date(year, month, day)
        if check_batch_id(f'MED_DATA_{str(year)}{str(month)}{str(day)}'):
            pass
            # - perform csv download function
        else:
            print()
    except ValueError as err:
        print('\nIncorrect format')
        user_menu()


def scheduler():
    pass


def user_menu():
    while True:
        command = input("""
                   Select Option
                   
                    1. Download CSV
                    
                    2. Set Scheduled Download
        
                    """)
        if command == "1":
            interactive()
        elif command == "2":
            pass
            # schedule function
        else:
            print("Input not recognised")


user_menu()