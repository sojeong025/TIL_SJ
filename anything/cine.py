import requests
from bs4 import BeautifulSoup

# url = requests.get("http://www.cine21.com/news/issue/list/")

# data1=soup.select('#content > .news_area > .news > li > a > span.tit')
# data2=soup.select('#content > .news_area > .news > li > a > span.thumb > img')
# data=soup.select('#content > div > ul > li:nth-child(1) > a > span.tit')

# for item in data2:
    # print(item['src'])

url2= requests.get("http://www.cine21.com/news/issue/view/?mag_id=2393")
soup = BeautifulSoup(url2.content, 'html.parser')

data3 = soup.find_all('#content > div > div.culm2_1 > div.article' )

print(data3)

#content > div > div.culm2_l > div.article