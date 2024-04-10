import requests
import shortuuid
from PIL import Image
import os
import sys

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Folder '{directory_path}' created successfully.")
    else:
        print(f"Folder '{directory_path}' already exists.")

def getPictures(nb, isInfinite = False): 
    try:
        i = 0
        u = 0
        folder = "result"

        create_directory(folder)

        while i < nb:
            url = "https://thispersondoesnotexist.com/"
            data = requests.get(url).content

            with open(folder +"/img_" + str(i + 1) + "_" + shortuuid.uuid() + ".jpg", "wb") as f:
                f.write(data)
            if not isInfinite:
                sys.stdout.write('\033[K' + 'Is running... [' + str(i + 1) + '/' + str(nb) + ']' + '\r')
                i += 1
            else:
                sys.stdout.write('\033[K' + 'Is running... [' + str(u + 1) + '/' + '∞] Press Ctrl+C to stop the process' + '\r')
                u += 1
        print("\nDone.")
    except KeyboardInterrupt:
        print("\nThe process has been stroped.")
        sys.exit(0)

def getInput():
    str = input("Type the number of pictures needed: ")
    try:
        nb = int(str)
        if nb <= 0:
            getPictures(1, True)
        else:
            getPictures(nb)
        return True
    except ValueError:
        print("Entry failed, a number is required.")
        return False
    
getInput()
    
