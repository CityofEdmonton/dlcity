import os
import json
import requests
from requests.exceptions import HTTPError
import pandas
import numpy
import urllib.request
import os, sys
from multiprocessing.dummy import Pool as ThreadPool


def getNearbyPhotos(lat, lng, radius):
    api_url_base = 'http://openstreetcam.org/'
    api_url = '{0}1.0/list/nearby-photos/'.format(api_url_base)

    data = {
        'lat': lat,
        'lng': lng,
        'radius': radius
    }

    response = requests.post(api_url, data=data)
    json_response = json.loads(response.content.decode('utf-8'))
    if response.status_code == 200:
        if len(json_response['currentPageItems']) > 0:
            image_url = json_response['currentPageItems'][0]['name']
            # print("+++ Image found within the radius")
            return image_url.replace(image_url.split('/')[0],
                                     'https://%s.openstreetcam.org' % image_url.split('/')[0])
        else:
            # print("--- No image found within the radius!")
            return None
    else:
        print(json_response['status'])
        raise Exception(json_response['status'])


def downloadFromUrl(url, filename):
    '''
    helper function for downloadAllImages
    '''
    if not os.path.exists(filename):
        try:
            urllib.request.urlretrieve(url, filename)
        except:
            pass

def downloadAllImages(filename, image_dir):
    '''
    call downloadFromUrl to download the image from urls for each row
    '''
    df = pandas.read_csv(filename)

    urls = df.apply(lambda row: str(row['url']), axis=1)
    
    filenames = df.apply(lambda row: image_dir+'\\'+ str(row['filename']), axis=1)
    
    pool = ThreadPool(100)
    results = pool.starmap(downloadFromUrl, zip(urls, filenames))


if __name__ == "__main__":
    lat = '53.544325'
    lng = '-113.487864'
    radius = '50'  # 50m radius

    result = getNearbyPhotos(lat, lng, radius)
    if result is not None:
        print(result)
