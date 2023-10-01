NúmeroContaCliente= float(input('Digite o numéro de sua conta: '))
saldo= float(input('Digite o seu saldo: '))
débito= float(input('Digite o seu débito: '))
crédito= float(input('Digite o seu crédito: '))
saldoatual= saldo - (débito + crédito)
if saldoatual >= 0:
 print('Saldo positivo')
if saldoatual < 0:
 print('Saldo negativo')