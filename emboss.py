import np, convolution

def kernel2dAsList():
    return [[-2,-1,0],[-1,1,1],[0,1,2]]
def kernel2d():
    kernel = kernel2dAsList()
    return np.array(kernel).reshape(len(kernel),len(kernel[0]))
def embossFilter(image):
    return convolution.applyFilter(image,kernel2d())
