import datetime
from config import *


# def get_username():
#     username = input('Enter FTP username: ')
#     return username
#
#
# def get_password():
#     password = input('Enter FTP password: ')
#     return password


def interactive():
    # username = get_username()
    # password = get_password()

    # date_entry = input('Enter date in YYYY-MM-DD format')
    # try:
    #     year, month, day = map(int, date_entry.split('-'))
    #     csv_date = datetime.date(year, month, day)
    #     check_file(f'{str(year)}{str(month)}{str(day)}')
    # except ValueError as err:
    #     print('\nIncorrect format')
    #     user_menu()

    username = input('Enter FTP username: ')
    password = input('Enter FTP password: ')
    year = input('Enter year: ')
    month = input('Enter month: ')
    day = input('Enter day: ')
    date = year+month+day
    download_file(date, username, password)



def scheduler():
    # set a date and time for scheduler to download files
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


if __name__ == "__main__":
    user_menu()