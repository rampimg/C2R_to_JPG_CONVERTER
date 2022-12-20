#!/usr/bin/env python

# import what we need
import numpy
import os
import glob
import time
import argparse
from PIL import Image
from rawkit import raw

# params
parser = argparse.ArgumentParser(description='Convert CR2 to JPG')
parser.add_argument('-s', '--source',help='Source folder of CR2 files', required=True)
parser.add_argument('-d', '--destination', help='Destination folder for converted JPG files', required=True)
args = parser.parse_args()

# dirs and files
raw_file_type = ".CR2"
raw_dir = args.source + '/'
converted_dir = args.destination + '/'
raw_images = os.listdir(raw_dir)#glob.glob(raw_dir + '*' + raw_file_type)

# converter function which iterates through list of files
def convert_cr2_to_jpg(raw_images):
    
    for raw_image in raw_images:
        #print "Converting the following raw image: " + raw_image + " to JPG"
            
        file = raw_dir+"/"+raw_image
        im = Image.open(file)
        #rgb_im = im.frombytes('RGB')
        rgb_im = im.convert('RGB')
        rgb_im.save(converted_dir + raw_image[:-4]+ '.JPG',quality = 125)

# call function
if __name__ == "__main__":
    print('run')
    print(raw_dir)
    print(converted_dir)
    print(raw_dir + '*' + raw_file_type)
    print(raw_images)
    convert_cr2_to_jpg(raw_images)
