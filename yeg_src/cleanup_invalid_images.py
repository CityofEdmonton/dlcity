import pandas
import numpy
import os

def is_valid(row, valid_list):
    left = str(row['left'])
    right = str(row['right'])  
    if (left in valid_list) and (right in valid_list):
        return True
    else:
        return False

def cleanup_invalid_images():
    filename =  r'yeg_data\train_safe_parsed_emptyurl.csv'
    df = pandas.read_csv(filename)
    valid_list = os.listdir(r'yeg_data\images')
    df['is_valid'] = df.apply(lambda row : is_valid(row, valid_list), axis=1)
    df = df[df.is_valid == True].drop(labels='is_valid', axis=1)
    df.to_csv(r'yeg_data\train_safe_parsed_emptyurl.csv', index=False, sep=',')