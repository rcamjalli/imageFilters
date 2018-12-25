from scipy import misc
import os, np
def readImage(filename):
    if os.path.exists(filename):
        first = misc.imread(filename)
        first.tofile('.temp.raw')
        imageMemmap = np.memmap('.temp.raw', dtype=np.uint8, shape=first.shape)
        try:
            os.remove(".temp.raw")
        finally:
            return imageMemmap
        
    else:
        print("The file does not exist")
        return None

def writeImage(imageMemmap,filename):
    misc.imsave(filename, imageMemmap)