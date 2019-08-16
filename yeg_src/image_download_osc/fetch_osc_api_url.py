from osc_api import getNearbyPhotos
import pandas
import numpy


if __name__ == "__main__":
    radius = 200 # radius = 200m
    df = pandas.read_csv(r"yeg_data\images_list_osc.csv")
    
    total = df.shape[0]
    count = 0
    display_interval = 100
    saving_interval = 5000
    for index, row in df.iterrows():
        count += 1
        lat = str(row['lat'])
        lon = str(row['lon'])
        url = str(row['url'])
        if url == "url":
            try:
                result = getNearbyPhotos(lat, lon, radius)
                if result is not None:
                    df.loc[index, "url"] = result
                else:
                    df.loc[index, "url"] = 'not found'
            except Exception as err:
                print(err)
                continue
        if count % display_interval == 0:
            print("fetched url: " + str(index+1) + " out of: " + str(total))        
        if count % saving_interval == 0:
            df.to_csv(r"yeg_data\images_list_osc.csv", sep=',', index=False)
            print("saved!")
    df.to_csv(r"yeg_data\images_list_osc.csv", sep=',', index=False)
    print("done")