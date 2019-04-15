from streetviewAPI import getImageUrl
import pandas
import numpy

if __name__ == "__main__":
    size = '400x400'
    heading = '' # default heading points to location
    pitch = '0' # default is 0

    file = open('googleapikey.txt', 'r')
    key = file.read() # need the dev key to download from google API

    df = pandas.read_csv(r"H:\workspace\dlcity\yeg_data\train_safe_parsed.csv")
    
    total = df.shape[0]
    count = 0
    saving_interval = 5000
    for index, row in df.iterrows():
        count += 1
        lat = str(row['l_lat'])
        lon = str(row['l_lon'])
        url = str(row['l_url'])
        if url == "url":
            df.loc[index, "l_url"] = getImageUrl(size, lat, lon, heading, pitch, key)
        lat = str(row['r_lat'])
        lon = str(row['r_lon'])
        url = str(row['r_url'])
        if url == "url":
            df.loc[index, "r_url"] = getImageUrl(size, lat, lon, heading, pitch, key)
        print("fetched url: " + str(index+1) + " out of: " + str(total))
        if count % saving_interval == 0:
            df.to_csv(r"H:\workspace\dlcity\yeg_data\train_safe_parsed.csv", sep=',', index=False)
            print("saved!")
    df.to_csv(r"H:\workspace\dlcity\yeg_data\train_safe_parsed.csv", sep=',', index=False)
    print("done")
