import numpy as np
import os

def main():
    image_search()

def image_search():
    base_path = "./image/"
    img_dir = os.listdir("./image/")
    count = 0

    for i in range( 0, len( img_dir ) ):
        img_path = base_path + img_dir[i]

        if os.path.isdir( img_path ):
            image = os.listdir( img_path )
            

main()
