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


def fetchImage(key, secret, filename, image_dir, day_limit, signature):
    df = pandas.read_csv(filename)
    limit = int(day_limit)
    for index, row in df.iterrows():
        # if index > 100:
        #     break
        # download left
        if limit <= 0:
            break
        filename = image_dir + '\\' + str(row['filename'])
        if not os.path.isfile(filename):            
            url = str(row['url'])
            if signature:
                signed_url = sign_url(input_url=url, secret=secret)
            else:
                signed_url = url
            try:
                # print(signed_url)
                urllib.request.urlretrieve(signed_url, filename)
                # remove invalid image
                # byte_size = os.path.getsize(filename)
                # if byte_size < 5500:
                #     os.remove(filename)
                #     print('invalid image removed:', filename)
                print("limit remaining:", limit, filename)
                limit -= 1
            except Exception as e:
                print(e)
                print("fetching: ",index+1," failed!")
                if "403" in str(e) :
                    print("exceed limit, exiting!")
                    break
                else:
                    print("skipped!")


if __name__ == "__main__":
    file = open('googleapikey.txt', 'r')
    key = file.read() # need the dev key to download from google API
    file.close()

    file = open('googleapisecret.txt', 'r')
    secret = file.read() # need the secret to sign the download url
    file.close()

    # the downloading part
    image_dir = r"H:\workspace\dlcity\yeg_data\images"
    filename = r"H:\workspace\dlcity\yeg_data\image_list.csv"
    fetchImage(key, secret, filename, image_dir, day_limit=104858, signature=True)
    # fetchImage(key, secret, filename, image_dir, day_limit=1000, signature=False)
