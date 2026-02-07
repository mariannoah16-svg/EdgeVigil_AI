void setup() {
  Serial.begin(115200);
  Serial.println("EdgeVigil Sentry Node Initialized.");
}

void loop() {
  // Simulating the "Sentry" layer from the architecture diagram
  float vibration = random(40, 60) / 100.0;
  float current = random(115, 125) / 10.0;

  Serial.print("DATA,");
  Serial.print(vibration);
  Serial.print(",");
  Serial.println(current);

  delay(1000);
}
