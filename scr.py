import requests
from bs4 import BeautifulSoup

def scrape_dust():
    print("[네이버 미세먼지 지수]")
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=imv3ysqpsECss5%2FFWQdssssstjs-136535"
    res=requests.get(url)
    res.raise_for_status() # 문제 발견 시 프로그램 종료

    soup=BeautifulSoup(res.text, "lxml") # html 문서를 lxml을 통해서 BeautifulSoup 객체로 만들어준다.

    dust=soup.find("div", attrs={"class":"tb_scroll"}).find("tbody")

    print(dust.get_text())


if __name__ == "__main__":
    scrape_dust()
