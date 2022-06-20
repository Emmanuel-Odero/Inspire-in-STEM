from __future__ import unicode_literals
import youtube_dl
import os

ydl_opts = {}
os.chdir('C:/Downloads')

makeDirectory = input("\nCreate new directory for your downloads or use an existing one [y/n] :")
if makeDirectory == 'n':
	print("\nNo directory made for download so defaults to 'F/downloads\n'")
elif makeDirectory == 'y':
	down = input('\nName folder for downloads : ')
	path = os.path.join(os.getcwd(), down)
	if os.path.isdir(path):
		os.chdir(path)
		print('Path folder already exits\n')
		print('Downloading to {}\n'.format(path))
	else:
		os.mkdir(path)
		os.chdir(path)
		print('Downloading to {}\n'.format(path))
else:
	print("\nInvalid Response, use either 'y' for 'yes' or 'n' for no\n\n")
	exit()

inputedLink = input("Input the link download : ")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([inputedLink])