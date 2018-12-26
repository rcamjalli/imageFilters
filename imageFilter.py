import time, argparse, imageIO
from blur import blur
from edgeDetector import edgeDetection
import basicFilters

parser = argparse.ArgumentParser()
parser.add_argument('--blur', action='store_true')
parser.add_argument('--sigma', nargs='?', type=float, default=3.0)
parser.add_argument('--invert_colors', action='store_true')
parser.add_argument('--grayscale', action='store_true')
parser.add_argument('--edge', action='store_true')
parser.add_argument('--color_filter', action='store_true')
parser.add_argument('--color', help='red,green,blue,brown', type=str, default="red")
parser.add_argument("input_file", help="The input image file.")
parser.add_argument("output_file", help="The output image file.")
args = parser.parse_args()

img = imageIO.readImage(args.input_file)

if img is not None:
    startTime = time.time()
    if args.blur:
        blurImage = blur(img,args.sigma)
        imageIO.writeImage(blurImage,args.output_file)
    elif args.edge:
        edgeImage = edgeDetection(img)
        imageIO.writeImage(edgeImage,args.output_file)
    elif args.invert_colors:
        invertImage = basicFilters.invertColors(img)
        imageIO.writeImage(invertImage,args.output_file)
    elif args.grayscale:
        grayscaleImage = basicFilters.grayscaleFilter(img)
        imageIO.writeImage(grayscaleImage,args.output_file)
    elif args.color_filter:
        color = None
        if args.color == "red":
            color = [191,90,47]
        elif args.color == "green":
            color = [47,191,90]
        elif args.color == "blue":
            color = [47,90,191]
        elif args.color == "brown":
            color = [104,54,33]
        if color is not None:
            colorImage = basicFilters.colorFiler(img,color)
            imageIO.writeImage(colorImage,args.output_file)
    print ("finish in " + str(round(time.time()-startTime,4)) + "s")
