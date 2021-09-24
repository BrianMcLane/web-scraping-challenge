from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('div', class_='content_title').text
    article = soup.find('div', class_='article_teaser_body').text
    mars_dict = {'1':{'title': title, "article": article}}

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    

    title2 = soup.find_all('div', class_='floating_text_area')
    # print(title2)
    for news in title2:
        try:
            img_title = news.find('h1', class_='media_feature_title').text
            img_hyper = news.find('a', class_="showimg fancybox-thumbs")
            link = url+news.a['href']
            print(img_title)
            print(link)
        except Exception as e:
            print(e)

    mars_dict['2'] = {'img_title': img_title, "link": link}

    url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url,flavor='html5lib')

    df = tables[0]
    df.columns = df.iloc[0]
    df = df.iloc[1: , :]
    df = df.set_index("Mars - Earth Comparison")
               
    df_json = df.to_html()

    mars_dict['3'] = df_json


    base_url = "https://marshemispheres.com/"

    url = "https://marshemispheres.com/cerberus.html"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img1 = soup.find_all('div', class_='downloads')
    # print(img1)
    for image in img1:
        try:
            cerb_hyper = image.find('li')
            cerb_link = base_url+image.a['href']
            print(cerb_link)
            
        except Exception as e:
            print(e)

    mars_dict['4'] = cerb_link

    url = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img2 = soup.find_all('div', class_='downloads')
    # print(img2)
    for image in img2:
        try:
            schi_hyper = image.find('li')
            schi_link = base_url+image.a['href']
            print(schi_link)
            
        except Exception as e:
            print(e)

    mars_dict['5'] = schi_link

    url = "https://marshemispheres.com/syrtis.html"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img3 = soup.find_all('div', class_='downloads')
    # print(img3)
    for image in img3:
        try:
            syrt_hyper = image.find('li')
            syrt_link = base_url+image.a['href']
            print(syrt_link)
            
        except Exception as e:
            print(e)

    mars_dict['6'] = syrt_link       

    url = "https://marshemispheres.com/valles.html"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img4 = soup.find_all('div', class_='downloads')
    # print(img4)
    for image in img4:
        try:
            vall_hyper = image.find('li')
            vall_link = base_url+image.a['href']
            print(vall_link)
            
        except Exception as e:
            print(e)

    mars_dict['7'] = vall_link

    browser.quit()

    return mars_dict


