#! /usr/bin/env python
# -*- coding: utf8 -*-

import glob

class archiver():
	"""
	archiver object finds and archives correctly
	"""
	def __init__(self):
		folders = glob.glob("/home/jamie/Dropbox/shared/*")
                files = []
		for fi in folders:
			files = glob.glob(fi + "/*")  #This should in fact be 'files.append(glob.glob(fi + '/*'))' or 'files += glob.glob(fi + '/*')'....
		print files	#....otherwise this will simply print the files in the last folder listed in the folders list...
                #...anyway, the API should do all this for us? See https://www.dropbox.com/developers  

if __name__ == "__main__":
	a = archiver()

#Modified by Eoin, Sunday 29 August, 9:29pm
