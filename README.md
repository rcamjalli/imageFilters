# Image Filters
## Python 
To run this code you need python 2.7 or newer. I've test this in Mac OS X and Windows 10, also it should work well in Linux.

## Running the code
The program needs an input image file and an output image path. There are 4 avaiable filters at the moment, blur, edge detection, color inversion and color filter.
If the file is too big it wil take a long time to process the image, take in mind that is Python code and is under development.

## Examples

Input File | 
------------ |
![input img](https://i.imgur.com/DNBiwzn.jpg) | 

### Blur Effect

`python imageFilter.py --blur images/input.jpeg images/output.jpeg`

Also you can change the sigma value by a float number like this `--sigma 6.0`, by default the value is 3.0

Output File | 
------------ |
![blur img](https://i.imgur.com/YWQphHJ.jpg) | 

### Edge Detection Effect

`python imageFilter.py --edge images/input.jpeg images/output.jpeg`

Output File | 
------------ |
![edge img](https://i.imgur.com/VHJtube.jpg) | 

### Invert Colors

`python imageFilter.py --invert_colors images/input.jpeg images/output.jpeg`

Output File | 
------------ |
![invert img](https://i.imgur.com/LR6TuPG.jpg) | 

### Color Filter

`python imageFilter.py --color_filter --color red images/input.jpeg images/output.jpeg`

The avaiable colors are  `[red,green,blue,brown]`

| Red | Green | Blue | Brown | 
| --- | ----- | ---- | ----- |
| ![red img](https://i.imgur.com/HNBHKp9.jpg) | ![green img](https://i.imgur.com/acO15Dv.jpg) | ![blue img](https://i.imgur.com/jS4HmIe.jpg) | ![brown img](https://i.imgur.com/dKslZfo.jpg) |

### Grayscale Filter

`python imageFilter.py --grayscale images/input.jpeg images/output.jpeg`

Output File | 
--
![grayscale img](https://i.imgur.com/DxwKCz0.jpg)|



