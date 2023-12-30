#define depthA 3
#define depthB 5
#define directionA 6
#define directionB 9
#define mainA 10
#define mainB 11
#define fullzeroout 7
#define fullin 8
#define zeroin 4
int incomingByte;      
void setup() {

  Serial.begin(9600);

  pinMode(depthA, OUTPUT);
  pinMode(depthB,OUTPUT);
  pinMode(directionA,OUTPUT);
  pinMode(directionB,OUTPUT);
  pinMode(mainA,OUTPUT);
  pinMode(mainB,OUTPUT);
  pinMode(fullzeroout,OUTPUT);
  pinMode(fullin,INPUT);
  pinMode(zeroin,INPUT);
}

void loop() {
  Serial.println("test"); 
  delay(10);
  Serial.println("123");
  delay(10);

  if (Serial.available() > 0) {
    

    incomingByte = Serial.read();

  
    if (incomingByte == 'w') {
     Forward();
        }
    if (incomingByte == 's') {
     Backward();
        }
    if (incomingByte == 'a') {
     Left();
        }
    if (incomingByte == 'd') {
     Right();
        }
    if (incomingByte == '8') {
     if (zeroin==LOW){
      Up();
     }
        }
    if (incomingByte == '2') {
     if (fullin==LOW){
      Down();
     }
        }
    
  }
}
void Forward(){
  analogWrite(mainA,255);
  digitalWrite(mainB,LOW);
}
void Backward(){
  digitalWrite(mainA,LOW);
  analogWrite(mainB,255);
}
void Left(){
  analogWrite(directionA,255);
  digitalWrite(directionB,LOW);
}
void Right(){
  digitalWrite(directionA,LOW);
  analogWrite(directionB,HIGH);
}
void Up(){
  analogWrite(depthA,200);
  digitalWrite(depthB,LOW);
}
void Down(){
  digitalWrite(depthA,LOW);
  analogWrite(depthB,200);
}
