"""
    Autor: Daniel de sousa Araujo,MIguel Marcelo
    Data: Agosto/2026
   Descrição: Simula um sistema simples de senha com até 3 tentativas.
"""
  senhaCorreta= 1234
tentativas= 1
limiteTentativas= 3
#definir 
senha = int(input("Digite a Senha: "))

while (senha != senhaCorreta and tentativas < limiteTentativas): #loop até acertar
    senha = int(input("Senha incoreta. Tente novamente:"))
    tentativas += 1 #max tres tentativas 

if senha == senhaCorreta:
    
    print("Acesso liberado.")
    
else:
    
    print("Acesso bloqueado.")
