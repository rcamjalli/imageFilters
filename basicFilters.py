import numpy as np
def invertColors(image):
    output = np.zeros(image.shape, dtype=np.float32)
    channel_count = image.shape[2]
    image_height = image.shape[0]
    image_width = image.shape[1]
    for y in range(image_height):
        for x in range(image_width):
            for c in range(channel_count):
                output[y,x,c] = 255 - image[y,x,c]
    return output

def colorFiler(image,color):
    output = np.zeros(image.shape, dtype=np.float32)
    channel_count = image.shape[2]
    image_height = image.shape[0]
    image_width = image.shape[1]
    for y in range(image_height):
        for x in range(image_width):
            for c in range(channel_count):
                output[y,x,c] = (color[c] + image[y,x,c])/2
    return output

def grayscaleFilter(image):
    output = np.zeros(image.shape, dtype=np.float32)
    channel_count = image.shape[2]
    image_height = image.shape[0]
    image_width = image.shape[1]
    for y in range(image_height):
        for x in range(image_width):
            value = 0
            for c in range(channel_count):
                value += image[y,x,c]
            value /= 3
            output[y,x] = [value,value,value]
    return output

def grayscaleFilter_1D(image):
    output = np.zeros((image.shape[0],image.shape[1]), dtype=np.float32)
    channel_count = image.shape[2]
    image_height = image.shape[0]
    image_width = image.shape[1]
    for y in range(image_height):
        for x in range(image_width):
            value = 0
            for c in range(channel_count):
                value += image[y,x,c]
            value /= 3
            output[y,x] = value
    return output