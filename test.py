import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import os
import glob

folder_path = "/Users/sahilgill/Downloads/temp"
files_path = os.path.join(folder_path, '*')
files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True) 
print("FILES: ",files)


def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

s = imageio.imread(files[0])
g=grayscale(s)
i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r= dodge(b,g)

plt.imshow(r, cmap="gray")
plt.imsave('img.png', r, cmap='gray', vmin=0, vmax=255)


