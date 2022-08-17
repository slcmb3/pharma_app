import ftplib
from ftplib import FTP
from creds import *


FTP_HOST = host
ftp = FTP(FTP_HOST)


def ftp_login_check(user, passwd):
    ftp_username = user
    ftp_pass = passwd
    try:
        ftp.login(user=ftp_username, passwd=ftp_pass)
        return True
    except ftplib.error_perm as err:
        print('Error: ', err)
        return False



