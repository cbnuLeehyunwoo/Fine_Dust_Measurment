import scr
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def first():
    p1 = f"img/scraping.png"
    p2 = f"img/arduinoValue.jpg"
    p3 = f"img/howact.png"
    p4 = f"img/Cheongju.png"
    return render_template('site.html', p1=p1, p2=p2, p3=p3, p4=p4)

@app.route("/Cheongju")
def cheongju():
    n=scr.scrape_naver("청주")
    w=scr.scrape_weatheri("청주")
    h=scr.scrape_health("청주")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Cheongju.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Yeongdong")
def yeongdong():
    n=scr.scrape_naver("영동")
    w=scr.scrape_weatheri("영동")
    h=scr.scrape_health("영동")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Yeongdong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Okcheon")
def okcheon():
    n=scr.scrape_naver("옥천")
    w=scr.scrape_weatheri("옥천")
    h=scr.scrape_health("옥천")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Okcheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Boeun")
def boeun():
    n=scr.scrape_naver("보은")
    w=scr.scrape_weatheri("보은")
    h=scr.scrape_health("보은")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Boeun.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Goesan")
def goesan():
    n=scr.scrape_naver("괴산")
    w=scr.scrape_weatheri("괴산")
    h=scr.scrape_health("괴산")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Goesan.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Jincheon")
def jincheon():
    n=scr.scrape_naver("진천")
    w=scr.scrape_weatheri("진천")
    h=scr.scrape_health("진천")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Jincheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Eumseong")
def eumseong():
    n=scr.scrape_naver("음성")
    w=scr.scrape_weatheri("음성")
    h=scr.scrape_health("음성")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Eumseong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Chungju")
def chungju():
    n=scr.scrape_naver("충주")
    w=scr.scrape_weatheri("충주")
    h=scr.scrape_health("충주")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Chungju.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Jecheon")
def jecheon():
    n=scr.scrape_naver("제천")
    w=scr.scrape_weatheri("제천")
    h=scr.scrape_health("제천")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Jecheon.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Danyang")
def danyang():
    n=scr.scrape_naver("단양")
    w=scr.scrape_weatheri("단양")
    h=scr.scrape_health("단양")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Danyang.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Jeungpyeong")
def jeungpyeong():
    n=scr.scrape_naver("증평")
    w=scr.scrape_weatheri("증평")
    h=scr.scrape_health("증평")
    nn=scr.state(n)
    ww=scr.state(w)
    hh=scr.state(h)
    s=scr.suggest(n,w,h)
    return render_template('Jeungpyeong.html', n=n, w=w, h=h, nn=nn, ww=ww, hh=hh, ard=scr.arduino_data, s=s, av=(n+w+h)/3)

@app.route("/Manual")
def manual():
    p1 = f"img/circuit.png"
    return render_template('manual.html', p1=p1)

app.run(debug=False)  #디버그 모드 임시 비활성화