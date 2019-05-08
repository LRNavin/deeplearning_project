from __future__ import division, print_function
import pandas as pd


data_drive_1 = 'C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master'
dat = pd.read_csv('C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master/train_info/train_info.csv')
img_dir = 'C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master/train_1'


image_groups = {}
for index, row in dat.iterrows():
    img_name = row['filename']
    group_name = row['artist']
    if group_name in image_groups:
        image_groups[group_name].append(img_name)
    else:
        image_groups[group_name] = [img_name]

csv_top = []

for i in image_groups:
   csv_top.append((i,len(image_groups[i])))

csv_top = sorted(csv_top,key=lambda l:l[1], reverse=True)

x = 3

def get_top(x):
    return print(csv_top[:x])

get_top(x)