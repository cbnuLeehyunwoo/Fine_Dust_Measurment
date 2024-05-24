#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

float minValue = 1000000; // 초기 최솟값을 인식하기 위해 큰 값으로 초기화.
float macValue = 0;
float average_V = 0;
int readCount = 0;
float sumV = 0;


void setup() {
  pinMode(PIN_DUST_LED, OUTPUT);
  digitalWrite(PIN_DUST_LED, HIGH);  // 미세먼지 센서 적외선 LED 초기값 설정(HIGH -> 센서 끔)
  Serial.begin(9600); // 시리얼 통신 시작, 통신속도 9600으로 설정
}

float read_dust() {
  digitalWrite(PIN_DUST_LED, LOW); // LOW-> 센서 킴, 데이터 샘플링 시작
  delayMicroseconds(280);   // 0.28ms 동안 데이터 수집
  int dust_analog = analogRead(PIN_DUST_OUT);
  float dustV = dust_analog * (5.0 / 1023.0); // 아날로그 값을 본래 전압 값으로 변환
  float defaultV = 0.3; // 미세먼지 기본 전압값 측정 필요, 현재는 명시된 초기값의 평균으로 설정
  delayMicroseconds(40); // 0.32의 펄스를 유지해야해서 0.04 ms동안 대기
  digitalWrite(PIN_DUST_LED, HIGH); // 데이터 샘플링 종료, 센서 끔
  delayMicroseconds(9680); // 센서 안정화
  float dustval = (dustV - defaultV)/0.005; // 미세먼지 변수 기본값 측정 필요(기본 전압 일단 0.3으로 해둠)
  return dustV;
}

void updateStatics(float dust V) {
  if(dustV < minValue) minValue = dustV;
  if(dustV < maxValue) minValue = dustV;

  sumValue += dustV;
  readCount++;
  averageV = sumV / readCount;
}

void print_Serial() {
  float dust_ug = read_dust();                  // 미세먼지 데이터 수집
  Serial.print(" 초기 전압 측정: ");
  Serial.print(dust_ug);
  Serial.println(" V");
}   

void loop() {
  print_Serial();
  delay(3000);
}

