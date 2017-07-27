#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:51:33 2017

@author: Vishesh
"""



import urllib.request
from bs4 import BeautifulSoup
#from PIL import Image
#import requests

#import pandas as pd
#df = pd.read_csv("photoAssets.csv")
#df = df[['id_category', 'name', 'link_rewrite', 'URLs']]
#df = df.dropna()



url = "https://www.check24.de/einsurance/pkw/vnt2/vehicle.form;jsessionid=DF4DEEEA3FAE90AE8922D6A79684035C.ajp13-01-41"

dep = urllib.request.urlopen(url)
soup = BeautifulSoup(dep, 'html.parser')
print(soup.body.div)
print(soup.find('h2', class_="box24Headline"))

soup.find('body').find('div', id="c24-page-and-ads").find('div', id="c24-page-container-content").find('div').find('div').find('div').find('div').find('div', class_="div24Main clearfix").find('div').find('div', class_="div24Right")["class"]

#Find first tip text
newdiv = (soup.find("div", {"class": "box24Col2"}).div)#["class"]
print(newdiv.h3.text)





#Find all tip text
newdiv1 = (soup.find_all("div", {"class": "box24Col2"}))
print(newdiv1)
print(newdiv1[2].div.find_all('h3')[1].text)
newdiv1


for i in range(4):
    for h in range(3):
        try:
            print("Heading: "+newdiv1[i].div.find_all('h3')[h].text)
            print("Text: "+newdiv1[i].div.find_all('p')[h].text)
        except:
            continue
