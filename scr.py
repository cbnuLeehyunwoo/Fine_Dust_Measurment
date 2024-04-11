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

def scrape_naver_chungbuk():
    print("[네이버 충청도 미세먼지 지수]")
    url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blQ3&qvt=0&query=%EC%B6%A9%EB%B6%81%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")  

    dust=soup.find("div", attrs={"class":"map_area ct16"})
    place=dust.find_all("span", attrs={"class":"cityname"})
    value=dust.find_all("span", attrs={"class":"value"}) #.find("em")

    x=0
    search=input("도시 이름 : ") # 도시 찾기
    for i in range(0, len(place)):
        if search in place[i]:
            x=i

    print(place[x].get_text()) # 도시 이름
    print(value[x].get_text()) # 미세먼지 값


if __name__ == "__main__":
    scrape_naver_chungbuk()
