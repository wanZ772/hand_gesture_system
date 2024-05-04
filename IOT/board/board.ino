#define LED 13
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  digitalWrite(LED, 0);

}

void loop() {
  // put your main code here, to run repeatedly:

  while (Serial.available() > 0)  {
    String speed = Serial.readStringUntil('\n');
    // Serial.print("");
    Serial.println(speed);
    if (speed == "on")  {
        digitalWrite(LED, 1);
    } else if (speed == "off"){
      digitalWrite(LED, 0);
    }
  }

}
