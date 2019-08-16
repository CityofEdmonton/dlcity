import pandas
import numpy
import os
from sklearn.model_selection import train_test_split

def convert_votes_to_train_data():
    filename = r"data\votes\safe.csv"
    df = pandas.read_csv(filename)
    new_df = df.copy()
    new_df = new_df[['left','right', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['left']==row['winner'] else -1, axis=1)
    new_df.to_csv(r'yeg_data\train_safe.csv', index=False, sep=',')

def parse_train_data():
    filename = r"yeg_data\train_safe.csv"
    df = pandas.read_csv(filename)
    new_df = df.copy()
    # new_df = pandas.DataFrame(columns=['l_lat', 'l_lon', 'l_id', 'r_lat', 'r_lon', 'r_id'])
    new_df['l_id'] = df.apply(lambda row: row['left'].split('_')[2], axis=1)
    new_df['l_lat'] = df.apply(lambda row: row['left'].split('_')[0], axis=1)
    new_df['l_lon'] = df.apply(lambda row: row['left'].split('_')[1], axis=1)
    new_df['l_city'] = df.apply(lambda row: row['left'].strip(".JPG").split('_')[3], axis=1)
    new_df['l_url'] = 'url'
    new_df['r_id'] = df.apply(lambda row: row['right'].split('_')[2], axis=1)
    new_df['r_lat'] = df.apply(lambda row: row['right'].split('_')[0], axis=1)
    new_df['r_lon'] = df.apply(lambda row: row['right'].split('_')[1], axis=1)
    new_df['r_city'] = df.apply(lambda row: row['right'].strip(".JPG").split('_')[3], axis=1)
    new_df['r_url'] = 'url'
    new_df.to_csv(r'yeg_data\train_safe_parsed_emptyurl.csv', index=False, sep=',')

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

def split_left_right_train_val(train_ratio = 0.65, val_ratio = 0.05, test_ratio = 0.30): 
    filename =  r'yeg_data\train_safe_parsed_emptyurl.csv'
    df = pandas.read_csv(filename)
    df[['left']] = r'/home/aimladmin/liyao_workspace/dlcity/yeg_data/images/' + df[['left']]
    df[['right']] = r'/home/aimladmin/liyao_workspace/dlcity/yeg_data/images/' + df[['right']]
    new_df = df.copy()[['left', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['winner']==1 else 0, axis=1)
    train_and_test, val = train_test_split(new_df, test_size=val_ratio, shuffle=False)
    train, test = train_test_split(train_and_test, test_size=(test_ratio/(train_ratio+test_ratio)), shuffle=False)
    train.to_csv(r'yeg_data\train\train_safe_left.txt', 
                        header=False, index=False, sep=' ')
    val.to_csv(r'yeg_data\train\val_safe_left.txt', 
                        header=False, index=False, sep=' ')
    test.to_csv(r'yeg_data\train\test_safe_left.txt', 
                        header=False, index=False, sep=' ')

    new_df = df.copy()[['right', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['winner']==-1 else 0, axis=1)
    train_and_test, val = train_test_split(new_df, test_size=val_ratio, shuffle=False)
    train, test = train_test_split(train_and_test, test_size=(test_ratio/(train_ratio+test_ratio)), shuffle=False)
    train.to_csv(r'yeg_data\train\train_safe_right.txt', 
                        header=False, index=False, sep=' ')
    val.to_csv(r'yeg_data\train\val_safe_right.txt', 
                        header=False, index=False, sep=' ')
    test.to_csv(r'yeg_data\train\test_safe_right.txt', 
                        header=False, index=False, sep=' ')

# def get_unique_images_list():
#     filename = r"yeg_data\train_safe.csv"
#     df = pandas.read_csv(filename)
#     new_df = df.copy()
#     new_df = new_df[['left','right']]
#     new_df = new_df.stack().reset_index(drop=True)
#     unique_array = new_df.unique()
#     new_df = pandas.DataFrame(unique_array).to_csv(
#         r'yeg_data\images_list.csv', header=None ,index=False, sep=',')

def get_unique_images_list_with_url():
    filename = r"yeg_data\train_safe_parsed_emptyurl.csv"
    df = pandas.read_csv(filename)
    df1 = df.copy()[['left','l_id','l_lat','l_lon','l_city','l_url']]
    df2 = df.copy()[['right','r_id','r_lat','r_lon','r_city','r_url']]
    df1.columns = ['filename','id','lat','lon','city','url']
    df2.columns = ['filename','id','lat','lon','city','url']
    df1 = df1.append(df2)
    df1.drop_duplicates().to_csv(
        r'yeg_data\images_list_emptyurl.csv', index=False, sep=',')

def filter_by_cities(cities):
    filename = r"yeg_data\train_safe_parsed_emptyurl.csv"
    df = pandas.read_csv(filename)
    new_df = df.copy()
    new_df = new_df[new_df['l_city'].isin(cities)]
    new_df = new_df[new_df['r_city'].isin(cities)]
    new_df.to_csv(r'yeg_data\train_safe_parsed_emptyurl_partial.csv', index=False, sep=',')


def main():
    convert_votes_to_train_data()
    parse_train_data()
    split_left_right_train_val()
    get_unique_images_list_with_url()

if __name__ == "__main__":
    main()