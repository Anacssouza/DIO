menuzinho = '''
  1 - Deposito
  2 - Saque
  3 - Extrato
  0 - Sair
'''
saldo = 0
extrato = []
max_saque = 3

print(menuzinho)
escolha = float(input('escolha: '))

def deposito(valor, saldo, extrato):
  extrato.append(f'Deposito de {valor}')
  saldo = saldo + valor
  return print(f'Seu saldo é de: {saldo}'), saldo

def saque(valor, saldo, extrato):
  extrato.append(f'Retirada de {valor}')
  saldo = saldo - valor
  return print(f'Seu saldo é de: {saldo}'), saldo

while escolha != 0:
  if escolha == 0:
      exit()
      
  elif escolha == 1: 
      valor = float(input('valor: '))
      if(valor > 0):
        deposito(valor, saldo, extrato)
        saldo = saldo + valor
      else: 
        print('Por favor, tente novamente. Valor inválido.')

  elif escolha == 2:  
    if(max_saque > 0):
      valor = float(input('valor: '))
      if(valor <= 500):
        if(valor <= saldo):
          saque(valor, saldo, extrato)
          saldo = saldo - valor
          max_saque -= 1
        else: 
          print('Saldo insuficiente')
      else: 
         print('Por favor tente de novo e inclua um valor menor ou igual a R$500')
    else: 
       print('Atingiu o limite diário de saques')

  elif escolha == 3: 
     print(f'Sua conta possui R${round(saldo,2)}')
     print(extrato)

  escolha = int(input('escolha: ')) 


