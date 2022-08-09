from ftplib import FTP
import os
from file_validation import *

FTP_HOST = "127.0.0.1"
ftp = FTP(FTP_HOST)


def ftp_login(user, passwd):
    ftp_username = user
    ftp_pass = passwd
    ftp.login(user=ftp_username, passwd=ftp_pass)


def get_file(date, user, passwd):
    ftp_login(user, passwd)
    ftp.cwd('/ftp/')
    ftp.cwd('MED_DATA_20210701')
    filenames = ftp.nlst()
    os.chdir('file_downloads')
    for filename in filenames:
        if filename.startswith(f'MED_DATA_{date}'):
            localfile = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            localfile.close()
        else:
            print('File not found')
    ftp.quit()
    validate_downloaded_csvs()

# get_file('20210701', 'admin', 'DeltaPlace$')