from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.misc

# mario = plt.imread('scenery.png')
# print mario.shape
# scale_factor = 2
# # print mario
# n_col = mario.shape[0]
# n_row = mario.shape[1]
# x = mario.shape[0]*scale_factor
# y = mario.shape[1]*scale_factor
# z = mario.shape[2]
# print "columns ", x
# print "rows ", y
# scaled = np.empty([x,y,z])
# print scaled
# plt.imshow(mario)
# scipy.misc.imsave('outfile.png', mario)

# print mario[1,1]

# test = mario[1,1]
# scaled[1,1] = test
# start_row = 0
# for row in range(n_row):
# 	start_col = 0
# 	for col in range(n_col):		
# 		scaled[start_col,start_row] = mario[col,row]
# 		start_col+=scale_factor
# 	start_row += scale_factor

# s_row = 0
# scipy.misc.imsave('test.png', scaled)

def spread(img,scale):
	Img = plt.imread(img)
	dim = Img.shape
	n_col = dim[0]
	n_row = dim[1]
	x = dim[0]*scale
	y = dim[1]*scale
	z = dim[2]
	scaled = np.empty([x,y,z])

	start_row = 0
	for row in range(n_row):
		start_col = 0
		for col in range(n_col):		
			scaled[start_col,start_row] = Img[col,row]
			start_col+=scale
		start_row += scale

	scipy.misc.imsave('test.png', scaled)
	return

spread('mario.png',2)

def fill(img,scale):
	#calculate zone from start point
	# eg (0,0) -> Zone {(0,0),(0,3),(3,0),(3,3)}
	# when it reaches new zone
	return




