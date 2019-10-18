# ffmpeg -i input.m2ts -c:v copy -c:a aac -strict experimental -b:a 128k output.mp4
# /home/d-eviloper/Videos/PRIVATE/AVCHD/BDMV/STREAM
#!/usr/bin/python
from pathlib import Path
import os
import sys






def banner():
	print('\n\n')
	print('##     ## ########  ######   #######  ##     ## ########  ##           ')
	print('###   ###    ##    ##    ## ##     ## ###   ### ##     ## ##    ##     ')
	print('#### ####    ##    ##              ## #### #### ##     ## ##    ##     ')
	print('## ### ##    ##     ######   #######  ## ### ## ########  ##    ##     ')
	print('##     ##    ##          ## ##        ##     ## ##        #########    ')
	print('##     ##    ##    ##    ## ##        ##     ## ##              ##     ')
	print('##     ##    ##     ######  ######### ##     ## ##              ##     ')
	print('\n\n')


# Conversion Function
def convert(file,folder,count):
	filename, file_extension = os.path.splitext(file)
	ext=['.MTS']
	if file_extension in ext:
		ot_folder=os.path.join(folder,mp4)
		output=os.path.join(ot_folder, os.path.basename(folder)+"_"+str(count)+".mp4")
		print("Converting "+str(file))
		try:
			os.system("ffmpeg -i "+str(file)+" -c:v copy -c:a aac -strict experimental -b:a 128k "+str(output)+"> /dev/null 2>&1")
		except:
			print("Something went wrong when Processing the file")

# File Seeker
def recur(folder_path):
	p=Path(folder_path)
	dirs=p.glob("*")
	i=0
	for folder in dirs:
		# print(folder)
		if folder.is_dir():
			recur(folder)
		else:
			i+=1
			convert(folder,folder_path,i)

# calling the seeker function with input directory
banner()
# Input directory
directory = input("Enter the Directory Path: ")
# Output Directory
mp4="mp4"
os.system("mkdir "+os.path.join(directory,mp4))
recur(directory)



