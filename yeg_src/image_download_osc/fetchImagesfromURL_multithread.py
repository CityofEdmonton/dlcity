'''
load the index and url for each image from the csv file
then sign using the google api secret
save result images named as index, e.g. : nyc_125.jpg , boston_111.jpg

fetch from each category evenly, save images in r'data\streetscore_dataset\images\i'
'''
import pandas
import numpy
import urllib.request
import os, sys
import cv2
from multiprocessing.dummy import Pool as ThreadPool

def geturl(url, filename):
    if not os.path.exists(filename):
        try:
            urllib.request.urlretrieve(url, filename)
            # print(url,filename)
        except:
            pass

def fetchImage(filename, image_dir):
    df = pandas.read_csv(filename)
    
    urls = df.apply(lambda row: str(row['url']), axis=1)
    
    filenames = df.apply(lambda row: image_dir+'\\'+ str(row['filename']), axis=1)
    
    pool = ThreadPool(100)
    results = pool.starmap(geturl, zip(urls, filenames))


if __name__ == "__main__":
    image_dir = r"yeg_data\images_osc"
    filename = r"yeg_data\images_list_osc.csv"
    fetchImage(filename, image_dir)
