import imageio
import numpy as np
import os, log
def readImage(filename):
    if os.path.exists(filename):
        log.status("reading from " + filename)
        first = imageio.imread(filename)
        first.tofile('.temp.raw')
        imageMemmap = np.memmap('.temp.raw', dtype=np.uint8, shape=first.shape)
        log.status("successfully read from" + filename)
        try:
            os.remove(".temp.raw")
        finally:
            return imageMemmap
        
    else:
        log.error("can't read from " + filename)
        return None

def writeImage(imageMemmap,filename):
    log.status("writing image to "+filename)
    imageio.imwrite(filename, imageMemmap)
    log.status("image successfully write to " + filename)