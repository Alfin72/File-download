# IMPORTING REQUIRED LIBRARIES
import os
import requests
from datetime import datetime, date, time
from zipfile import ZipFile

# CREATE DICTIONARY WITH THE LINK AND IT'S FILE NAME.
Links = {
	'https://go.microsoft.com/fwlink/?LinkID=187316&arch=x86&nri=true': "Network Real-time Inspection Definition Updates (32bit).exe",
	'https://go.microsoft.com/fwlink/?LinkID=187316&arch=x64&nri=true': "Network Real-time Inspection Definition Updates (64bit).exe",
        'https://go.microsoft.com/fwlink/?LinkID=121721&arch=x86': "MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe",
        'https://go.microsoft.com/fwlink/?LinkID=121721&arch=x64': "MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe"
		}

Location = []
windows8files=[]
windows10files=[]

# FUNCTION TO CREATE A FOLDER WITH CURRENT DATE.
def create_folder():
	today = datetime.now() #ASSIGNING THE DATE AND TIME TO THE VARIABLE today
	new = ("/home/sncsag/Documents/Defender_Updates/") # ASSIGNING THE STRING (FOLDER NAME) 
	newpath = (new + today.strftime('%d-%m-%y')) # ASSIGNING THE FOLDER NAME AFTER ADDING THE DATE TO THE END OF STRING (NEW)
	if not os.path.exists(newpath): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs(newpath) # CREATES THE FOLDER WITH THE GIVEN NAME.
	os.chdir(newpath) # CHANGE THE WORKING DIRECTORY OF PYTHON TO THE CREATED FOLDER
	Location.append(newpath)

#FUNCTION TO DOWNLOAD THE FILE.
def download_file():
	for url, file_name in Links.items(): # ITERATES THROUGH THE DICTIONARY (LINKS)
		r = requests.get(url, allow_redirects=True) # USING REQUEST LIBRARY TO DOWNLOAD THE FILE FROM THR LINK.
		open(file_name, 'wb').write(r.content) # RE-NAMING THE DOWNLOADED FILES WITH THE FILE NAME GIVEN IN DICTIONARY

def collect_file_name():
    for (dirpath, dirnames, filenames) in os.walk(Location[0]):
        for filename in filenames:
            if 'MS Defender' in str(filename):
                windows10files.append(filename)
            windows8files.append(filename)
            
def tozip(list_to_zip, name):
    with ZipFile(name+'.zip','w') as zip: 
# writing each file one by one 
        for file in list_to_zip: 
            zip.write(file)

def create_bitfolder():
	newpath = (new + "32bit") # ASSIGNING THE FOLDER NAME AFTER ADDING THE DATE TO THE END OF STRING (NEW)
	if not os.path.exists(newpath): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs(newpath) # CREATES THE FOLDER WITH THE GIVEN NAME.
	newpath = (new + "64bit") # ASSIGNING THE FOLDER NAME AFTER ADDING THE DATE TO THE END OF STRING (NEW)
	if not os.path.exists(newpath): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs(newpath) # CREATES THE FOLDER WITH THE GIVEN NAME.

        
#CALLING THE FUNCTIONS.
create_folder()
download_file()
collect_file_name()
tozip(windows10files, "Windows 10 files")
tozip(windows8files, "Windows 8.1 files")
