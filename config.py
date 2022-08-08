import ftplib
from ftplib import FTP
import os
from pathlib import Path
from file_validation import *

FTP_HOST = "127.0.0.1"
ftp = FTP(FTP_HOST)


def ftp_login(user, passwd):
    FTP_USER = user
    FTP_PASS = passwd

    ftp.login(user=FTP_USER, passwd=FTP_PASS)


def check_file(date: str):
    ftp.cwd('/ftp/')
    contents = ftp.nlst('MED_DATA_20210701')
    folder = []
    for file in contents:
        stored_files = Path('file_downloads')
        if date in file and not stored_files.is_file():
            folder.append(file)
    print(folder)
    return folder


def download_file(date: str, user: str, passwd: str):
    ftp_login(user, passwd)
    files = check_file(date)
    for file in files:
        file = file[18:]
        print(file)
    try:
        ftp.cwd('/ftp/')
        ftp.cwd('MED_DATA_20210701')
        os.chdir('file_downloads')
        print(ftp.dir())
        with open(file, "wb") as file:
            ftp.retrbinary(f"RETR {file}", file.write)
    except ftplib.Error as err:
        print('Error accessing FTP server: ', err)
    finally:
        ftp.quit()

