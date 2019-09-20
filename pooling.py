import numpy as np
def pooling_greyscale(image):
    output = np.zeros((image.shape[0]//2,image.shape[1]//2,3), dtype=np.float32)
    x = 0
    while x//2 < image.shape[0]//2:
        y = 0
        while y//2 < image.shape[1]//2:
            max_pixel = greyscale_pixel(image[x,y])
            if (image.shape[0] - x) >= 1:
                max_pixel = max(greyscale_pixel(image[x+1,y]),max_pixel)
            if (image.shape[1] - y) >= 1:
                max_pixel = max(greyscale_pixel(image[x,y+1]), max_pixel)
            if (image.shape[0] - x) >= 1 and (image.shape[1] - y) >= 1:
                max_pixel = max(greyscale_pixel(image[x+1,y+1]),max_pixel)
            output[x//2,y//2] = [max_pixel,max_pixel,max_pixel]
            y += 2
        x += 2
    return output
def greyscale_pixel(pixel):
    return (int(pixel[0])+int(pixel[1])+int(pixel[2]))/3