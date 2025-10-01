import cv2
import pandas as pd
from pathlib import Path
from Functions import *

def main():
    mypath = Path().absolute()
    filePath = mypath / 'Desktop\GIT\CollageCreator\Pictures'
       
    collection_names = ['collection1.jpg', 'collection2.jpg', 'collection3.jpg']
    paths = []
    for i in collection_names:
        path = format(filePath / i)
        paths += [path]
    
      
    d = {'name':    ['blue', 'yellow','orange','amber', 'ruby',  'purple', 'green'],
          'x':      [1300,    150,     1320,    170,     860,     840,     50],
          'y':      [330,     820,     800,     80,      630,     1080,    1780],
          'height': [350,     400,     400,     460,     420,     440,     1750],
          'width':  [570,     470,     530,     570,     690,     650,     2000],
          'source': [paths[0],paths[0],paths[0],paths[1],paths[1],paths[1],paths[2]]}
    
    df = pd.DataFrame(data=d)
    
    print(df)
    for i in range(len(df)):
        h, w, y, x = df.loc[i, 'height'], df.loc[i, 'width'], df.loc[i, 'y'], df.loc[i, 'x']
        
        name = str(df.loc[i, 'name']) + '.jpg'
        new_picture = filePath / name
        new_picture = format(new_picture)
        
        source = df.loc[i, 'source']
        collection = cv2.imread(source, 1)
        
        img = crop_image(collection, y, x, h, w, 1, 0)
        
        cv2.imshow(df.loc[i, 'name'], img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        cv2.imwrite(new_picture, img)
   
main()