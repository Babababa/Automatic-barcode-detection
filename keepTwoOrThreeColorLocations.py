#keep nonblack pixels which are:
#(not (red or blue or yellow) OR have at least one nonblack neighbor which is not the same color, thinking of edges)

#Import used dependencies
import glob, os
from PIL import Image
import cv2
import numpy as np
#from numpy import array
#import matplotlib.image as mpimg
#from skimage.feature import blob_log
import math
import itertools
#from scipy import stats
#import random
#import datetime
#import time
import copy
#import heapq

#from matplotlib import pyplot as plt#!

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#Open and load images one by one
directory = '/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing'
#C:\Users\orskar\ownCloud\Desktop\KI from laptop\Rosettes\For further processing
os.chdir('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing')
cwd = os.getcwd()
#Combine channels:
index = 0
print("cwd: ", str(cwd))#DEBUG
print("index: ", str(index))#DEBUG
for file in glob.glob("*.jpg"):
		img = Image.open(file)
		im = np.asarray(img)
		#print(im)
		#cv2.imshow('image',im)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		index=index+1
		print("Starting processing image " +str(index))
		Max_X_coord, Max_Y_coord = img.size
		width = Max_X_coord
		height = Max_Y_coord
		print("width: ", str(width))
		print("height: ", str(height))
		#Create greyscale composite image:
		if index == 1:
			img_np = np.zeros((width, height))
		for i in range(width):
			for h in range(height):
				toBeAdded = 0
				if im[i, h] > 100:
					if index == 1:
						toBeAdded = 36
					elif index == 2:
						toBeAdded = 72
					elif index == 3:
						toBeAdded = 144
				img_np[i,h] = img_np[i,h] + toBeAdded
		img_cv = cv2.resize(img_np,( width, height))
		#cv2.imshow('summaryImage',img_cv)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		#plt.savefig('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + str(index) + '.jpg')
		cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + str(index) + '.jpg', img_cv)
#Algorithm
newestImg  = np.zeros((width, height))
for i in range(width):
	for h in range(height):
		colorOfPixel = img_np[i,h]
		if i == 0 and h == 0 or i == width - 1 and h == 0 or i == 0 and h == height - 1 or i == width -1 and h == height -1: #CORNER
			newestImg[i, h] = 0#TODO
		elif i == 0 or h == 0 or i == width - 1 or h == height - 1:#EDGE
			newestImg[i, h] = 0#TODO
		else:#inner point
			if (colorOfPixel == 36 or colorOfPixel == 72 or colorOfPixel == 144) and ((img_np[i-1,h-1] == 0 or img_np[i-1,h-1] == colorOfPixel) and (img_np[i-1,h] == 0 or img_np[i-1,h] == colorOfPixel) and (img_np [i-1,h+1] == 0 or img_np[i-1,h+1] == colorOfPixel) and (img_np[i,h-1] == 0 or img_np[i,h-1] == colorOfPixel) and (img_np[i,h+1] == 0 or img_np[i,h+1] == colorOfPixel) and (img_np[i+1,h-1] == 0 or img_np[i+1,h-1] == colorOfPixel) and (img_np[i+1,h] == 0 or img_np[i+1,h] == colorOfPixel) and (img_np[i+1,h+1] == 0 or img_np[i+1,h+1] == colorOfPixel)):
				newestImg[i, h] = 0
			else:
				newestImg[i, h] = colorOfPixel
img_cv2 = cv2.resize(newestImg,( width, height))
#cv2.imshow('compositeGreyscaleImage', newestImg)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'compositeGreyscale.jpg', img_cv2)
#Convert this to color image by splitting it into 5 channels:
#36 P2 - blue
#72 P4 - red
#144 P6 - yellow
#108 P2 and P4 lilac (cyan)
#180 P2 and P6 green
#218 P4 and P6 orange (magenta)
#252 P2, P4, P6 white
img_blue = np.zeros((width, height))
img_red = np.zeros((width, height))
img_yellow = np.zeros((width, height))
img_lilac = np.zeros((width, height))
img_green = np.zeros((width, height))
img_orange = np.zeros((width, height))
img_white = np.zeros((width, height))
for i in range(width):
	for h in range(height):
		colorOfPixel = newestImg[i,h]
		if colorOfPixel == 36:
			img_blue[i,h] = 255
		elif colorOfPixel == 72:
			img_red[i,h] = 255
		elif colorOfPixel == 144:
			img_yellow[i,h] = 255
		elif colorOfPixel == 108:
			img_lilac[i,h] = 255
		elif colorOfPixel == 180:
			img_green[i,h] = 255
		elif colorOfPixel == 218:
			img_orange[i,h] = 255
		elif colorOfPixel == 252:
			img_white[i,h] = 255
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'blue.jpg', img_blue)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'red.jpg', img_red)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'yellow.jpg', img_yellow)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'lilac.jpg', img_lilac)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'green.jpg', img_green)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'orange.jpg', img_orange)
cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'white.jpg', img_white)
#Create composite in Fiji
#print 'Processing finished'cv2.imwrite('/Users/orskar/ownCloud/Desktop/KI from laptop/Rosettes/For further processing/' + 'blue.jpg', img_blue)
