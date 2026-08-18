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
