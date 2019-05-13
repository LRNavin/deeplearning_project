from __future__ import division, print_function
import pandas as pd


data_drive_1 = 'C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master'
dat = pd.read_csv('C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master/train_info/train_info.csv')
img_dir = 'C:/Users/Jose Maria Soengas/Documents/siamese-CNN-master/train_1'


#x = number of artists you want
def get_top(x):
    #create dictionary of all artists and paintings
    image_groups = {}
    for index, row in dat.iterrows():
        img_name = row['filename']
        group_name = row['artist']
        if group_name in image_groups:
            image_groups[group_name].append(img_name)
        else:
            image_groups[group_name] = [img_name]

    csv_top = []

    #create an arracy of artists and the number of paintings they've drawn
    for i in image_groups:
       csv_top.append((i,len(image_groups[i])))
    #sort the above array by ranking of number of paintings
    csv_top = sorted(csv_top,key=lambda l:l[1], reverse=True)

    #define csv_top as list of top x artists
    csv_top = csv_top[:x]
    #determine the number of paintings of the painter with least amount of paintings in this top list
    paintings_per_artist = (csv_top[x-1:x][0][1])

    #create a new dictionary of top painters with same number of paitings (paintings_per_artist) for all artists
    top_image_groups = {}
    for i in csv_top:
        for k,v in image_groups.items():
            if i[0] == k:

                top_image_groups[k] = v
    return top_image_groups

get_top(2)

