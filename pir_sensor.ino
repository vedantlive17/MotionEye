int pirPin = 2;  // Pin where the PIR sensor is connected

void setup() {
  Serial.begin(9600);  // Start Serial Communication
  pinMode(pirPin, INPUT);  // PIR sensor as input
}

void loop() {
  int pirState = digitalRead(pirPin);  // Read PIR state
  if (pirState == HIGH) {
    Serial.println("Motion detected!");  // Send signal to Raspberry Pi
  } else {
    Serial.println("Motion ended!");  // Send signal to Raspberry Pi
  }
  delay(1000);  // Check every second
}
