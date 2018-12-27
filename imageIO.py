from scipy import misc
import os, np
def readImage(filename):
    if os.path.exists(filename):
        print ("Log: reading from " + filename)
        first = misc.imread(filename)
        first.tofile('.temp.raw')
        imageMemmap = np.memmap('.temp.raw', dtype=np.uint8, shape=first.shape)
        print("Log: successfully read from" + filename)
        try:
            os.remove(".temp.raw")
        finally:
            return imageMemmap
        
    else:
        print("Error: can't read from " + filename)
        return None

def writeImage(imageMemmap,filename):
    print("Log: writing image to "+filename)
    misc.imsave(filename, imageMemmap)
    print("Log: image successfully write to " + filename)