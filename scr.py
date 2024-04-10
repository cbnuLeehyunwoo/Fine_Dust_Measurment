import requests
from bs4 import BeautifulSoup

def scrape_naver():
    print("[네이버 미세먼지 지수]")
    url="https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&tqi=imv3ysqpsECss5%2FFWQdssssstjs-136535"
    res=requests.get(url)
    res.raise_for_status() # 문제 발견 시 프로그램 종료

    soup=BeautifulSoup(res.text, "lxml") # html 문서를 lxml을 통해서 BeautifulSoup 객체로 만들어준다.

    dust=soup.find("div", attrs={"class":"tb_scroll"}).find("tbody").find("tr") # 도 별 정보
    place=dust.find("th") # 도 이름
    value=dust.find("span") # 미세먼지 값

    print(dust.get_text())
    print(place.get_text())
    print(value.get_text())

def scrape_naver_gang():
    print("[네이버 강원도 미세먼지 지수]")
    url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blQ3&qvt=0&query=%EA%B0%95%EC%9B%90%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")  

    dust=soup.find("div", attrs={"class":"map_area ct01"})
    place=dust.find("span", attrs={"class":"cityname"})
    value=dust.find("span", attrs={"class":"value"}).find("em")
    print(place.get_text()) # 시 이름
    print(value.get_text()) # 미세먼지 값


if __name__ == "__main__":
    scrape_naver_gang()
