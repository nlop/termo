// BaudRate = 9600 , Timeout = 1000ms (def)

int PINS_IN[8] = {9,8,7,6,5,4,3,2}; //LSB = 2 , MSB = 9
  
void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 8 ; i++){
    pinMode(PINS_IN[i],INPUT);  
  }
  Serial.begin(9600);
}

void loop() {
  byte dbyte = 0x00;
  for(int i = 0; i < 8 ; i++){
    /*char cbit = digitalRead(PINS_IN[i]) ? '1' : '0';
    Serial.write(cbit);*/
    if(digitalRead(PINS_IN[i])){
      bitSet(dbyte, 7 - i);
    }
  }
  Serial.write(dbyte);
  //Serial.print(dbyte);
  Serial.println();
  delay(100);
}
