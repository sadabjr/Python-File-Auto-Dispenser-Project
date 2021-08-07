import os
from datetime import datetime, timedelta


def file_dispenser(path, thresh, base=False):
    if os.path.isdir(path):
        for internal in os.listdir(path):
            file_dispenser(path + "/" + internal, thresh, False)

        if (not base) and len(os.listdir(path)) == 0:
            os.rmdir(path)
        return

    mod = os.path.getmtime(path)

    if thresh > mod:
        print("The is is an old file.")
        os.remove(path)
    else:
        print("This is a new file")

threshold = (datetime.now() - timedelta(minutes=1)).timestamp()
file_dispenser("File name", threshold)
#print(threshold)