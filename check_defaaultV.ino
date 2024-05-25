#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

// 미세먼지 값의 최솟값, 최댓값, 평균값을 저장할 변수들 선언
float minValue = 1000000; // 충분히 큰 값으로 초기화
float maxValue = 0; // 0으로 초기화
float averageValue = 0; // 평균값 초기화
int readCount = 0; // 읽은 횟수 초기화
float sumValue = 0; // 총 합 초기화
int under_06 = 0;
int under_05 = 0;
int under_04 = 0;
int under_03 = 0;
void setup() {
  pinMode(PIN_DUST_LED, OUTPUT);
  digitalWrite(PIN_DUST_LED, HIGH);  // 미세먼지 센서 적외선 LED 초기값 설정(HIGH -> 센서 끔)
  Serial.begin(9600); // 시리얼 통신 시작, 바우드레이트 9600으로 설정
}

float read_dust() {
  digitalWrite(PIN_DUST_LED, LOW); // LOW-> 센서 킴, 데이터 샘플링 시작
  delayMicroseconds(280); // 0.28ms 동안 데이터 수집
  int dust_analog = analogRead(PIN_DUST_OUT);
  float dustV = dust_analog * (5.0 / 1023.0); // 아날로그 값을 본래 전압 값으로 변환
  digitalWrite(PIN_DUST_LED, HIGH); // 데이터 샘플링 종료, 센서 끔
  delayMicroseconds(9680); // 센서 안정화
  return dustV;
}

void updateStatistics(float dustV) {
  // 최솟값, 최댓값 업데이트
  if(dustV < minValue) minValue = dustV;
  if(dustV > maxValue) maxValue = dustV;
  if(dustV < 0.3){
    under_03++;
  }
  if(dustV < 0.4){
    under_04++;
  } 
  if(dustV < 0.5){
    under_05++;
  }
  if(dustV < 0.6){
    under_06++;
  }
  // 평균값 업데이트
  sumValue += dustV;
  averageValue = sumValue / (readCount - 1);
}

void printStatistics() {
  
  Serial.print("0.3 이하의 값 출현 횟수:  ");
  Serial.print(under_03);
  Serial.println(" 회");
  
  Serial.print("0.4 이하의 값 출현 횟수:  ");
  Serial.print(under_04);
  Serial.println(" 회");
  
  Serial.print("0.5 이하의 값 출현 횟수:  ");
  Serial.print(under_05);
  Serial.println(" 회");

  Serial.print("0.6 이하의 값 출현 횟수:  ");
  Serial.print(under_06);
  Serial.println(" 회");
  
  Serial.print("최소 전압: ");
  Serial.print(minValue);
  Serial.println(" V");
  
  Serial.print("최대 전압: ");
  Serial.print(maxValue);
  Serial.println(" V");
  
  Serial.print("평균 전압: ");
  Serial.print(averageValue);
  Serial.println(" V");

  Serial.print("측정 횟수: ");
  Serial.print(readCount-1);
  Serial.println(" 회");
  
}

void loop() {
  readCount++;
  float dustV = read_dust();
  if(readCount > 1){
    updateStatistics(dustV); // 통계 업데이트
    Serial.println();
    Serial.print("현재 전압: ");
    Serial.print(dustV);
    Serial.println(" V");

    printStatistics(); // 통계 출력
    delay(3000); // 3초 대기
  }
  delay(1000); // 1초 대기
}

