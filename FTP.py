from ftplib import FTP

ftp = FTP('ftp.dlptest.com')  # Example FTP server
ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')

# List files
ftp.retrlines('LIST')

# Upload a file
filename = 'test_upload.txt'
with open(filename, 'w') as f:
    f.write("Hello FTP!")
with open(filename, 'rb') as f:
    ftp.storbinary(f'STOR {filename}', f)

# Download a file
with open('downloaded.txt', 'wb') as f:
    ftp.retrbinary('RETR test_upload.txt', f.write)

ftp.quit()
