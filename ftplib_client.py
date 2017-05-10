from ftplib import FTP
import os
import argparse
import urlparse

class ftplib_client():
    def __init__(self, server, account, pwd):
        self.ftp = FTP(server)        
        self.ftp.set_pasv(True)        
        print 'login...'
        self.ftp.login(account, pwd)    

    def chdir(self, dir): 
        try:
            self.ftp.mkd(dir)
        except:
            pass
        self.ftp.cwd(dir)

    # Check if directory exists (in current location)
    def directory_exists(self, dir):
        if dir in self.ftp.nlst():
            return True
        return False

    def upload_file(self, remote_folder, local_fpath):   
        print 'chdir...'   

        self.chdir(remote_folder)
        fname = os.path.basename(local_fpath)
        print 'upload...'
        self.ftp.storlines("STOR " + fname, open(local_fpath, 'r'))

if __name__ == "__main__":

    parser = argparse.ArgumentParser()    
    parser.add_argument("-s", "--server", help="ftp ip address", type=str, required=True)  
    parser.add_argument("-a", "--account", help="account", type=str, required=True)
    parser.add_argument("-p", "--pwd", help="password", type=str, required=True)
    parser.add_argument("-f", "--localfile", help="local file path", type=str, required=False)  
    parser.add_argument("-rd", "--remotedir", help="download file name", type=str, required=False, default='/')    
    
    args = parser.parse_args()
    print args

    f = ftplib_client(server = args.server, account = args.account, pwd = args.pwd)
    f.upload_file(remote_folder = args.remotedir, local_fpath = args.localfile)
        