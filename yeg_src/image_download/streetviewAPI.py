# Import google_streetview for the api module
import google_streetview.api
import os
# Define parameters for street view api

def getImage(size, lat, lon, heading, pitch, key):
    params = [{
    'size': size, # max 640x640 pixels
    'location': lat + "," + lon,
    'heading': heading,
    'pitch': pitch,
    'key': key
    }]

    name = lat + "_" + lon
    # Create a results object
    results = google_streetview.api.results(params)

    # Download images to directory 'downloads'
    # results.download_links('data\\downloads')
    
    # Save links
    # results.save_links('data\\downloads\\links.txt')
    url = results.links[0]
    f = open('data\\downloads\\'+ name + '.txt', 'w+')
    f.write(url) # need the dev key to download from google API
    f.close()

    # Save metadata
    # results.save_metadata('data\\downloads\\metadata.json')

    # os.rename("gsv_0.jpg", name + ".jpg")

def getImageUrl(size, lat, lon, heading, pitch, key):
    params = [{
    'size': size, # max 640x640 pixels
    'location': lat + "," + lon,
    'heading': heading,
    'pitch': pitch,
    'key': key,
    'source': 'outdoor' # outdoor images only
    }]

    # name = lat + "_" + lon
    # Create a results object
    results = google_streetview.api.results(params)
    url = results.links[0]

    return url

   
    
if __name__ == "__main__":
    size = '600x400'
    lat = '40.704906'
    lon = '-74.0084'
    heading = ''
    pitch = '0'
    file = open('googleapikey.txt', 'r')
    key = file.read() # need the dev key to download from google API
    # file = open('googleapisecret.txt', 'r')
    # secret = file.read() # need the secret to download from google API

    # getImage(size, lat, lon, heading, pitch, key)
    print(getImageUrl(size, lat, lon, heading, pitch, key))