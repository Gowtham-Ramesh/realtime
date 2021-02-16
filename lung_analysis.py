import os
from glob import glob
from skimage.io import imread
import nibabel as nib
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops, perimeter
from scipy import ndimage as ndi
from scipy.cluster.vq import kmeans
import numpy as np

p_args = dict(cmap = 'bone', interpolation = 'none')

base_path = os.path.join('Dataset','kaggle', '3d_images')
all_images = glob(os.path.join(base_path,'IMG_*'))
all_masks = [c_path.replace('IMG_','MASK_') for c_path in all_images]
print(len(all_masks),' matching files found:',all_masks[0])

img=nib.load(all_images[0])
test_image=img.get_data()

c_mask=nib.load(all_masks[0])
test_mask=c_mask.get_data()
print('loading images:', test_image.shape, 'and mask:', test_mask.shape)
ref_slice_idx = 100


from skimage.morphology import reconstruction
def fill_image(in_image):
    seed = np.copy(in_image)
    seed[1:-1, 1:-1] = in_image.max()
    mask = in_image
    return reconstruction(seed, mask, method='erosion')
def fill_image_3d(in_image):
    return np.stack([fill_image(c_slice) for c_slice in in_image],0)

fl_image = fill_image_3d(test_image)

dfl_image = np.abs(fl_image - test_image)

# plt.subplot(311)
# plt.imshow(test_image[ref_slice_idx])
# plt.subplot(312)
# plt.imshow(fl_image[ref_slice_idx])
# plt.subplot(313)
# plt.imshow(dfl_image[ref_slice_idx])
# plt.show()

def kmeans_thresh(in_img):
    centers, _ = kmeans(in_img.ravel().astype(np.float32), 2)
    tissue_center, air_center = sorted(centers)
    return np.abs(in_img-air_center)<np.abs(in_img-tissue_center)

k_seg = kmeans_thresh(dfl_image)
# fig, (ax1,ax2) = plt.subplots(1,2)
# ax1.imshow(test_image[ref_slice_idx], cmap = 'bone')
# ax1.set_title('Input Image')
# ax2.imshow(k_seg[ref_slice_idx], cmap = 'bone')
# ax2.set_title('KMeans Seg')

plt.subplot(211)
plt.imshow(test_image[ref_slice_idx])
plt.subplot(212)
plt.imshow(k_seg[ref_slice_idx])
plt.show()


# fig, (ax1,ax2, ax3) = plt.subplots(1,3, figsize = (9,3))
# ax1.imshow(np.sum(test_image,1), cmap = 'bone')
# ax1.set_title('Input Image')
# ax2.imshow(np.sum(k_seg,1), cmap = 'bone')
# ax2.set_title('KMeans Segmented')
# ax3.imshow(np.sum(test_mask,1), cmap = 'bone')
# ax3.set_title('Ground Truth')