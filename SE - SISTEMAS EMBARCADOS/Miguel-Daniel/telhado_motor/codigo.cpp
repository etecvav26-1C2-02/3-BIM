#include <Servo.h>

int ldr = A2;
int tmp = A1;
int servoPin = 3;
int ledVerde = 6;
int ledVermelho = 5;

float tempLimite = 28.0;
int luzLimite = 700;

Servo servo1;

void setup() {
  Serial.begin(9600);
  
  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(servoPin, OUTPUT);
  pinMode(ldr, INPUT);
  
  servo1.attach(servoPin);
  servo1.write(0);
  digitalWrite(ledVermelho, HIGH);
}

void loop() {
  servo1.write(90);
  int valorLDR = analogRead(ldr);
  int valorTMP = analogRead(tmp);
  
  float tensao = valorTMP * (5.0 / 1024.0);
  float temperatura = (tensao - 0.5) * 100.0;

  Serial.print(valorLDR);
  Serial.print(" ");
  Serial.println(temperatura);

  bool fechar = (valorLDR < luzLimite) || (temperatura > tempLimite);


  if (fechar) {
    servo1.write(0);
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, HIGH);
  } else {
    servo1.write(90);
    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledVermelho, LOW); 
  }

  delay(500);
}
