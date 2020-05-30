''' 

Automation where we don't need to change the path and image name each and every time we run script but just provide the path to the directory of images

Input:
path : "give the path to the directory of images"
{Example "D://images", "//home//Arvind//supply_data//img"  always use // for / in py for accessing directories}

Process:
Images from different format like 'png', 'tiff', etc. are converted to jpeg with resizing of 600 x 400 and saved.
The conversion from other format like 'tiff' uses RGBA format, so we convert them first to RGB. If no need to convert to RGBA remove the convert() method.

Important: Make sure your destination folder exists
you can also check it by removing the # from continuous 4 line after the input, also copy paste it in for loop to check the detination folder for complete execution.

Output:
Reach to the destination directory where you can find the images manipulated

'''
import os
from PIL import Image
path=input("Enter the path to extract files")
#import sys
#if not(os.path.exists(path)):
#        print("Please input the correct path")
#        sys.exit(1)
ilist=os.listdir(path)
for img in ilist:
        #replace the 'extenstion to change' to any image format you like to read example 'png' or 'tiff'
        if 'extension_to_change' in img:
                #I have converted the image to 'jepg' you can replace "jpeg" with any format you want
                h="path to save the manipulated image" +"imagename" + "." +"jpeg"
                #print(h) 
                #To make sure you have the exact destination path remove # above
                im=Image.open(path+img)
                im.convert('RGB').resize((600,400)).save(h)
#Visit your destination path to find the images