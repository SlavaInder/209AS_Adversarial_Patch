import numpy as np
import matplotlib.pyplot as plt
import PIL


# allows to plot a single image or one of the images from the array
def show_image(img_array, imge_ind = 0):
    if img_array.shape[0] == 1:
        img = img_array.reshape(300, 300, 3)
    else:
        img = img_array[imge_ind]
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
