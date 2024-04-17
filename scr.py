import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

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
    print("[네이버 충청북도 미세먼지 지수]")
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
    print("미세먼지 :", value[x].get_text()) # 미세먼지 값
    if int(value[x].get_text()) <= 30:
        print("좋음")
    elif int(value[x].get_text()) <= 80:
        print("보통")
    elif int(value[x].get_text()) <= 150:
        print("나쁨")
    elif int(value[x].get_text()) >= 151:
        print("매우나쁨")

def scrape_naver_25():
    print("[네이버 충청북도 초미세먼지 지수]")
    url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%B6%A9%EB%B6%81%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")

    dust=soup.find("div", attrs={"class":"map_area ct16"})
    place=dust.find_all("span", attrs={"class":"cityname"})
    value=dust.find_all("span", attrs={"class":"value"})

    x=0
    search=input("도시 이름 : ") # 도시 찾기
    for i in range(0, len(place)):
        if search in place[i]:
            x=i

    print(place[x].get_text()) # 도시 이름
    print("초미세먼지 :", value[x].get_text()) # 초미세먼지 값
    if int(value[x].get_text()) <= 15:
        state = "좋음"
    elif int(value[x].get_text()) <= 35:
        state = "보통"
    elif int(value[x].get_text()) <= 75:
        state = "나쁨"
    elif int(value[x].get_text()) >= 76:
        state = "매우나쁨"

    message = [
        place[x].get_text(),
        value[x].get_text(),
        state
    ]
    return '<br>'.join(message)


def weatheri(n):
    url="https://www.weatheri.co.kr/special/special05_1.php?a=6"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.content.decode('utf-8','replace'), "lxml") # 글자 깨짐 해결

    dust=soup.find("table", attrs={"width":"100%", "border":"0", "cellpadding":"1", "cellspacing":"1", "bgcolor":"#D2D4D4"}).find_all("tr", attrs={"valign":"top", "bgcolor":"#FFFFFF", "height":"19"})

    place=dust[n].find("td", attrs={"align":"center"}).get_text() #도시 이름
    value=dust[n].find_all("td", attrs={"width":"7%", "align":"right"})[0].get_text() #미세먼지 값
    value2=dust[n].find_all("td", attrs={"width":"7%", "align":"right"})[1].get_text() #초미세먼지 값
    print(place)
    print("미세먼지 :", value)
    if int(value) <= 30:
        print("좋음")
    elif int(value) <= 80:
        print("보통")
    elif int(value) <= 150:
            print("나쁨")
    elif int(value) >= 151:
        print("매우나쁨")
    if "-" not in value2:
        print("초미세먼지 :", value2)
        if int(value2) <= 15:
            print("좋음")
        elif int(value2) <= 35:
            print("보통")
        elif int(value2) <= 75:
            print("나쁨")
        elif int(value2) >= 76:
            print("매우나쁨")

def scrape_weatheri_chungbuk():
    search=input("도시 이름 : ")
    if "청주" in search:
        weatheri(1)
        weatheri(11)
        weatheri(12)
        weatheri(13)
        weatheri(14)
        weatheri(19)
        weatheri(20)
        weatheri(22)
        weatheri(23)
    elif "괴산" in search:
        weatheri(2)
        weatheri(3)
        weatheri(29)
    elif "음성" in search:
        weatheri(4)
        weatheri(16)
        weatheri(24)
    elif "단양" in search:
        weatheri(5)
        weatheri(6)
        weatheri(9)
    elif "진천" in search:
        weatheri(7)
        weatheri(28)
    elif "증평" in search:
        weatheri(8)
        weatheri(27)
    elif "보은" in search:
        weatheri(10)
    elif "충주" in search:
        weatheri(15)
        weatheri(16)
        weatheri(31)
        weatheri(32)
    elif "영동" in search:
        weatheri(17)
        weatheri(33)
    elif "화성" in search:
        weatheri(18)
    elif "옥천" in search:
        weatheri(21)
    elif "제천" in search:
        weatheri(25)
        weatheri(30)
    elif "진천" in search:
        weatheri(28)


def scrape_health():
    print("[충청북도 보건소 미세먼지 지수]")
    url="https://www.chungbuk.go.kr/here/srmmr/list.do?key=1858"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")  

    dust=soup.find("table", attrs={"class":"table tr_over"}).find_all("tr")
    
    search=input("도시 이름 : ")
    count=0
    for n in range(1, len(dust)): #1부터 시작
        place=dust[n].find("td", attrs={"class":"bd_left"}).get_text() #도시 이름
        
        if search in place:
            value=dust[n].find_all("td")[2].get_text().strip().replace(".0㎍/㎥", "") #미세먼지 값
            value2=dust[n].find_all("td")[3].get_text().strip().replace(".0㎍/㎥", "") #초미세먼지
            if count > 0:
                value=dust[n].find_all("td")[1].get_text().strip().replace(".0㎍/㎥", "") #미세먼지 값
                value2=dust[n].find_all("td")[2].get_text().strip().replace(".0㎍/㎥", "") #초미세먼지
            print(place)
            
            if int(value) <= 30:
                print("미세먼지 :", value, " - ", "좋음")
            elif int(value) <= 80:
                print("미세먼지 :", value, " - ", "보통")
            elif int(value) <= 150:
                print("미세먼지 :", value, " - ", "나쁨")
            elif int(value) >= 151:
                print("미세먼지 :", value, " - ", "매우나쁨")
            
            if int(value2) <= 15:
                print("초미세먼지 :", value2, " - ", "좋음")
            elif int(value2) <= 35:
                print("초미세먼지 :", value2, " - ", "보통")
            elif int(value2) <= 75:
                print("초미세먼지 :", value2, " - ", "나쁨")
            elif int(value2) >= 76:
                print("초미세먼지 :", value2, " - ", "매우나쁨")
            count+=1

if __name__ == "__main__":
    #scrape_naver_chungbuk()
    #scrape_naver_25()
    #scrape_weatheri_chungbuk()
    #scrape_health()

    app = Flask(__name__)

    @app.route('/')
    def index():
        result=scrape_naver_25()
        return render_template('mygoogle.html', result=result)

    if __name__ == '__main__':
        app.run(debug=True)
