qatual= int(input('Digite a quantidade atual em estoque: '))
qmaxima= int(input('Digite a quantidade maxima de estoque do produto: '))
qminima= int(input('Digite a quantidade minima de estoque do produto: '))
qmedia= qmaxima + qminima/2
if qatual >= qmedia:
 print('Não efetuar compra')
if qatual < qmedia:
 print('Efetuar compra') 