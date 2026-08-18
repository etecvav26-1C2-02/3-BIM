# Respostas — Conceitos Básicos de Eletricidade, Eletrônica, Sensores e Atuadores
 
---
 
## Questão 1 — O LED acendeu. Está tudo certo?

**Não concordamos com o aluno.**
O fato de o LED ter acendido **não garante** que a ligação esteja correta ou segura.
 
Ligar um LED diretamente ao pino do microcontrolador, sem um **resistor em série** para limitar a corrente, é um erro comum. O LED exige limitação de corrente; sem o resistor, ele tenta puxar mais corrente do que a porta do microcontrolador pode fornecer com segurança. Isso pode **queimar o pino do chip** ou **diminuir drasticamente a vida útil do LED**.

