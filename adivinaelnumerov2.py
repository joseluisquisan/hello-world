import random

def run():
  intentos = 0
  numero_aleatorio = random.randint(1, 10)
  numero_elegido = int(input('Elige un número del 1 al 10: '))
  while numero_elegido != numero_aleatorio:
    if numero_elegido < numero_aleatorio:
      print('Elige un número más grande')
    else: 
      print('Elige un número más pequeño')
    intentos += 1
    numero_elegido = int(input('Elige otro número: '))
      
  print('Habeís ganao con ' + str(intentos + 1) + ' intentos')

if __name__ == '__main__':
  run()