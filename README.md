# Fine_Dust_Measurement
---
충북대학교 오픈소스기초프로젝트 스리라차 소스🔥팀에서 진행하는 프로젝트
충청북도 미세먼지 데이터 웹 스크래핑 및 아두이노 측정값, 그에 맞는 행동요령을 제공하는 사이트를 제작하였습니다.


## 💻 프로젝트 소개
미세먼지는 WHO에서 1급 발암물질로 지정된 물질이다. 우리는 미세먼지 농도를 알아보기 위해 검색을 해본다. 미세먼지 농도를 제공해주는 사이트는 많다. 사이트마다 그 값은 조금씩 다르고 농도가 나쁠수록 그 편차는 커진다.
### 이 사이트에서는
- 미세먼지 농도값을 제공하는 여러 사이트들의 값을 한번에 보여준다.
- 아두이노 기기 측정을 통해 가장 유사한 값을 제공하는 사이트를 찾아본다. (선택)
- 미세먼지 농도에 따른 행동요령을 제시한다.


## ⏲ 개발 기간
2024.03.22(금) ~ 2024.06.08(토)


## 🧑‍💻 개발자 소개 
- 이기홍 @gihong-free
- 이현우 @cbnuLeehyunwoo
- 최고원 @choigowon


## 💾 설치 방법
  ### python
  ```
  pip install beautifulsoup4
  pip install lxml
  pip install requests
  pip install flask
  pip install serial (혹은 pip install pyserial)
  ```


## ✏️ 실행 방법
1. scr.py 파일 실행
2. Flask를 통해 만들어진 주소 접속
3. 사이트 실행


## 📁 의존성
```
python - 3.x
beautifulsoup4 - 4.x
Flask - 3.x
lxml - 5.x
pyserial - 3.x
requests - 2.x
```


## 📋 LICENSE
```
MIT License

Copyright (c) 2024 cbnuLeehyunwoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
