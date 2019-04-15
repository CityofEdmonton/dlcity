import os
import pandas

def clean_folder(directory):
    df = pandas.read_csv(r"data\streetscore_dataset\csv\combined_score.txt",
                        header=None, sep=' ')

    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            byte_size = os.path.getsize(directory + '\\' + filename)
            if byte_size < 6300:
                
                id = filename.replace(".jpg","")
                df = df.loc[df[0] != id]
                print("invalid image", filename, "removed from combined_score.txt")
                count += 1
                
    df.to_csv(r"data\streetscore_dataset\csv\combined_score.txt",
                header=None, index=None, sep=' ')
    print("removed total of", count, "files")


if __name__ == "__main__":
    directory = r'data\streetscore_dataset\images\\'
    for i in range(1,11):
        print("cleaning: class", i)
        clean_folder(directory + str(i))


                