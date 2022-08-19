import shutil
import typer
from datetime import date
from os.path import exists
from config import *
from file_validation import *

app = typer.Typer()


def get_file(combined_date, user, passwd, host):
    ftp = return_ftp_host(host)
    get_batch_ids()
    if ftp_login_check(user, passwd):
        ftp.cwd('/ftp/')
        ftp.cwd('MED_DATA_20210701')
        filenames = ftp.nlst()
        os.chdir('..')
        os.chdir('file_downloads')
        print('If file exists, check file_downloads for CSV')
        for filename in filenames:
            if filename.startswith(f'MED_DATA_{combined_date}'):
                local_file = open(filename, 'wb')
                ftp.retrbinary('RETR ' + filename, local_file.write, 1024)
                local_file.close()
        ftp.quit()
    validate_downloaded_csvs()


def ftp_credentials(menu_type):
    username = input('Enter FTP username: ')
    password = input('Enter FTP password: ')
    host = input('Enter FTP host: ')
    if menu_type == 'interactive':
        interactive_download(username, password, host)
    elif menu_type == 'scheduler':
        set_schedule_creds(username, password, host)
        scheduler()


def interactive_download(username, password, host):
    year = input('Enter year of CSV (YYYY): ')
    month = input('Enter month of CSV (MM): ')
    day = input('Enter day of CSV (DD): ')
    combined_date = year+month+day
    get_file(combined_date, username, password, host)


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


def set_schedule_creds(username, password, host):
    f = open('creds.txt', 'w')
    f.write(username + '\n')
    f.write(password + '\n')
    f.write(host + '\n')
    f.close()


def get_schedule_creds(cred_type):
    f = open('creds.txt', 'r')
    username = f.readline().rstrip()
    passw = f.readline().rstrip()
    host = f.readline().rstrip()
    if cred_type == 'username':
        cred = username
    elif cred_type == 'password':
        cred = passw
    elif cred_type == 'host':
        cred = host
    return cred






def scheduler():
    frequency = input('Enter frequency of csv download scheduler: ')
    time = input('Enter time for csv download: ')
    # set_task_schedule(frequency, time)
    pass


@app.command()
def start():
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


@app.command()
def auto_download():
    ftp_name = get_schedule_creds('username')
    ftp_passw = get_schedule_creds('password')
    ftp_host = get_schedule_creds('host')
    today = str(date.today())
    today = today.replace('-', '')
    get_file(today, ftp_name, ftp_passw, ftp_host)


if __name__ == "__main__":
    auto_download()
    #app()
