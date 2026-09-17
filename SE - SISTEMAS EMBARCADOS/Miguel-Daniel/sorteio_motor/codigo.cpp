#include <Servo.h>

long readUltrassonicDistance(int triggerPin, int echoPin)
{
     pinMode(triggerPin, OUTPUT); // declara a porta de saída do sinal
     digitalWrite(triggerPin, LOW); // declara a saída como BAIXO
     delayMicroseconds(2); // aguarda 2 microsegundos
     digitalWrite(triggerPin, HIGH); // declara a saída como ALTO
     delayMicroseconds(10); // aguarda 10 microsegundos
     digitalWrite(triggerPin, LOW); // declara a saída como BAIXO
     pinMode(echoPin, INPUT); // declara a porta de entrada do sinal
     return pulseIn(echoPin, HIGH); // verifica se houve entrada de sinal,

}

float centimetro;
int valor;
Servo servo1;

void setup()
{

  randomSeed(analogRead(A1)) ;
  pinMode(2, INPUT_PULLUP);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(1, OUTPUT);
  centimetro = 0.01723 * readUltrassonicDistance(A0, A0) ;
  servo1.attach(12);

}

void sorteio(){
	 valor = random(1,7);
   
     if (valor ==1){
    digitalWrite(8, HIGH);
    }
    
   if (valor == 2){
    digitalWrite(7, HIGH);
    digitalWrite(11, HIGH);
    }
  
   if (valor == 3){
    digitalWrite(7, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(8, HIGH);
   }
  
   if (valor == 4){
    digitalWrite(5, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(9, HIGH);
   }
  
   if (valor == 5){
    digitalWrite(5, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(8, HIGH);
   }
  
   if (valor == 6){
    digitalWrite(10, HIGH);
    digitalWrite(11, HIGH);
    digitalWrite(7, HIGH);
    digitalWrite(9, HIGH);
    digitalWrite(6, HIGH);
    digitalWrite(5, HIGH);
  }
  delay(4000);
   digitalWrite(11, LOW);
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
    digitalWrite(7, LOW);
    digitalWrite(6, LOW);
    digitalWrite(5, LOW);
    
}
void motor(){
  
  servo1.write(90);
  delay(2000);
   servo1.write(0);
  delay(1000);
   
}

void loop() {
  
    centimetro = 0.01723 * readUltrassonicDistance(A0, A0);
  if (centimetro > 0 && centimetro < 40) {
    sorteio();
  if (valor % 2 == 0) {
    motor();

	}
   }
  }
