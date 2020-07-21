import cv2
import numpy as np
import os
import re
 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps,verbos = False):
	frame_array = []
	files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
	#for sorting the file names properly
	files.sort(key=lambda f: int(re.sub('\D', '', f)))

	if verbos:
		print("File sorted")

	size = (0,0)

	for i in range(len(files)):
		filename=pathIn + files[i]

		img = cv2.imread(filename)
		height, width, layers = img.shape
		size = size[0] + width,size[1] + height

		if verbos:
			print("Read file : ", filename)

		frame_array.append(img)
	
	size = int(size[0]/len(files)), int(size[1]/len(files))

	out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
	for i in range(len(frame_array)):
		# writing to a image array
		if verbos:
			print("Wrote file : ", i)
		out.write(frame_array[i])
	out.release()


 
if __name__=="__main__":
	#image folder path
	pathIn= './input/'

	#video file name
	pathOut = 'video.avi'

	fps = 25.0
	convert_frames_to_video(pathIn, pathOut, fps, verbos = True)