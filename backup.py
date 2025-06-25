import shutil
import datetime
import os

def backup_files(source, destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup1{today}")
    shutil.make_archive(backup_file_name,'gztar',source)

source = "/Users/muzah/OneDrive/Documents/python-ALI"
destination = "/Users/muzah/OneDrive/Documents/python-ALI/backups"

backup_files(source, destination)


