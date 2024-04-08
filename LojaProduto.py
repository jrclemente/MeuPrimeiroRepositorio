#import sys
import os

#Limpar tela(console)
def limpar():
     os.system('cls')

listaProdutos = []

def ListaProdutos(listaProdutos):

  if (len(listaProdutos) > 0):
    print()
    print('*** Lista de Produtos ***')
    for item in listaProdutos:
      print(item)
  else:
    print('Não foi incluido nenhum produto na lista!!!')
  return ""

def VerificaProduto(listaProdutos):

  produto = input('Qual produto está precisando: ')

  temProduto = True
  try:
    idex = listaProdutos.index(produto)
  except:
    temProduto = False
    print('Produto %s em falta!!!' %produto)
  return temProduto

def ExisteProduto(produto, listaProdutos):
  jaExiste = False
  try:
    idex = listaProdutos.index(produto)
    print('Este produto %s já existe!!!' %produto)
    jaExiste = True
  except:
     jaExiste = False
  return jaExiste

def ExcluiProduto(listaProdutos):

  produto = input('Qual produto para excluir: ')

  temProduto = True
  try:
    idex = listaProdutos.index(produto)
    del(listaProdutos[idex])
  except:
    temProduto = False
    print('Produto para excluir - %s - não identificador!!!' %produto)
  return listaProdutos

def TrocarProduto(listaProdutos):

  produto = input('Informe o produto a ser trocado: ')
  novoProduto = input('Informe o novo produto: ')

  produtoTrocado = True
  try:
    idex = listaProdutos.index(produto)
    if(not(ExisteProduto(novoProduto, listaProdutos))):
     listaProdutos[idex] = novoProduto
  except:
    produtoTrocado = False
    print('Produto %s para trocar não encontrado!!!' %produto)

  return listaProdutos

def AdicionaProduto(listaProdutos):

  print('Informe o novo produto ou FIM para terminar: ')

  incluido = True
  eFim = False
  while(not(eFim)):
    produto = input()
    if(produto != 'FIM'):
      try:
        idex = listaProdutos.index(produto)
        print('Este produto %s já existe!!!' %produto)
        incluido = False
      except:
        listaProdutos.append(produto)
    else:
      eFim = True

  return listaProdutos

def Processo(listaProdutos, opcao):
  match opcao:
    case 1:
      ListaProdutos(listaProdutos)
    case 2:
      temProduto = VerificaProduto(listaProdutos)
      if(temProduto):
       print('Produto encontrado!!!')
    case 3:
      listaProdutos = TrocarProduto(listaProdutos)
      ListaProdutos(listaProdutos)
    case 4:
      listaProdutos = AdicionaProduto(listaProdutos)
      ListaProdutos(listaProdutos)
    case 5:
      listaProdutos = ExcluiProduto(listaProdutos)
      ListaProdutos(listaProdutos)
    case _:
      print('Opção Inválida!!!')

  return '';

def ExibirMenu():
    print("Opções:")
    print("1. Verificar Lista de Produtos")
    print("2. Verificar um Produto")
    print("3. Trocar Produto")
    print('4. Adicionar Produto(s)')
    print("5. Excluir Produto")
    print("99. Sair")
    return ''

while True:
  limpar()
  print(ExibirMenu())
  opcao = int(input("Escolha a Opção: "))

  if(opcao != 99):
    resultado = Processo(listaProdutos, opcao)
    input('Continua....')
    print()
  else:
    #erro = sys.exit('Fim do Processo!!')
    print('Fim do Processo!!!')
    break