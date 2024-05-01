#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

#include <LiquidCrystal.h>


#define PIN_LCD_V0 6
#define PIN_LCD_RS 13
#define PIN_LCD_EN 12
#define PIN_LCD_D4 5
#define PIN_LCD_D5 4
#define PIN_LCD_D6 3
#define PIN_LCD_D7 2

#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

#define PIN_LED_R 10 // 아두이노 측정기에 LED 추가
#define PIN_LED_G 9 // 빨강과 초록을 섞어서 농도별 LED 출력 구현 예정
#include <LiquidCrystal.h>
LiquidCrystal lcd(PIN_LCD_RS, PIN_LCD_EN, PIN_LCD_D4, PIN_LCD_D5, PIN_LCD_D6, PIN_LCD_D7);


void setup() {
  // pinMode 및 Serial 초기화
  Serial.begin(9600);
  pinMode(PIN_DUST_LED, OUTPUT);

  digitalWrite(PIN_DUST_LED, HIGH);  // 미세먼지 센서 적외선 LED 초기값 설정(HIGH -> 센서 끔)
 
  analogWrite(PIN_LCD_V0, 100); // LCD 콘트라스트 조절
  analogWrite(PIN_LED_G, 0); // 초록 LED 초기값 : 0
  analogWrite(PIN_LED_R, 0); // 적색 LED 초기값 : 0
  lcd.begin(16, 2);
}

float read_dust() {
  digitalWrite(PIN_DUST_LED, LOW); // LOW-> 센서 킴, 데이터 샘플링 시작
  delayMicroseconds(280);   // 0.28ms 동안 데이터 수집
  int dust_analog = analogRead(PIN_DUST_OUT);
  float defautV = 0.3;
  delayMicroseconds(40); // 0.32의 펄스를 유지해야해서 0.04 ms동안 대기
  digitalWrite(PIN_DUST_LED, HIGH); // 데이터 샘플링 종료, 센서 끔
  delayMicroseconds(9680); // 센서 안정화
  float dustval = (dust_analog - defautV)/0.005; // 미세먼지 변수 기본값 측정 필요(기본 전압 일단 0.3으로 해둠)
  return dustval;
}

void print_Serial_LCD() {
  float dust = read_dust();                  // 미세먼지 데이터 수집
  
  Serial.print(" Dust: ");
  Serial.print(dust);
  Serial.println(" ug");       

  lcd.clear();  
  lcd.setCursor(0, 0);
  lcd.print("Dust: ");
  lcd.print(dust);
  lcd.print("ug");

  // if(dust < ??) {                 // 추후에 기준을 정확히 잡으면 추가
  //   analogWrite(PIN_LED_G, 20);
  //   analogWrite(PIN_LED_R, 0);
  // }
  // else if(dust < ??){
  //   analogWrite(PIN_LED_G, 30);
  //   analogWrite(PIN_LED_R, 10)
  // }
  // else{
  //   analogWrite(PIN_LED_G, 0);
  //   analogWrite(PIN_LED_R, 20);
  // }

}

void loop() {
  print_Serial_LCD();
  delay(3000);
}
