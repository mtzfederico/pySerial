String incomingData = "";
#define redLedPin 5
#define greenLedPin 6
#define blueLedPin 9
void setup() {
Serial.begin(115200); // set the baud rate
pinMode(redLedPin, OUTPUT);
pinMode(greenLedPin, OUTPUT);
pinMode(blueLedPin, OUTPUT);
digitalWrite(redLedPin, HIGH);
digitalWrite(greenLedPin, HIGH);
digitalWrite(blueLedPin, HIGH);
Serial.println("Ready"); // print "Ready" once
}

void loop() {
incomingData = Serial.readString(); // read the incoming data
if (incomingData == "Ready"){
  Serial.println("Mega fucking ready"); 
}
if (incomingData == "red"){
  digitalWrite(redLedPin, LOW);
  digitalWrite(greenLedPin, HIGH);
  digitalWrite(blueLedPin, HIGH);
  Serial.println("red led on");
}
if (incomingData == "green"){
  digitalWrite(redLedPin, HIGH);
  digitalWrite(greenLedPin, LOW);
  digitalWrite(blueLedPin, HIGH);
  Serial.println("green led on");
}
if (incomingData == "blue"){
  digitalWrite(redLedPin, HIGH);
  digitalWrite(greenLedPin, HIGH);
  digitalWrite(blueLedPin, LOW);
  Serial.println("blue led on");
}
if (incomingData == "off"){
  digitalWrite(redLedPin, HIGH);
  digitalWrite(greenLedPin, HIGH);
  digitalWrite(blueLedPin, HIGH);
  Serial.println("led off");
}
delay(100);
}
