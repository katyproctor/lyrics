#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:51:11 2018

@author: katyproctor
"""

# import libraries
import requests
import bs4

# specify the artist url
quote_page = "https://www.azlyrics.com/b/beatles.html"
page = requests.get(quote_page)

content = page.content

soup = bs4.BeautifulSoup(content, "html.parser")

# get list of all songs by artist
url_list = []

for link in soup.find_all('a'):
    temp = link.get('href')
    
    # only keep urls with lyrics
    if temp and temp[0:9] == "../lyrics":
        temp = temp.replace('..',
                            'https://www.azlyrics.com')
        url_list.append(temp)
        
print(url_list)  

# scrape lyrics for each song and save
for song in url_list:
    temp_song = requests.get(song)
     
    # parse html
    song_content = temp_song.content
    soup = bs4.BeautifulSoup(song_content, "html.parser")
    
    # extract lyrics only
    for link in soup.fin_all('div'):
        temp = link.get() # need to work out a way to do this efficiently
     
     
           
        