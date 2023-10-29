const int ledPin = 13;
int incomingByte;      
void setup() {

  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
}

void loop() {
  Serial.println("test"); 
  delay(10);
  Serial.println("123");
  delay(10);

  if (Serial.available() > 0) {
    

    incomingByte = Serial.read();

  
    if (incomingByte == 'h') {
      digitalWrite(ledPin, HIGH);
      delay(4);
      digitalWrite(ledPin,LOW);
      
        }
   
    if (incomingByte == 'l') {
      digitalWrite(ledPin, LOW);
     
    }
  }
}