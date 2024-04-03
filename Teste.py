def mostrarNumero():
  print("Digite um número divisível por 2 e 3")
  numero_valido = False

  while(not(numero_valido)):
    try:
      num = int(input())
      if(num % 2 == 0):
        print("Boa! " + str(num) + " é um número divisível por 2")
        numero_valido = True
      elif(num % 3 == 0):
        print("Boa! " + str(num) + " é um número divisível por 3")
        numero_valido = True
      else:
        print("Número informado " + str(num) + " não é divisível por 2 ou 3")        
    except:
      print("Precisa digitar um número inteiro")

mostrarNumero()