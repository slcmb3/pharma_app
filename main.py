import shutil
import typer
from datetime import date
from os.path import exists
from config import *
from file_validation import *

app = typer.Typer()


def get_file(combined_date, user, passwd):
    """

    :param combined_date: date of csv file
    :param user: ftp username
    :param passwd: ftp password
    :return: this will retrieve all CSVs of specified date and pass them to the validation functions
    """
    # ftp = return_ftp_host(host)
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
    """
    :param menu_type: interactive or automatic login option
    :return: interactive: user menu // scheduler: set automated download
    """
    username = input('Enter FTP username: ')
    password = input('Enter FTP password: ')
    host = input('Enter FTP host: ')
    if menu_type == 'interactive':
        interactive_download(username, password)
    elif menu_type == 'scheduler':
        # set_schedule_creds(username, password, host)
        # scheduler()
        pass


def interactive_download(username, password):
    year = input('Enter year of CSV (YYYY): ')
    month = input('Enter month of CSV (MM): ')
    day = input('Enter day of CSV (DD): ')
    combined_date = year + month + day
    get_file(combined_date, username, password)


def show_validation():
    """
    :return: display the validation information from last csv download
    """
    validation_log = 'file_downloads/validation_log.txt'
    if exists(validation_log):
        f = open(validation_log, 'r')
        file_contents = f.read()
        print(file_contents)
    else:
        print('Check file validation before archiving files\n')


def archive_file():
    """
    :return: move downloaded csv to an archive
    """
    show_validation()
    csv_file = input('Enter file name for archive: ')
    src_path = f'file_downloads/{csv_file}'
    dest_path = 'file_validated'
    shutil.move(src_path, dest_path)


def set_schedule_creds(username, password, host):
    """
    :param username: ftp username
    :param password: ftp password
    :param host: ftp host
    :return: to enable task scheduler to auto download csv, login credentials are taken and stored in text file
    """
    f = open('creds.txt', 'w')
    f.write(username + '\n')
    f.write(password + '\n')
    f.write(host + '\n')
    f.close()


def get_schedule_creds(cred_type):
    """
    :param cred_type: ftp credential option
    :return: the selected ftp credential from creds.txt file (for task scheduled download)
    """
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


def scheduler(username, password):
    # function to set PowerShell task schedule download
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
    # ftp_username = get_schedule_creds('username')
    today = str(date.today())
    today = today.replace('-', '')
    get_file(today, ftp_username, ftp_password)


if __name__ == "__main__":
    start()
    #app()
