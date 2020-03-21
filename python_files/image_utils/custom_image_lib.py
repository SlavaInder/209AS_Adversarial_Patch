import random
import numpy as np
import matplotlib.pyplot as plt
import PIL


# allows to plot a single image or one of the images from the array
def show_image(img_array, imge_ind = 0):
    if len(img_array.shape) == 3:
        img = img_array
    elif img_array.shape[0] == 1:
        img = img_array.reshape(img_array.shape[1], img_array.shape[2], img_array.shape[3])
    else:
        img = img_array[imge_ind]

    plt.figure(figsize=(5,5))    
    plot = plt.imshow(img)
    plt.show()


# image and probs should be for single class!
def show_probs(img, p, labels, correct_class=None, target_class=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 8))
    fig.sca(ax1)
    ax1.imshow(img)
    fig.sca(ax1)
    
    topk = list(p.argsort()[-10:][::-1])
    topprobs = p[topk]
    barlist = ax2.bar(range(10), topprobs)
    if target_class in topk:
        barlist[topk.index(target_class)].set_color('r')
    if correct_class in topk:
        barlist[topk.index(correct_class)].set_color('g')
    plt.sca(ax2)
    plt.ylim([0, 1.1])
    plt.xticks(range(10),
               [labels[i][:15] for i in topk],
               rotation='vertical')
    fig.subplots_adjust(bottom=0.2)
    plt.show()


# Input images should be scaled to the range of [-1, 1] and have format (num_images, 299, 299, 3)
# this function takes as an input an array of *.jpg images (because *.png-s actually have 4-dims),
# crops them to the size 300x300, and convert them to proper shape
def preprocessing(raw_pillow_images):
    # init output array
    np_images = np.zeros(shape=(len(raw_pillow_images), 300, 300, 3))

    for i in range(len(raw_pillow_images)):
        # just in case convert to proper format
        raw_pillow_images[i] = raw_pillow_images[i].convert('RGB')

        # scale the image in a way that maps its smaller dimension to the length of 300
        wide = raw_pillow_images[i].width > raw_pillow_images[i].height
        if wide:
            new_width = int(raw_pillow_images[i].width * 300 / raw_pillow_images[i].height)
            new_height = 300
        else:
            new_width = 300
            new_height = int(raw_pillow_images[i].height * 300 / raw_pillow_images[i].width)

        # actually scale image 
        raw_pillow_images[i] = raw_pillow_images[i].resize((new_width, new_height))  

        # crop exceeding dimension
        raw_pillow_images[i] = raw_pillow_images[i].crop((0, 0, 300, 300))
    
        # scale to [0, 1]
        pillow_image = (np.asarray(raw_pillow_images[i]) / 255.0).astype(np.float32)
    
        np_images[i] = ((pillow_image - 0.5) * 2).reshape(1, 300, 300, 3)
        
    return np_images


# this function rescales output of the learning from [-1; 1] to [0, 1] which can be used by PIL
def postprocessing(image_array):
	return ((image_array / 2) + 0.5)


# this function takes samples random images having index
def sample_images_with_index(folder_index, num_images, folder):
    # init array of raw images
    my_raw_pillow_images = []

    # sample raw images
    for i in range(num_images):
        # sample class of the image
        current_class = random.choice(list(folder_index.keys()))
        # sample random index of image
        random_index = np.random.randint(folder_index[current_class][0], folder_index[current_class][1])
        # append new image
        my_raw_pillow_images.append(PIL.Image.open(folder + current_class + '/' + current_class[:-1] + str(random_index) + '.jpg'))

    # preprocess random images
    return preprocessing(my_raw_pillow_images)


# this function samples random images
def sample_images(num_images, folder):
    # read info about image set
    with open(folder + "/index.txt", "r") as f:
        names, indices = f.read().split("\n")
    names = names.split(" ")
    names.pop()
    indices = indices.split(" ")
    indices.pop()
    index = {}

    # pack info in a dictionary
    for i in range(len(names)):
        index[names[i]] = [int(indices[2*i]), int(indices[2*i+1])]
        
    # sample images having index
    return sample_images_with_index(index, num_images, folder + '/images/')


# this function protects from missing images
def sample_image_wrapper(num_images, folder):
    result = None
    while result is None:
        try:
            result = sample_images(num_images, folder)
        except:
            pass
    return result


# this function samples fold for an image of given size
def fold_sampler(size, thickness):
    # choose a start side
    start_side = np.random.randint(0, 4)

    # top
    if start_side == 0:
        x_start, y_start = sample_dot(size, thickness, 0)
        x_end, y_end = sample_dot(size, thickness, 1)
    # right
    elif start_side == 1:
        x_start, y_start = sample_dot(size, thickness, 1)
        x_end, y_end = sample_dot(size, thickness, 2)
    # bottom
    if start_side == 2:
        x_start, y_start = sample_dot(size, thickness, 2)
        x_end, y_end = sample_dot(size, thickness, 3)
    # left
    if start_side == 3:
        x_start, y_start = sample_dot(size, thickness, 3)
        x_end, y_end = sample_dot(size, thickness, 0)

    return x_start, y_start, x_end, y_end


#        end_side = np.random.choice((1, 2, 3), 1)[0]
        



# this function samples fold for an image of given size
def sample_dot(size, thickness, side):
    # top
    if side == 0:
        y = size
        x = np.random.randint(thickness+18, size-thickness-18)
    # right
    elif side == 1:
        x = size
        y = np.random.randint(thickness+18, size-thickness-18)
    # bottom
    elif side == 2:
        y = 0
        x = np.random.randint(thickness+18, size-thickness-18)
    # left
    else:
        x = 0
        y = np.random.randint(thickness+18, size-thickness-18)

    return x, y


