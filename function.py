import requests
import re
import random
from bs4 import BeautifulSoup

PTT_url = 'https://www.ptt.cc'
def get_webPage(url):
    res = requests.get(url,cookies = {'over18': '1'})
    return res.text
 
def get_articles(page):
    soup = BeautifulSoup(page,'html.parser')   
    #上一頁連結位置
    prevURL = soup.select('.btn-group-paging a')[1]['href']
    articles = []
    divs = soup.select('.r-ent')
    for article in divs:        
        if article.find('a'):
            href = article.find('a')['href'] #取得文章連結
            articles.append({
                'href':href
            })
    return articles, prevURL
 
def get_url():
    allArticles = []
    currentPage = get_webPage(PTT_url+'/bbs/Pet_Get/index.html')
    randPage = random.randrange(2,11)
    randArticle = random.randrange(1,11)
    for i in range(randPage):
        articles, prevURL = get_articles(currentPage)
        allArticles = articles
        currentPage = get_webPage(PTT_url+prevURL)
    count=0
    for article in allArticles:
        count+=1;
        # 再次進入文章，進行圖片爬取
        if count==randArticle:
            url = PTT_url+article['href']
            newRequest = get_webPage(url)
            soup = BeautifulSoup(newRequest,'html.parser')  
            # 找尋符合的 img 圖片網址
            imgLinks = soup.findAll('a',{'href':re.compile('https:\/\/(imgur|i\.imgur)\.com\/.*.jpg$')})
            # 依照文章標題建立資料夾   
            if len(imgLinks)>0:
                return imgLinks[0]['href']
            else:
                count-=1;
    return 'https://imgur.com/inE9TKd.jpg'