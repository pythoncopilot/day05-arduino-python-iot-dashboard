int lightPin = A0;
int fanPin = A1;
int acPin = A2;

void setup() {
  Serial.begin(9600);
}

void loop() {

  int light = map(analogRead(lightPin), 0, 1023, 0, 100);
  int fan   = map(analogRead(fanPin), 0, 1023, 0, 100);
  int ac    = map(analogRead(acPin), 0, 1023, 0, 100);

  Serial.print("LIGHT:");
  Serial.print(light);
  Serial.print(",FAN:");
  Serial.print(fan);
  Serial.print(",AC:");
  Serial.println(ac);

  delay(1000);
}
