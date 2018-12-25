from scipy import misc
import os, np
def readImage(filename):
    if os.path.exists(filename):
        first = misc.imread(filename)
        first.tofile('.temp.raw')
        imageMemmap = np.memmap('.temp.raw', dtype=np.uint8, shape=first.shape)
        os.remove(".temp.raw")
        return imageMemmap
    else:
        print("The file does not exist")
        return None

def writeImage(imageMemmap,filename):
    misc.imsave(filename, imageMemmap)