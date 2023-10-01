nota1= float(input('Digite a sua primeira nota: '))
nota2= float(input('Digite a sua segunda nota: '))
media= (nota1 + nota2)/2
print(nota1, nota2)
print(media)
if media >=9.0 <=10.0 :
 print('Conceito A/APROVADO')
if media >=7.5 <=8.9:
 print('Conceito B/APROVADO')
if media >=6.0 <=7.4:
 print('Conceito C/APROVADO')
if media >=4.0 <=5.9:
 print('Conceito D/REPROVADO')
if media >=0 <=3.9:
 print('Conceito E/REPROVADO')