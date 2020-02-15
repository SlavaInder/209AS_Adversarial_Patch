import tensorflow as tf
import numpy as np

# this function expects all "empty" pixels to be set to -2.
# pixels that belong to a patch have range of [-1, 1]
@tf.function
def applicator(mapped_patches, original_images):
	# prepare a mask for original images
	img_mask = tf.math.abs(tf.math.add(tf.math.sign(tf.math.add(mapped_patches, 2)), -1))
    # crop the place for the pathch
	cropped_images = tf.math.multiply(original_images, img_mask)

	# prepare a mask for patches
	patch_mask = tf.math.sign(tf.math.add(mapped_patches, 2))

	# crop patch from the field of -2-s
	cropped_patch = tf.math.multiply(mapped_patches, patch_mask)

	# get images with patches
	images_with_patches = cropped_images + cropped_patch

	return(images_with_patches)


# this function maps all patches to a particular place on the image
# this place is the ssame for all images.
@tf.function
def shift(folded_patches, x_shift, y_shift):
	# get dimensions of the patch
	dims = tf.shape(folded_patches)

	# update patch lenth
	a = tf.concat((folded_patches, -2 * tf.ones(shape=(dims[0], dims[1], 300 - dims[2], 3), dtype=tf.float32)), axis=2)

	# update patch height
	b = tf.concat((a, -2 * tf.ones(shape=(dims[0], 300 - dims[1], 300, 3))), axis=1)

	# shift the patch to the place needed
	mapped_patches = tf.roll(b, shift = (x_shift, y_shift), axis = (2, 1))

	return(mapped_patches)


# this function maps patches to different places on the image
@tf.function
def _shift(folded_patches, x_shift, y_shift):
	# do this using loop
	pass


# this function creates copies of patch
@tf.function
def multiply(single_patch, train_images):
    single_patch = tf.expand_dims(single_patch, axis=0)
    patch_array = tf.tile(single_patch, (tf.shape(train_images)[0], 1, 1, 1))	
    
    return(patch_array)

