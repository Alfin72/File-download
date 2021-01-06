# IMPORTING REQUIRED LIBRARIES
import os
import requests
import shutil
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
new = ("/home/sncsag/Documents/Defender_Updates/")

# FUNCTION TO CREATE A FOLDER WITH CURRENT DATE.
def create_folder():
	today = datetime.now() #ASSIGNING THE DATE AND TIME TO THE VARIABLE today
	#new = ("/home/sncsag/Documents/Defender_Updates/") # ASSIGNING THE STRING (FOLDER NAME) 
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
        for dirnames in dirnames:
            if 'windows' in str(dirnames):
                windows10files.append(dirnames)
            windows8files.append(dirnames)

            
def tozip(list_to_zip, name):
    with ZipFile(name+'.zip','w') as zip: 
# writing each file one by one 
        for file in list_to_zip: 
            zip.write(file)

def create_bitfolder():
	if not os.path.exists("windows 8.1 32_bit"): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs("windows 8.1 32_bit") # CREATES THE FOLDER WITH THE GIVEN NAME.
	if not os.path.exists("windows 8.1 64_bit"): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs("windows 8.1 64_bit") # CREATES THE FOLDER WITH THE GIVEN NAME.
	if not os.path.exists("windows 10 32_bit"): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs("windows 10 32_bit") # CREATES THE FOLDER WITH THE GIVEN NAME.
	if not os.path.exists("windows 10 64_bit"): # CHECKS IF THE FOLDER WITH THE GIVEN NAME EXISTS.
		os.makedirs("windows 10 64_bit") # CREATES THE FOLDER WITH THE GIVEN NAME.

def move_file():
	today = datetime.now() #ASSIGNING THE DATE AND TIME TO THE VARIABLE today

	st = str(today.strftime('%d-%m-%y')) #ASSIGNING THE DATE AND TIME TO THE VARIABLE st in string format


	source = ("/home/sncsag/Documents/Defender_Updates/%s/Network Real-time Inspection Definition Updates (64bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 64_bit/Network Real-time Inspection Definition Updates (64bit).exe" %(st))
	os.rename(source,destination)

	source = ("/home/sncsag/Documents/Defender_Updates/%s/Network Real-time Inspection Definition Updates (32bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 32_bit/Network Real-time Inspection Definition Updates (32bit).exe" %(st))
	os.rename(source,destination)

	source = ("/home/sncsag/Documents/Defender_Updates/%s/MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 10 64_bit/MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe" %(st))

	shutil.copyfile(source,destination)

	source = ("/home/sncsag/Documents/Defender_Updates/%s/MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 10 32_bit/MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe" %(st))

	shutil.copyfile(source,destination)
	
	source = ("/home/sncsag/Documents/Defender_Updates/%s/MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 64_bit/MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe" %(st))
	os.rename(source,destination)

	source = ("/home/sncsag/Documents/Defender_Updates/%s/MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe" %(st))
	destination = ("/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 32_bit/MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe" %(st))
	os.rename(source,destination)

create_folder()
#create_bitfolder()
#move_file()
collect_file_name()
print (windows8files)
