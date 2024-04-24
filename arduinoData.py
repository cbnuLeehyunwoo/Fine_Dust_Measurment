import serial
import time

# 시리얼 포트 연결
PORT = 'COM3'
BaudRate = 9600
ser = serial.Serial('PORT', BaudRate)  # 포트번호 확인 완료, 추후에 다른 컴퓨터에서 동작 시 재확인 필요

while True:
    # 아두이노에서 시리얼 통신을 통해 보내는 데이터 읽기
    if ser.in_waiting:
        data = ser.readline().decode('utf-8').strip()
        print("미세먼지 농도:", data) # 추후 출력을 다른 파일로 변경 필요   
    time.sleep(1)
    
