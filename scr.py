import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import serial

PORT = 'COM3'
BaudRate = 9600
ser = serial.Serial(PORT, BaudRate)  # 포트번호 확인 완료, 추후에 다른 컴퓨터에서 동작 시 재확인 필요
# def scrape_naver_25(): # 네이버 초미세먼지
#     url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%B6%A9%EB%B6%81%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
#     res=requests.get(url)
#     res.raise_for_status()
#     soup=BeautifulSoup(res.text, "lxml")

#     dust=soup.find("div", attrs={"class":"map_area ct16"})
#     place=dust.find_all("span", attrs={"class":"cityname"})
#     value=dust.find_all("span", attrs={"class":"value"})

#     x=0
#     search=input("도시 이름 : ") # 도시 찾기
#     for i in range(0, len(place)):
#         if search in place[i]:
#             x=i

#     print(place[x].get_text()) # 도시 이름
#     print("초미세먼지 :", value[x].get_text()) # 초미세먼지 값
#     if int(value[x].get_text()) <= 15:
#         state = "좋음"
#     elif int(value[x].get_text()) <= 35:
#         state = "보통"
#     elif int(value[x].get_text()) <= 75:
#         state = "나쁨"
#     elif int(value[x].get_text()) >= 76:
#         state = "매우나쁨"

#     message = [
#         place[x].get_text(),
#         value[x].get_text(),
#         state
#     ]
#     return '<br>'.join(message)

def scrape_naver(location): # 네이버 미세먼지
    url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blQ3&qvt=0&query=%EC%B6%A9%EB%B6%81%20%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
    # 스크랩 해올 주소
    res=requests.get(url) # 주소를 받아온다
    res.raise_for_status() # 문제 발견 시 프로그램 종료
    soup=BeautifulSoup(res.text, "lxml")  # html 문서(DevTools)를 lxml을 통해서 BeautifulSoup 객체로 만들어준다.

    dust=soup.find("div", attrs={"class":"map_area ct16"}) # 미세먼지 농도
    place=dust.find_all("span", attrs={"class":"cityname"}) # 지역
    value=dust.find_all("span", attrs={"class":"value"}) # 상태

    x=0
    for i in range(0, len(place)): # 해당 도시에 해당하는 값 찾기
        if location in place[i]:
            x=i

    print(place[x].get_text()) # 도시 이름 출력
    print("미세먼지 :", value[x].get_text()) # 미세먼지 농도 출력
    if int(value[x].get_text()) <= 30: # 상태 출력
        state = "좋음"
    elif int(value[x].get_text()) <= 80:
        state = "보통"
    elif int(value[x].get_text()) <= 150:
        state = "나쁨"
    elif int(value[x].get_text()) >= 151:
        state = "매우나쁨"

    message = [ # html로 띄울 값
        place[x].get_text(),
        value[x].get_text(),
        state
    ]
    return message

sum=0 # 웨더아이 미세먼지 값 합계
count=0 # 웨더아이 미세먼지 지역 갯수

def weatheri(n):
    url="https://www.weatheri.co.kr/special/special05_1.php?a=6"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.content.decode('utf-8','replace'), "lxml") # 글자 깨짐 해결

    dust=soup.find("table", attrs={"width":"100%", "border":"0", "cellpadding":"1", "cellspacing":"1", "bgcolor":"#D2D4D4"}).find_all("tr", attrs={"valign":"top", "bgcolor":"#FFFFFF", "height":"19"})
    value=dust[n].find_all("td", attrs={"width":"7%", "align":"right"})[0].get_text()
    global count
    count+=1
    if(value in "-\xa0"): # 미세먼지 값 안뜨는 지역은 제외 처리
        value = 0
        count-=1
    global sum
    sum+=int(value) # 미세먼지 합계

def scrape_weatheri(location):
    value=0
    if "청주" in location:
        weatheri(1)
        weatheri(11)
        weatheri(12)
        weatheri(13)
        weatheri(14)
        weatheri(19)
        weatheri(20)
        weatheri(22)
        weatheri(23)
        value = int(sum/count)
    elif "괴산" in location:
        weatheri(2)
        weatheri(3)
        weatheri(29)
        value = int(sum/count)
    elif "음성" in location:
        weatheri(4)
        weatheri(16)
        weatheri(24)
        value = int(sum/count)
    elif "단양" in location:
        weatheri(5)
        weatheri(6)
        weatheri(9)
        value = int(sum/count)
    elif "진천" in location:
        weatheri(7)
        weatheri(28)
        value = int(sum/count)
    elif "증평" in location:
        weatheri(8)
        weatheri(27)
        value = int(sum/count)
    elif "보은" in location:
        weatheri(10)
        value = sum
    elif "충주" in location:
        weatheri(15)
        weatheri(16)
        weatheri(31)
        weatheri(32)
        value = int(sum/count)
    elif "영동" in location:
        weatheri(17)
        weatheri(33)
        value = int(sum/count)
    elif "화성" in location:
        weatheri(18)
        value = sum
    elif "옥천" in location:
        weatheri(21)
        value = sum
    elif "제천" in location:
        weatheri(25)
        weatheri(30)
        value = int(sum/count)

    state = "좋음"
    if(15<value<30):
        state="보통"
    elif(value<75):
        state="나쁨"
    elif(value>=76):
        state="매우나쁨"

    message = [
        location,
        value,
        state
    ]
    return message


def scrape_health(location): # 충청북도 보건환경연구원
    url="https://www.chungbuk.go.kr/here/srmmr/list.do?key=1858"
    res=requests.get(url)
    res.raise_for_status()
    soup=BeautifulSoup(res.text, "lxml")  

    dust=soup.find("table", attrs={"class":"table tr_over"}).find_all("tr")
    count=0
    result=0
    for n in range(1, len(dust)): #1부터 시작
        place=dust[n].find("td", attrs={"class":"bd_left"}).get_text() #도시 이름
        
        if location in place:
            if count==0:
                value=dust[n].find_all("td")[2].get_text().strip().replace("㎍/㎥ 이하", "") #미세먼지 값
                value=value.replace(".0㎍/㎥", "")
                count+=1
                if(value in "점검중"): # 점검 중인 지역 제외 처리
                    value=0
                    count-=1
                result+=int(value)
                #value2=dust[n].find_all("td")[3].get_text().strip().replace(".0㎍/㎥", "") #초미세먼지
            else:
                value=dust[n].find_all("td")[1].get_text().strip().replace("㎍/㎥ 이하", "") #미세먼지 값
                value=value.replace(".0㎍/㎥", "")
                count+=1
                if(value in "점검중"): #점검 중인 지역 제외 처리
                    value=0
                    count-=1
                result+=int(value)
                #value2=dust[n].find_all("td")[2].get_text().strip().replace(".0㎍/㎥", "") #초미세먼지
            
            if int(value) <= 30:
                state = "좋음"
            elif int(value) <= 80:
                state = "보통"
            elif int(value) <= 150:
                state = "나쁨"
            elif int(value) >= 151:
                state = "매우나쁨"

    message = [
        location,
        int(result/count),
        state
    ]
    return message

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def first():
        photo1 = f"img/Whetheri.jpg"
        photo2 = f"img/NaverWhether.png"
        photo3 = f"img/AirKorea.png"
        return render_template('site2.html', photo1=photo1, photo2=photo2, photo3=photo3)
    
    @app.route("/Cheongju")
    def cheongju():
        result1=scrape_naver("청주")
        result2=scrape_weatheri("청주")
        result3=scrape_health("청주")
        return render_template('Cheongju.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Yeongdong")
    def yeongdong():
        result1=scrape_naver("영동")
        result2=scrape_weatheri("영동")
        result3=scrape_health("영동")
        return render_template('Yeongdong.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Okcheon")
    def okcheon():
        result1=scrape_naver("옥천")
        result2=scrape_weatheri("옥천")
        result3=scrape_health("옥천")
        return render_template('Okcheon.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Boeun")
    def boeun():
        result1=scrape_naver("보은")
        result2=scrape_weatheri("보은")
        result3=scrape_health("보은")
        return render_template('Boeun.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Goesan")
    def goesan():
        result1=scrape_naver("괴산")
        result2=scrape_weatheri("괴산")
        result3=scrape_health("괴산")
        return render_template('Goesan.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Jincheon")
    def jincheon():
        result1=scrape_naver("진천")
        result2=scrape_weatheri("진천")
        result3=scrape_health("진천")
        return render_template('Jincheon.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Eumseong")
    def eumseong():
        result1=scrape_naver("음성")
        result2=scrape_weatheri("음성")
        result3=scrape_health("음성")
        return render_template('Eumseong.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Chungju")
    def chungju():
        result1=scrape_naver("충주")
        result2=scrape_weatheri("충주")
        result3=scrape_health("충주")
        return render_template('Chungju.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Jecheon")
    def jecheon():
        result1=scrape_naver("제천")
        result2=scrape_weatheri("제천")
        result3=scrape_health("제천")
        return render_template('Jecheon.html', result1=result1, result2=result2, result3=result3)
    
    @app.route("/Danyang")
    def danyang():
        result1=scrape_naver("단양")
        result2=scrape_weatheri("단양")
        result3=scrape_health("단양")
        return render_template('Danyang.html', result1=result1, result2=result2, result3=result3)
   
    @app.route("/Jeungpyeong")
    def jeungpyeong():
        result1=scrape_naver("증평")
        result2=scrape_weatheri("증평")
        result3=scrape_health("증평")
        return render_template('Jeungpyeong.html', result1=result1, result2=result2, result3=result3)
    
    if __name__ == '__main__':
        app.run(debug=True)
