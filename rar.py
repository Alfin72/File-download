# IMPORTING REQUIRED LIBRARIES
import os
import sys
import requests
import shutil
from datetime import datetime, date, time
import zipfile

# CREATE DICTIONARY WITH THE LINK AND IT'S FILE NAME.
Links = {
	'https://go.microsoft.com/fwlink/?LinkID=187316&arch=x86&nri=true': "Network Real-time Inspection Definition Updates (32bit).exe",
	'https://go.microsoft.com/fwlink/?LinkID=187316&arch=x64&nri=true': "Network Real-time Inspection Definition Updates (64bit).exe",
        'https://go.microsoft.com/fwlink/?LinkID=121721&arch=x86': "MS Defender Updates for Windows 10 and Windows 8.1 (32bit).exe",
        'https://go.microsoft.com/fwlink/?LinkID=121721&arch=x64': "MS Defender Updates for Windows 10 and Windows 8.1 (64bit).exe"
		}

today = datetime.now() #ASSIGNING THE DATE AND TIME TO THE VARIABLE today

st = str(today.strftime('%d-%m-%y')) #ASSIGNING THE DATE AND TIME TO THE VARIABLE st in string format

#list of folders 
win10_folder = [
    "/home/sncsag/Documents/Defender_Updates/%s/windows 10 64_bit"%(st),
    "/home/sncsag/Documents/Defender_Updates/%s/windows 10 32_bit"%(st),
	]

win8_folder = [
	"/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 64_bit"%(st),
	"/home/sncsag/Documents/Defender_Updates/%s/windows 8.1 32_bit"%(st)
	]

Location = []
windows8files=[]
windows10files=[]
test = []
new = ("/home/sncsag/Documents/Defender_Updates/")
Zipname = ["/home/sncsag/Documents/Defender_Updates/%s/Windows_10.zip"%(st),"/home/sncsag/Documents/Defender_Updates/%s/Windows_8.zip"%(st)]

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
		if 'windows 10' in str(dirnames):
			windows10files.append(dirnames)
		else:
			windows8files.append(dirnames)

#creating zip file            
def zipit(folders, zip_filename):
    zip_file = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

    for folder in folders:
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                zip_file.write(
                    os.path.join(dirpath, filename),
                    os.path.relpath(os.path.join(dirpath, filename), os.path.join(folders[0], '../..')))

    zip_file.close()


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
download_file()
create_bitfolder()
move_file()
collect_file_name()
zipit(win10_folder, Zipname[0])
zipit(win8_folder, Zipname[1])



