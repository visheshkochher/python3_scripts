#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:51:33 2017

@author: Vishesh
"""



import urllib.request
from bs4 import BeautifulSoup
from PIL import Image
import requests

import pandas as pd
df = pd.read_csv("photoAssets.csv")
df = df[['id_category', 'name', 'link_rewrite', 'URLs']]
df = df.dropna()



#url = "http://www.website.co.uk/sofa-throws"

def urlImageCrop(oldname, newname, url):
    try:
        dep = urllib.request.urlopen(url)
        soup = BeautifulSoup(dep, 'html.parser')
        imageLink = soup.find('img', class_="banner-image")    
    
        image_url = imageLink["src"]
    
    
    
        img_data = requests.get(image_url).content
        with open(oldname+"original"+".jpg", 'wb') as handler:
            handler.write(img_data)
    
    
    
        img = Image.open(oldname+"original"+".jpg")
    
    
        half_the_width = img.size[0] / 2
        half_the_height = img.size[1] / 2
        img4 = img.crop(
        (
            half_the_width - 500,
            half_the_height - 75,
            half_the_width + 500,
            half_the_height + 75
        )
        )
        img4.save(oldname+"cropped1"+".jpg")
    
    except:
         print("error")
         pass
         
    
#urlImageCrop("Cashmere for Summer", "luxury-cashmere", "http://www.website.co.uk/luxury-cashmere")

#urlImageCrop(df.iloc[0:1,1].to_string()[5:], df.iloc[0:1,2].to_string()[5:], df.iloc[0:1,3].to_string()[5:])


for i in range(df['URLs'].size-1):
    urlImageCrop(df.iloc[i:i+1,1].to_string()[5:], df.iloc[i:i+1,2].to_string()[5:], df.iloc[i:i+1,3].to_string()[5:])