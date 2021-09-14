from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from webdriver_manager.chrome import ChromeDriverManager

Result_Dict = {}
def scrape():
    
    executable_path= {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome',**executable_path,headless=True)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html=browser.html
    result = BeautifulSoup(html,'html.parser')
#*************************************************************
# Identify and return title of listing
    news_title = result.body.find('div', class_='content_title').text.strip()
# Identify and return price of listing
    news_p = result.body.find('div', class_='article_teaser_body').text.strip()

#**************Featured_image_URL*******************
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    html=browser.html
    result = BeautifulSoup(html,'html.parser')

    list=[]
    for link in result.findAll('img'):
        x = link.get('src')
        list.append(x)

    
    featured_image_url = url + list[1]
    

#****************MARS FACTS*******************
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    df = tables[0]
    df.columns =['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    html_table = df.to_html()
    html_table = html_table.replace('\n', '')
    df_to_html= df.to_html().replace('class="dataframe"', 'class="dataframe table-striped table-bordered table-sm"')
    
    

#**********************Mars Hemispheres*****************

    url= 'https://marshemispheres.com/'
    url1 = 'https://marshemispheres.com/cerberus.html'
    url2 = 'https://marshemispheres.com/schiaparelli.html'
    url3 = 'https://marshemispheres.com/syrtis.html'
    url4 = 'https://marshemispheres.com/valles.html'
    hemisphere_image_urls =[]
    url_list = [url1,url2,url3,url4]

    for i in url_list:
        browser.visit(i)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        title = soup.body.find('h2', class_='title').text.strip()
        img_url = soup.body.find('img', class_='wide-image').get('src')
        img_url = url + img_url
        post = {
            'title': title,
            'img_url': img_url,
        }
        hemisphere_image_urls.append(post)
    

#********************Result Dictionary*********************************
    Result_Dict = {
        'news_title':news_title,
        'news_p': news_p,
        'featured_image_url':featured_image_url,
        'html_table':df_to_html,
        'hemisphere_image_urls':hemisphere_image_urls,
        }

   
    return Result_Dict

#********************************************************************************







