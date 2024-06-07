import requests, serial, re, threading
from bs4 import BeautifulSoup

arduino_data = "No data"
def read_arduino():
    global arduino_data
    try:
        PORT = 'COM4'
        BaudRate = 9600
        ser = serial.Serial(PORT, BaudRate)
        while True:
            if ser.in_waiting:
                ard = ser.readline().decode('utf-8').strip()
                numbers = re.findall(r'\d+\.?\d*', ard)
                if numbers:
                    arduino_data = float(numbers[0])
                else:
                    arduino_data = "값에 숫자가 없습니다."
    except serial.SerialException:
        arduino_data = "포트 미연결 상태"
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

    global sum
    global count

    dust=soup.find("table", attrs={"width":"100%", "border":"0", "cellpadding":"1", "cellspacing":"1", "bgcolor":"#D2D4D4"}).find_all("tr", attrs={"valign":"top", "bgcolor":"#FFFFFF", "height":"19"})
    value=dust[n].find_all("td", attrs={"width":"7%", "align":"right"})[0].get_text()
    count+=1
    if(value in "-\xa0"): # 미세먼지 값 안뜨는 지역은 제외 처리
        value = 0
        count-=1
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
    if value <= 30:
        state += "좋음"
    elif value <= 50:
        state += "양호"
    elif value <= 70:
        state += "주의"
    elif value <= 85:
        state += "나쁨"
    elif value <= 100:
        state += "매우나쁨"
    elif value >= 101:
        state += "외출금지"
    return state

def suggest(n,w,h):
    ard=arduino_data
    if(ard=="포트 미연결 상태") or (ard=="No data"):
        return "아두이노 포트 미연결"
    site=""
    min=abs(n-ard)
    if (abs(w-ard)<min):
        min=(w-ard)
    if (abs(h-ard)<min):
        min=(h-ard)

    if(abs(n-ard)==min):
        site+=" 네이버 "
    if (abs(w-ard)==min):
        site += " 웨더아이 "
    if (abs(h-ard)==min):
        site += " 충북보건환경연구원 "
    return site
