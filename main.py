#Programa que transforme notas universitaria a Letras
# de 91 a 100 es A
# de 81 a 90 es B
# de 71 a 80 es C
# de 61 a 70 es D
# todo lo demas es F 50 <
nota = int(input('Digame la nota: '))
if (nota >= 91):
  print('Es A')
elif (nota >= 81):
  print('Es B')
elif (nota >= 71):
  print('Es C')
elif (nota >= 61):
  print('Es D')
else:
  print('Es F')
print('Fin')