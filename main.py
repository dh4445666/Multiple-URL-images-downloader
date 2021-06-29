# import
import pandas as pd
import urllib.request

#.........................
def url_jpg(i,url,file_path):
    filename = 'image={}'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)
    print('{} saved.'.format(filename))
    return None

# ........................

# File name
FILENAME = '' #add nmae of the excel csv file
FILEPATH = '' # add path of the file saved

# To read url as panda dataframe
urls = pd.read_csv(FILENAME)

#save images to directory
for i, url in enumerate(urls.values):
