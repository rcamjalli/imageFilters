import convolution
import numpy as np
def gaussian_kernel_1d(sigma):
    kernel_radius = np.ceil(sigma) * 3
    kernel_size = kernel_radius * 2 + 1
    ax = np.arange(-kernel_radius, kernel_radius + 1., dtype=np.float32)
    kernel = np.exp(-(ax**2) / (2. * sigma**2))
    return (kernel / np.sum(kernel)).reshape(1,kernel.shape[0])

def blur(image,sigma):
    imageBlur = convolution.applyFilter(image,gaussian_kernel_1d(3.0))   
    return convolution.applyFilter(imageBlur,gaussian_kernel_1d(3.0).transpose()) 