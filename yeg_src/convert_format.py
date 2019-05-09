import pandas
import numpy
from sklearn.model_selection import train_test_split

def convert_votes_to_train_data():
    filename = r"H:\workspace\dlcity\data\votes\safe.csv"
    df = pandas.read_csv(filename)
    new_df = df.copy()
    new_df = new_df[['left','right', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['left']==row['winner'] else -1, axis=1)
    new_df.to_csv(r'H:\workspace\dlcity\yeg_data\train_safe.csv', index=False, sep=',')

def parse_train_data():
    filename = r"H:\workspace\dlcity\yeg_data\train_safe.csv"
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
    new_df.to_csv(r'H:\workspace\dlcity\yeg_data\train_safe_parsed_emptyurl.csv', index=False, sep=',')

def split_left_right_train_val():
    filename =  r'H:\workspace\dlcity\yeg_data\train_safe_parsed_emptyurl.csv'
    df = pandas.read_csv(filename)
    df[['left']] = r'/home/aimladmin/liyao_workspace/dlcity/yeg_data/images/' + df[['left']]
    df[['right']] = r'/home/aimladmin/liyao_workspace/dlcity/yeg_data/images/' + df[['right']]
    new_df = df.copy()[['left', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['winner']==1 else 0, axis=1)
    train, test = train_test_split(new_df, test_size=0.2, shuffle=False)
    train.to_csv(r'H:\workspace\dlcity\yeg_data\train\train_safe_left.txt', 
                        header=False, index=False, sep=' ')
    test.to_csv(r'H:\workspace\dlcity\yeg_data\train\val_safe_left.txt', 
                        header=False, index=False, sep=' ')

    new_df = df.copy()[['right', 'winner']]
    new_df['winner'] = new_df.apply(lambda row: 1 if row['winner']==-1 else 0, axis=1)
    train, test = train_test_split(new_df, test_size=0.2, shuffle=False)
    train.to_csv(r'H:\workspace\dlcity\yeg_data\train\train_safe_right.txt', 
                        header=False, index=False, sep=' ')
    test.to_csv(r'H:\workspace\dlcity\yeg_data\train\val_safe_right.txt', 
                        header=False, index=False, sep=' ')

# def get_unique_images_list():
#     filename = r"H:\workspace\dlcity\yeg_data\train_safe.csv"
#     df = pandas.read_csv(filename)
#     new_df = df.copy()
#     new_df = new_df[['left','right']]
#     new_df = new_df.stack().reset_index(drop=True)
#     unique_array = new_df.unique()
#     new_df = pandas.DataFrame(unique_array).to_csv(
#         r'H:\workspace\dlcity\yeg_data\images_list.csv', header=None ,index=False, sep=',')

def get_unique_images_list_with_url():
    filename = r"H:\workspace\dlcity\yeg_data\train_safe_parsed_emptyurl.csv"
    df = pandas.read_csv(filename)
    df1 = df.copy()[['left','l_id','l_lat','l_lon','l_city','l_url']]
    df2 = df.copy()[['right','r_id','r_lat','r_lon','r_city','r_url']]
    df1.columns = ['filename','id','lat','lon','city','url']
    df2.columns = ['filename','id','lat','lon','city','url']
    df1 = df1.append(df2)
    df1.drop_duplicates().to_csv(
        r'H:\workspace\dlcity\yeg_data\images_list_emptyurl.csv', index=False, sep=',')

def filter_by_cities(cities):
    filename = r"H:\workspace\dlcity\yeg_data\train_safe_parsed_emptyurl.csv"
    df = pandas.read_csv(filename)
    new_df = df.copy()
    new_df = new_df[new_df['l_city'].isin(cities)]
    new_df = new_df[new_df['r_city'].isin(cities)]
    new_df.to_csv(r'H:\workspace\dlcity\yeg_data\train_safe_parsed_emptyurl_partial.csv', index=False, sep=',')
