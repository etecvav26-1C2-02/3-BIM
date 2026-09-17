#include <Servo.h>

//declarando potenciometros
const int port1 = A0;
const int port2 = A1;
const int port3 = A3;
const int port4 = A4;


  
Servo Servo1;
Servo Servo2;
Servo Servo3;
Servo Servo4;

void setup()
{
  Servo1.attach(2);
  Servo2.attach(3);
  Servo3.attach(5);
  Servo4.attach(4);
}

void loop()
{
  
  int leitura1;
  int leitura2;
  int leitura3;
  int leitura4;

  int angulo1;
  int angulo2;                  
  int angulo3;
  int angulo4;
  
  
  leitura1 = analogRead(port1);
  leitura2 = analogRead(port2);
  leitura3 = analogRead(port3);
  leitura4 = analogRead(port4);



  angulo1 = map(leitura1, 0, 1023, 0, 180);
  angulo2 = map(leitura2, 0, 1023, 0, 180);
  angulo3 = map(leitura3, 0, 1023, 0, 180);
  angulo4 = map(leitura4, 0, 1023, 0, 180);


  Servo1.write(angulo1);
  Servo2.write(angulo2);
  Servo3.write(angulo3);
  Servo4.write(angulo4);       
  
  delay(15);
}
