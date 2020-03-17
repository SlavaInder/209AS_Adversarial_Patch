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


# this function creates copies of patch
@tf.function
def multiply(single_patch, train_images):
    single_patch = tf.expand_dims(single_patch, axis=0)
    patch_array = tf.tile(single_patch, (tf.shape(train_images)[0], 1, 1, 1))	
    
    return(patch_array)


@tf.function
def fold(array_images, starting, thickness):
    # Array of images
    # Float32, and int32 
    
    mask_fill_thickness = tf.zeros([tf.shape(array_images)[0], tf.shape(array_images)[1], thickness, 3], tf.float32, name='mask_fill_thickness')
    mask_left = tf.slice(array_images, [0, 0, 0, 0], [-1, -1, starting, -1]) 
    mask_right_start = starting+thickness
    mask_right = tf.slice(array_images, [0, 0, mask_right_start, 0], [-1, -1, -1, -1])
    mask_appended = tf.concat([mask_left, mask_right], axis=2, name='mask_appended')
    mask_without_fill = tf.concat([mask_left, mask_right, mask_fill_thickness], axis=2, name='mask_appended')    
    
    # Let's add the -2 fills now 
    mask_fill = tf.ones([tf.shape(array_images)[0], tf.shape(array_images)[1], thickness, 3], 
                        tf.float32, 
                        name='mask_fill')
    mask_fill_two = tf.subtract(mask_fill, 3, name='mask_fill_two')
    remaining = tf.shape(array_images)[2] - thickness
    mask_fill_zeros = tf.zeros([tf.shape(array_images)[0], tf.shape(array_images)[1], remaining, 3], tf.float32, name='mask_fill_zeroes')    
        
    mask_fill_final = tf.concat([mask_fill_zeros, mask_fill_two], axis=2, name='mask_fill_final')    
    out = tf.add(mask_without_fill, mask_fill_final)
    
    return out
