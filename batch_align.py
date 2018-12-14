#!/usr/bin/python

""" Command-line usage:
      python batch_align.py directory4processing P2FApath
      where directory4processing contains the files you want to process
      where P2FApath is the path to align.py
      written by Samantha Gordon Danner, December 2018
      """
import os, sys, getopt

mydir = sys.argv[1]
P2FApath = sys.argv[2]

for file in os.listdir(mydir):
    if file.endswith(".txt"):
    	txtname = os.path.join(mydir, file)
    	wavname = txtname.replace(".txt", ".wav")
    	gridname = txtname.replace(".txt", ".TextGrid")
    	
    	cmd = 'python ' + P2FApath + ' ' + wavname + ' ' + txtname + ' ' + gridname
	os.system(cmd)