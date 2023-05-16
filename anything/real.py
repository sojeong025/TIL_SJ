import requests
from bs4 import BeautifulSoup

def crawl_cine21_news(page_limit):
    base_url = "http://www.cine21.com/news/issue/list/"
    
    for page in range(1, page_limit + 1):
        url = base_url + f"?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        news_list = soup.select("#content > div > ul > li")
        
        for index, news in enumerate(news_list, start=1):
            # 5번째 게시글은 기사가 아니므로 제외
            if index == 5:
                continue
            
            title = news.select_one("a > span.tit").text.strip()
            thumbnail = news.select_one("a > span.thumb > img")["src"]
            
            print(f"제목: {title}")
            print(f"썸네일 이미지 URL: {thumbnail}")
            print("=" * 50)

# 크롤링 실행 (50페이지까지 크롤링)
crawl_cine21_news(page_limit=50)
