from selenium import webdriver
from zipfile import ZipFile
import os

## Listing all files in a directory using scandir()
 
def zipping(name, file):
    finalname = name + '.zip'
    with ZipFile(finalname, 'w') as zip:
        zip.write(file)


if __name__ == "__main__":
    
    basepath ='/home/julio/qt-script/files'

    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                zipping(entry.name, entry)
                os.remove(entry)    ## remove the file after zipping it

    zipfiles = []

    with os.scandir('/home/julio/qt-script/') as entries:
        for entry in entries:
            if entry.is_file():
                if 'zip' in entry.name:
                    zipfiles.append(entry)

    for file in zipfiles:
        if 'imx8' in file.name:
            




