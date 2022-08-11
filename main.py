import shutil
from os.path import exists
from config import *
from file_validation import *


def get_file(date, user, passwd):
    get_batch_ids()
    if ftp_login_check(user, passwd):
        ftp.cwd('/ftp/')
        ftp.cwd('MED_DATA_20210701')
        filenames = ftp.nlst()
        os.chdir('..')
        os.chdir('file_downloads')
        print('If file exists, check file_downloads for CSV')
        for filename in filenames:
            if filename.startswith(f'MED_DATA_{date}'):
                local_file = open(filename, 'wb')
                ftp.retrbinary('RETR ' + filename, local_file.write, 1024)
                local_file.close()
        ftp.quit()
    validate_downloaded_csvs()


def ftp_credentials(menu_type):
    username = input('Enter FTP username: ')
    password = input('Enter FTP password: ')
    if menu_type == 'interactive':
        interactive_download(username, password)
    elif menu_type == 'scheduler':
        pass


def interactive_download(username, password):
    year = input('Enter year of CSV (YYYY): ')
    month = input('Enter month of CSV (MM): ')
    day = input('Enter day of CSV (DD): ')
    date = year+month+day
    get_file(date, username, password)


def show_validation():
    validation_log = 'file_downloads/validation_log.txt'
    if exists(validation_log):
        f = open(validation_log, 'r')
        file_contents = f.read()
        print(file_contents)
    else:
        print('Check file validation before archiving files\n')


def archive_file():
    show_validation()
    csv_file = input('Enter file name for archive: ')
    src_path = f'file_downloads/{csv_file}'
    dest_path = 'file_validated'
    shutil.move(src_path, dest_path)


def scheduler(username, password):
    # set a date and time for scheduler to download files
    pass


def user_menu():
    while True:
        command = input("""
        
        ***     Medical CSV Downloader      ***
                
        
                   Select Option:
                   
                1. Download CSV
                
                2. Archive Validated CSV
                    
                3. Set Scheduled Download
        
                    """)
        if command == "1":
            ftp_credentials('interactive')
        elif command == "2":
            archive_file()
        elif command == "3":
            pass
            # ftp_credentials('scheduler')
        else:
            print("Input not recognised")


if __name__ == "__main__":
    user_menu()
