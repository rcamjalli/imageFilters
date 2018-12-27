import np, convolution

def kernelAsList():
    return [[1,2,3,-12,3,2,1]]

def midKernel():
    kernel = kernelAsList()
    return np.array(kernel).reshape(1,len(kernel[0]))

def midKernelTranspose():
    kernel = kernelAsList()
    return np.array(kernel).reshape(len(kernel[0]),1)
def edgeDetection(image):
    imageEdge = convolution.applyFilter(image, midKernelTranspose())
    return convolution.applyFilter(image,midKernel())