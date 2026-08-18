# Respostas — Conceitos Básicos de Eletricidade, Eletrônica, Sensores e Atuadores
 
---
 
## Questão 1 — O LED acendeu. Está tudo certo?

**Não concordamos com o aluno.**
O fato de o LED ter acendido **não garante** que a ligação esteja correta ou segura.
 
Ligar um LED diretamente ao pino do microcontrolador, sem um **resistor em série** para limitar a corrente, é um erro comum. O LED exige limitação de corrente; sem o resistor, ele tenta puxar mais corrente do que a porta do microcontrolador pode fornecer com segurança. Isso pode **queimar o pino do chip** ou **diminuir drasticamente a vida útil do LED**.

### Lei de Ohm ($V = I \cdot R$)
 
| Grandeza | Descrição |
|---|---|
| **Tensão ($V$)** | Cada LED precisa de uma queda de tensão específica para operar (geralmente entre 1,8V e 3,3V) |
| **Corrente ($I$)** | LEDs operam com correntes baixas (~10mA a 20mA). Pinos de microcontroladores possuem limites estritos de corrente máxima |
| **Resistência ($R$)** | O resistor ajusta essa equação, absorvendo o excesso de tensão e mantendo a corrente dentro dos limites seguros |

---

## Questão 2 — Escolhendo sensores
 
### Análise do problema
 
- *Informação a ser detectada:* presença ou movimentação de pessoas na sala de aula
- *Sensor indicado:* sensor de presença/movimento PIR (Infravermelho Passivo) ou sensor ultrassônico
- *Função do microcontrolador:* ler o sinal do sensor, contabilizar o tempo sem movimento e enviar a ordem de desligar as luzes após um tempo limite (timeout)
- *Atuador:* módulo relé (chaveamento da lâmpada de 110V/220V) ou dimmer digital
### Decisões do programa
 
1. *Se detectar movimento* → mantém a luz ligada e reseta o temporizador
2. *Se parar de detectar movimento* → inicia contagem de tempo (ex: 10 minutos)
3. *Se o tempo limite esgotar* sem novo movimento → desliga o relé (apaga a luz)
### Fluxo da solução
 

ENTRADA (Sensor PIR de Presença)
        ↓
PROCESSAMENTO (Microcontrolador / Lógica de Tempo)
        ↓
SAÍDA (Módulo Relé / Lâmpada)

 
---
## Questão 3 — Sensor ou atuador?
 
### Classificação dos componentes
 
| Categoria | Componentes |
|---|---|
| *Entrada* (Sensores/Controles) | Sensor de temperatura, sensor de luminosidade, botão |
| *Processamento* (Cérebro) | ESP32 |
| *Saída* (Atuadores/Indicadores) | Motor, LED, buzzer |
 
### Por que combinar vários sensores e atuadores?
 
Projetos reais lidam com *múltiplas variáveis do ambiente* e precisam responder de formas diferentes para cada situação.
 
*Exemplo de sistema integrado: Estufa inteligente*
 
- *Sensores (Entrada):*
  - Sensor de temperatura → mede o calor
  - Sensor de luminosidade → mede a luz solar
  - Botão → alterna entre modo manual/automático
- *Atuadores (Saída):*
  - *Motor* — se a temperatura subir demais, abre uma janela ou liga um exaustor
  - *LED* — se estiver escuro, acende iluminação sintética
  - *Buzzer* — se a água do reservatório acabar, apita para alertar o operador
---
