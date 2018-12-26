import np
def applyFilter(image, kernel):
    output = np.zeros(image.shape, dtype=np.float32)
    channel_count = image.shape[2]
    image_height = image.shape[0]
    image_width = image.shape[1]
    kernel_height = kernel.shape[0]
    kernel_halfh = kernel_height // 2
    kernel_width = kernel.shape[1]
    kernel_halfw = kernel_width // 2
    for y in range(image_height):
        for x in range(image_width):
            x_min = max(0, x - kernel_halfw)
            x_max = min(image_width - 1, x + kernel_halfw)
            y_min = max(0, y - kernel_halfh)
            y_max = min(image_height - 1, y + kernel_halfh)
            for c in range(channel_count):
                value = 0
                for u in range(x_min, x_max + 1):
                    for v in range(y_min, y_max + 1):
                        tmp = kernel[v - y + kernel_halfh, u - x + kernel_halfw]
                        value += image[v, u, c] * tmp  
                value = value if value >= 0 else 0
                value = value if value <= 255 else 255 
                output[y, x, c] = value
    return output
