import cv2
from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import ndimage, misc
from skimage.filters import threshold_otsu
import os
import sys


file = [f.name for f in os.scandir() if f.name.endswith('.PNG')]
img = Image.open(file[0])
imgarr = np.array(img).astype(int)
#print(type(circlearr)) #numpy.ndarray
bw_img = np.array(img.convert('L'))
print(bw_img)
thresarr = np.array(threshold_otsu(bw_img).astype(type(bw_img)))
ImgBlur = ndimage.gaussian_filter(img, sigma=1)
print("ImgBlur Type:",type(ImgBlur))
print("Black White Type:",type(bw_img))
print("Threshold Type:",type(thresarr))

print(thresarr)

#circle_darr = ndimage.binary_dilation(circlearr).astype(circlearr.dtype)
#circle_darrimg = Image.fromarray(circle_darr)

BW_Img = Image.fromarray(bw_img)
Threshold = Image.fromarray(thresarr)
BlurImg = Image.fromarray(ImgBlur)


plt.subplot(131)
plt.imshow(BW_Img)
plt.subplot(132)
plt.imshow(Threshold)
plt.subplot(133)
plt.imshow(BlurImg)
plt.show()