import requests, serial, threading, re
from bs4 import BeautifulSoup
from flask import Flask, render_template, g

class Scr:
    arduino_data = "No data"
    def read_arduino():
        #global arduino_data
        try:
            PORT = 'COM3'
            BaudRate = 9600
            ser = serial.Serial(PORT, BaudRate)
            while True:
                if ser.in_waiting:
                    ard = ser.readline().decode('utf-8').strip()
                    numbers = re.findall(r'\d+\.?\d*', ard)
                    if numbers:
                        Scr.arduino_data = float(numbers[0])
                        # print(arduino_data) 아두이노 데이터 정상수신 테스트 코드
                    else:
                        Scr.arduino_data = "값에 숫자가 없습니다."
        except serial.SerialException:
            Scr.arduino_data = "포트 미연결 상태"
    threading.Thread(target=read_arduino, daemon=True).start()

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
        
        return int(value[x].get_text())

    sum=0 # 웨더아이 미세먼지 값 합계
    count=0 # 웨더아이 미세먼지 지역 갯수

    def weatheri(n):
        url="https://www.weatheri.co.kr/special/special05_1.php?a=6"
        res=requests.get(url)
        res.raise_for_status()
        soup=BeautifulSoup(res.content.decode('utf-8','replace'), "lxml") # 글자 깨짐 해결

        dust=soup.find("table", attrs={"width":"100%", "border":"0", "cellpadding":"1", "cellspacing":"1", "bgcolor":"#D2D4D4"}).find_all("tr", attrs={"valign":"top", "bgcolor":"#FFFFFF", "height":"19"})
        value=dust[n].find_all("td", attrs={"width":"7%", "align":"right"})[0].get_text()
        #global count
        Scr.count+=1
        if(value in "-\xa0"): # 미세먼지 값 안뜨는 지역은 제외 처리
            value = 0
            Scr.count-=1
        #global sum
        Scr.sum+=int(value) # 미세먼지 합계

    def scrape_weatheri(location):
        value=0
        if "청주" in location:
            Scr.weatheri(1)
            Scr.weatheri(11)
            Scr.weatheri(12)
            Scr.weatheri(13)
            Scr.weatheri(14)
            Scr.weatheri(19)
            Scr.weatheri(20)
            Scr.weatheri(22)
            Scr.weatheri(23)
            value = int(Scr.sum/Scr.count)
        elif "괴산" in location:
            Scr.weatheri(2)
            Scr.weatheri(3)
            Scr.weatheri(29)
            value = int(Scr.sum/Scr.count)
        elif "음성" in location:
            Scr.weatheri(4)
            Scr.weatheri(16)
            Scr.weatheri(24)
            value = int(Scr.sum/Scr.count)
        elif "단양" in location:
            Scr.weatheri(5)
            Scr.weatheri(6)
            Scr.weatheri(9)
            value = int(Scr.sum/Scr.count)
        elif "진천" in location:
            Scr.weatheri(7)
            Scr.weatheri(28)
            value = int(Scr.sum/Scr.count)
        elif "증평" in location:
            Scr.weatheri(8)
            Scr.weatheri(27)
            value = int(Scr.sum/Scr.count)
        elif "보은" in location:
            Scr.weatheri(10)
            value = Scr.sum
        elif "충주" in location:
            Scr.weatheri(15)
            Scr.weatheri(16)
            Scr.weatheri(31)
            Scr.weatheri(32)
            value = int(Scr.sum/Scr.count)
        elif "영동" in location:
            Scr.weatheri(17)
            Scr.weatheri(33)
            value = int(Scr.sum/Scr.count)
        elif "화성" in location:
            Scr.weatheri(18)
            value = Scr.sum
        elif "옥천" in location:
            Scr.weatheri(21)
            value = Scr.sum
        elif "제천" in location:
            Scr.weatheri(25)
            Scr.weatheri(30)
            value = int(Scr.sum/Scr.count)
            
        return value


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
                else:
                    value=dust[n].find_all("td")[1].get_text().strip().replace("㎍/㎥ 이하", "") #미세먼지 값
                    value=value.replace(".0㎍/㎥", "")
                    count+=1
                    if(value in "점검중"): #점검 중인 지역 제외 처리
                        value=0
                        count-=1
                    result+=int(value)
                
        value=int(result/count)
        
        return value

    def state(value):
        state = "상태 : "
        if int(value) <= 30:
            state += "좋음"
        elif int(value) <= 50:
            state += "양호"
        elif int(value) <= 70:
            state += "주의"
        elif int(value) <= 85:
            state += "나쁨"
        elif int(value) <= 100:
            state += "매우나쁨"
        elif int(value) >= 101:
            state += "외출금지"
        return state

    def suggest(n,w,h):
        ard=Scr.arduino_data
        if(ard=="포트 미연결 상태") or (ard=="No data"):
            return "아두이노 포트 미연결"
        min=n-ard
        site=""
        if (w-ard<min):
            min=w-ard
        if (h-ard<min):
            min=h-ard
        if (n-ard==min):
            site += "네이버 "
        if (w-ard==min):
            site += "웨더아이 "
        if (h-ard==min):
            site += "충북보건환경연구원"
        return site

if __name__ == "__main__":
    app = Flask(__name__)

    @app.route('/')
    def first():
        return render_template('site.html')
    
    @app.route("/Cheongju")
    def cheongju():
        n=Scr.scrape_naver("청주")
        w=Scr.scrape_weatheri("청주")
        h=Scr.scrape_health("청주")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        s=Scr.suggest(n,w,h)
        return render_template('Cheongju.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data, s=s)
    
    @app.route("/Yeongdong")
    def yeongdong():
        n=Scr.scrape_naver("영동")
        w=Scr.scrape_weatheri("영동")
        h=Scr.scrape_health("영동")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Yeongdong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Okcheon")
    def okcheon():
        n=Scr.scrape_naver("옥천")
        w=Scr.scrape_weatheri("옥천")
        h=Scr.scrape_health("옥천")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Okcheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Boeun")
    def boeun():
        n=Scr.scrape_naver("보은")
        w=Scr.scrape_weatheri("보은")
        h=Scr.scrape_health("보은")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Boeun.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Goesan")
    def goesan():
        n=Scr.scrape_naver("괴산")
        w=Scr.scrape_weatheri("괴산")
        h=Scr.scrape_health("괴산")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Goesan.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Jincheon")
    def jincheon():
        n=Scr.scrape_naver("진천")
        w=Scr.scrape_weatheri("진천")
        h=Scr.scrape_health("진천")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Jincheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Eumseong")
    def eumseong():
        n=Scr.scrape_naver("음성")
        w=Scr.scrape_weatheri("음성")
        h=Scr.scrape_health("음성")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Eumseong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Chungju")
    def chungju():
        n=Scr.scrape_naver("충주")
        w=Scr.scrape_weatheri("충주")
        h=Scr.scrape_health("충주")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Chungju.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Jecheon")
    def jecheon():
        n=Scr.scrape_naver("제천")
        w=Scr.scrape_weatheri("제천")
        h=Scr.scrape_health("제천")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Jecheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
    
    @app.route("/Danyang")
    def danyang():
        n=Scr.scrape_naver("단양")
        w=Scr.scrape_weatheri("단양")
        h=Scr.scrape_health("단양")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Danyang.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
   
    @app.route("/Jeungpyeong")
    def jeungpyeong():
        n=Scr.scrape_naver("증평")
        w=Scr.scrape_weatheri("증평")
        h=Scr.scrape_health("증평")
        nn=Scr.state(n)
        ww=Scr.state(w)
        hh=Scr.state(h)
        return render_template('Jeungpyeong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=Scr.arduino_data)
        
    @app.teardown_appcontext             
    def close_connection(exception=None):
         if 'arduino' in g and g.arduino is not None:
           g.arduino.close()
           print("아두이노 포트 닫힘")
    
    if __name__ == '__main__':
        app.run(debug=False)  #디버그 모드 임시 비활성화
