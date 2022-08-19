import ftplib
from ftplib import FTP
from creds import *


FTP_HOST = host
ftp = FTP(FTP_HOST)

# def return_ftp_host(host):
#     ftp = FTP(host)
#     return ftp


def ftp_login_check(user, passwd):
    # ftp = return_ftp_host(host)
    try:
        ftp.login(user=user, passwd=passwd)
        return True
    except ftplib.error_perm as err:
        print('Error: ', err)
        return False



