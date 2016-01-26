from easygui import multenterbox
msg = "Fill out these things please"
title = "blablablabl"
fieldNames = ["Width",
	      "Height",
	      "Bit Depth", 
              "FPS", 
              "minutes"]
fieldValues = []  # we start with blanks for the values
fieldValues = multenterbox(msg,title, fieldNames)

if fieldValues[2]   == '10':
	bitdepth    =  '32'
elif fieldValues[2] == '16':
	bitdepth     = '48'

evaluate = float(fieldValues[0]) * float(fieldValues[1])  * float(bitdepth) //8 // 1024 // 1024 * float(fieldValues[3]) * 60 * float(fieldValues[4]) //1024 
print "%s minutes of footage will take up %s gigabytes of space" % (fieldValues[4], evaluate)
