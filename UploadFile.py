import os
import dropbox from dropbox.files 
import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx= dropbox.Dropbox(self.accesstoken)

        for root,dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'riFu6Ybhc9AAAAAAAAAAHWkfE9AiGyD6n4254tOxesw7ShRjGjFhrjhRVa3NX3mx'
    transferData - TrasnferData(access_token)

    file_to= str(input("Enter the folder path you want to transfer:- "))
    file_from=input("Enter the full path of the file you want to upload to dropbox:- ")

    transferData.upload_files(file_from, file_to)
    print("This file has been removed")