#!/usr/bin/env python

# Import the text entry GUI functionality from easygui.
from easygui import multenterbox    

# Create GUI that asks for user input
msg = "Enter DPX Sequence Details"
title = "Enter info please"
fieldNames = ["Width",
	      "Height",
	      "Bit Depth", 
              "FPS", 
              "minutes"]
fieldValues = []  # we start with blanks for the values
# The values will be stored as a list, eg [2048,1556,32,24,60]
fieldValues = multenterbox(msg,title, fieldNames)

if fieldValues[2]   == '10':
	bitdepth     = '32'               # While 10 bits * 3 components = 30 bits, they are stored as 32 bits.
elif fieldValues[2] == '16':
	bitdepth     = '48'               # 16 bits * 3 components(RGB) = 48 bits

evaluate = (float(fieldValues[0])           # gets width
 	   * float(fieldValues[1])          # multiples by height
 	   * float(bitdepth)                # multiplies by bit depth per component
	   /8 / 1024 / 1024 		  # these calcs turn the value from a bit into a megabyte	
 	   * float(fieldValues[3])          # multiply by FPS
 	   * 60                             # multiply by 60 to get how many megs for one second
 	   * float(fieldValues[4])          # multiply by how many minutes
 	   /1024 )                          # turn the value into gigabytes
 
# prints the result to the screen
print "%s minutes of footage will take up %s gigabytes of space" % (fieldValues[4], evaluate)
