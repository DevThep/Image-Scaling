from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.misc
import scipy.ndimage

def nearest_nbr_up(img,scale,new_name):
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
	scipy.misc.imsave(new_name, scaled)
	return

def bilinearInterpolationTest(image, scale):
    Img = plt.imread(image)
    dim = Img.shape
    y = dim[0]
    x = dim[1]
    z = dim[2]
    scaled = np.zeros([int(y*scale),int(x*scale),z])
    xn = len(scaled[0])
    yn = len(scaled)
    #print scaled
    for row in range(yn):
        for col in range(xn):
            y0 = row
            x0 = col
            x00 = x0/scale
            x1 = int(math.floor(x00))
            if x1+1 < x:
                x2 = x1+1
            else:
                x1 -= 1
                x2 = x1+1
            y00 = y0/scale
            y1 = int(math.floor(y00))
            if y1+1 < y:
                y2 = y1+1
            else:
                y1 -= 1
                y2 = y1+1
            #Interpolate in x-direction
            fx_y1 = (((x2-x00)/(x2-x1))*Img[y1,x1])+(((x00-x1)/(x2-x1))*Img[y1,x2])
            fx_y2 = (((x2-x00)/(x2-x1))*Img[y2,x1])+(((x00-x1)/(x2-x1))*Img[y2,x2])
            #Interpolate in y-direction
            fx_y = (((y2-y00)/(y2-y1))*fx_y1)+(((y00-y1)/(y2-y1))*fx_y2)
            scaled[row,col] = fx_y
    scipy.misc.imsave('test.png', scaled)

bilinearInterpolationTest('carola.png', 0.04)
