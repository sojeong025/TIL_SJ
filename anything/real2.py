import requests
from bs4 import BeautifulSoup

def crawl_cine21_news(page_limit):
    base_url = "http://www.cine21.com/news/issue/view/?mag_id="
    
    start_id = 2400
    end_id = 2400 - page_limit
    
    for mag_id in range(start_id, end_id, -1):
        url = base_url + str(mag_id)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        article_content = soup.select_one("#news_content")
        
        # 기사 내용 출력 또는 필요한 정보 추출
        print("기사 내용:")
        print(article_content.text.strip())
        print("=" * 50)

# 크롤링 실행 (3개의 상세 페이지 크롤링)
crawl_cine21_news(page_limit=3)
