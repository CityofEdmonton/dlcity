'''
load the index and url for each image from the csv file
then sign using the google api secret
save result images named as index, e.g. : nyc_125.jpg , boston_111.jpg

fetch from each category evenly, save images in r'data\streetscore_dataset\images\i'
'''
from streetviewAPI import getImageUrl
import pandas
import numpy
from urlsigner import sign_url
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

def fetchImage(key, secret, filename, image_dir, signature):
    df = pandas.read_csv(filename)
    if signature:
        urls = df.apply(lambda row: sign_url(input_url=str(row['url']), secret=secret), axis=1)
    else:
        urls = df.apply(lambda row: str(row['url']), axis=1)
    
    filenames = df.apply(lambda row: image_dir+'\\'+ str(row['filename']), axis=1)
    
    pool = ThreadPool(100)
    results = pool.starmap(geturl, zip(urls, filenames))


if __name__ == "__main__":
    file = open('googleapikey.txt', 'r')
    key = file.read() # need the dev key to download from google API
    file.close()

    file = open('googleapisecret.txt', 'r')
    secret = file.read() # need the secret to sign the download url
    file.close()

    # the downloading part
    image_dir = r"yeg_data\images"
    filename = r"yeg_data\images_list.csv"
    fetchImage(key, secret, filename, image_dir, signature=True)
