from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.misc
import scipy.ndimage

def nearest_nbr_up(img,scale):
	Img = plt.imread(img)
	dim = Img.shape
	n_col, n_row = dim[0],dim[1] 
	x = dim[0]*scale
	y = dim[1]*scale
	z = dim[2]
	x_ratio = n_col/float(x)
	y_ratio = n_row/float(y)
	scaled = np.empty([x,y,z])

	for row in range(y):
		for col in range(x):
			p_row = int(math.floor(row*y_ratio))
			p_col = int(math.floor(col*x_ratio))
			scaled[col,row] = Img[p_col,p_row]
	scipy.misc.imsave('test.png', scaled)
	return

nearest_nbr_up('mario.png',10)

def downscale(img,scale):
	Img = plt.imread(img)
	dim = Img.shape
	n_col, n_row = dim[0],dim[1]
	x = dim[0]/scale
	y = dim[1]/scale
	z = dim[2]
	scaled = np.empty([x,y,z])
	return





