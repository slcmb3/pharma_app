import ftplib

FTP_HOST = " "
FTP_USER = " "
FTP_PASS = " "
CSV_FILENAME = " "

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding = "utf-8"


def download_file(filename):
    with open(filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)

    ftp.quit()