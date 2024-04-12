

void setup() {
  // pinMode 및 Serial 초기화
  Serial.begin(9600);
  pinMode(PIN_DUST_LED, OUTPUT);

  digitalWrite(PIN_DUST_LED, HIGH);  // 미세먼지 센서 적외선 LED 초기값 설정(HIGh -> 센서 끔?)

}

float read_dust() {
  digitalWrite(PIN_DUST_LED, LOW); // (LOW-> 센서 킴?, 데이터 샘플링 시작)
  delayMicroseconds(280);
  int dustval = analogRead(PIN_DUST_OUT);
  delayMicroseconds(40);
  digitalWrite(PIN_DUST_LED, HIGH); // (데이터 샘플링 종료, 센서 끔?)
  delayMicroseconds(9680);
  return dustval
}

void print_Serial_LCD() {
  float dust= read_dust();                  // 미세먼지 데이터 수집
  
  Serial.print(" Dust: ");
  Serial.print(dust);
  Serial.println(" ug");
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.("Dust: ");
  lcd.print(dust);
  lcd.print("ug");

}

void loop() {
  read_dust();
  delay(3000);
}
