from streetviewAPI import getImageUrl
import pandas
import numpy


# def fetch_url(lat,lon,url):
#     lat = str(lat)
#     lon = str(lon)
#     url = str(url)
#     if url == "url":
#         return getImageUrl(size, lat, lon, heading, pitch, key)
#     else:
#         return url

if __name__ == "__main__":
    size = '400x400'
    heading = '' # default heading points to location
    pitch = '0' # default is 0

    file = open('googleapikey.txt', 'r')
    key = file.read() # need the dev key to download from google API

    df = pandas.read_csv(r"H:\workspace\dlcity\yeg_data\images_list.csv")
    
    total = df.shape[0]
    count = 0
    saving_interval = 5000
    for index, row in df.iterrows():
        count += 1
        lat = str(row['lat'])
        lon = str(row['lon'])
        url = str(row['url'])
        if url == "url":
            df.loc[index, "url"] = getImageUrl(size, lat, lon, heading, pitch, key)
        print("fetched url: " + str(index+1) + " out of: " + str(total))
        if count % saving_interval == 0:
            df.to_csv(r"H:\workspace\dlcity\yeg_data\images_list.csv", sep=',', index=False)
            print("saved!")
    df.to_csv(r"H:\workspace\dlcity\yeg_data\images_list.csv", sep=',', index=False)
    print("done")

    # df["l_url"] = df.apply(lambda row: fetch_url(row['l_lat'], row['l_lon'], row['l_url']), axis=1)
    # df["r_url"] = df.apply(lambda row: fetch_url(row['r_lat'], row['r_lon'], row['r_url']), axis=1)