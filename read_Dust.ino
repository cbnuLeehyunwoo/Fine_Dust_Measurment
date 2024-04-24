
#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

#include <LiquidCrystal.h>
//LiquidCrystal lcd();


void setup() {
#define PIN_LCD_V0 6
#define PIN_LCD_RS 13
#define PIN_LCD_EN 12
#define PIN_LCD_D4 5
#define PIN_LCD_D5 4
#define PIN_LCD_D6 3
#define PIN_LCD_D7 2

#define PIN_DUST_LED 11 // 센서 LED 핀
#define PIN_DUST_OUT A0 // 데이터 출력 핀

#include <LiquidCrystal.h>
LiquidCrystal lcd(PIN_LCD_RS, PIN_LCD_EN, PIN_LCD_D4, PIN_LCD_D5, PIN_LCD_D6, PIN_LCD_D7);


void setup() {
  // pinMode 및 Serial 초기화
  Serial.begin(9600);
  pinMode(PIN_DUST_LED, OUTPUT);

  digitalWrite(PIN_DUST_LED, HIGH);  // 미세먼지 센서 적외선 LED 초기값 설정(HIGH -> 센서 끔?)
 
 
  lcd.begin(16, 2);
}

float read_dust() {
  digitalWrite(PIN_DUST_LED, LOW); // (LOW-> 센서 킴?, 데이터 샘플링 시작)
  delayMicroseconds(280);
  int dustval = analogRead(PIN_DUST_OUT);
  delayMicroseconds(40);
  digitalWrite(PIN_DUST_LED, HIGH); // (데이터 샘플링 종료, 센서 끔?)
  delayMicroseconds(9680);
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

}

void loop() {
  print_Serial_LCD();
  delay(3000);
}
