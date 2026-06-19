# nome = "joao"
# idade = 20
# salario = 3500.0

# print(f'{nome} tem {idade} anos e recebe {salario}!')

# numero_1 = float(input("Digite um numero: "))
# numero_2 = float(input("Digite outro numero: "))

# print(numero_1 + numero_2)
# print(numero_1 * numero_2)
# print(numero_1 - numero_2)
# print(numero_1 / numero_2)

# temp_celsius = 25

# fahrenheit = temp_celsius * 9/5 + 35
# print(fahrenheit)

# frase = "Python é incrível"

# print(type(frase))
# print(len(frase.lower()))
# print(len(frase.upper()))

# def eh_palindromo(palavra):
#     lista_normal = list(palavra)
#     lista_reversa = lista_normal.reverse()
#     print(lista_reversa)
#     print(lista_normal)
#     if lista_normal == lista_normal.reverse():
#         return True
#     else:
#         return False

# print(eh_palindromo('ovo'))

# def converter_temperatura(valor, unidade):
#     if unidade.lower() == "c":
#         temp_fahrenheit = (valor * 9/5) + 32
#         return f'{temp_fahrenheit} graus fahrenheit'
#     elif unidade.lower() == "f":
#         temp_celsius = (valor - 32) * 5/9
#         return f'{temp_celsius} graus celsius'
#     else:
#         return "Unidade incorreta."
    
# print(converter_temperatura(64, "f"))
# print(converter_temperatura(25, "c"))
# # print(converter_temperatura(25, "a"))

# alunos = [
#     {"nome": "Ana", "nota": 8.5},
#     {"nome": "Bruno", "nota": 6.0},
#     {"nome": "Carla", "nota": 9.2}
# ]

# filtro = [x for x in alunos if x['nota'] >= 7]
# print(filtro)

# dict_frequencia = {}
# frase = "o gato e o cachorro"

# lista_de_palavras = frase.split()
# for i in lista_de_palavras:
#     quantidade = lista_de_palavras.count(i)
#     dict_frequencia[i] = quantidade

# print(dict_frequencia)

# -------------------- Loops/Classes/Try exercises --------------------

## Exercise 1

# contador = 0

# numero_escolhido = int(input("Digite um número de 0 a 10: "))
# if numero_escolhido > 10 or numero_escolhido <=     0:
#     print("Erro")
# else:
#     for i in range(0, 10):
#         contador += numero_escolhido
#         print(contador)

## exercise 2

# senha_correta = '12345'
# contador_de_tentativas = 0
# ativo = True

# while ativo:
#     contador_de_tentativas += 1
#     if contador_de_tentativas == 4:
#         print("Você foi bloqueado!")
#         break
#     senha_digitada = input("Digite a senha para acessar o caixa: ")
#     if senha_digitada == senha_correta:
#         print("Caixa acessado!")
#         break

## exercise 3

# altura = int(input("Escolha a altura do triângulo: "))
# altura_base = "*"

# for i in range(0, altura):
#     print(altura_base)
#     altura_base += "*"

## exercise 4

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#          self.nome = nome
#          self.preco = preco
#          self.quantidade = quantidade

#     def vender(self, quantidade):
#          if quantidade <= 0:
#              print("Quantidade insuficiente")
#          elif quantidade <= self.quantidade:
#              print("Estoque insuficiente")
#          else:
#              self.quantidade -= quantidade

#     def valor_total(self):
#          return self.preco * self.quantidade

# ## exercise 5

# class Carrinho:
#     def __init__(self):
#         self.lista = []

#     def adicionar(self, produto):
#         self.lista.append(produto)

#     def total_compra(self):
#         total = 0
#         for produto in self.lista:
#             total += produto.valor_total()
#         return total

## exercise 6

# class ContaBancaria:
#     def __init__(self, saldo):
#         self.__saldo = saldo

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#         else:
#             print("Valor deve ser maior que zero.\n")

#     def sacar(self, valor):
#         if self.__saldo >= valor:
#             self.__saldo -= valor
#         else:
#             print("Não houve alteração no saldo total\n")

#     def __str__(self):
#         return f'Seu saldo total é de {self.__saldo}'
    
# c1 = ContaBancaria(1500)
# c1.depositar(1000)
# print(c1)

## exercise 7

# def dividir_seguro(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Não há número divisivel por 0.")
#     except TypeError:
#         print("Digite um número.")

## exercise 8

# config = {
#     "host": "localhost",
#     "porta": 8080
# }

# try:
#     debug = config['debug']
# except KeyError:
#     debug = False

## bonus exercise

class GerenciadorTarefas:
    def __init__(self):
        self.__tarefas = []

    def adicionar(self, add):
        self.__tarefas.append(add)
        print(f"\nTarefa '{add}' adicionada!")

    def remover(self, remove):
        if remove in self.__tarefas:
            self.__tarefas.remove(remove)
        else:
            print("\nProduto não existente.")
    
    def listar(self):
        if not self.__tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(self.__tarefas, 1):
                print(f"\n{i}. {tarefa}")
    
programa_1 = GerenciadorTarefas()

while True:
    try:
        opcao_escolhida = int(input("""
Gerenciador de tarefas:
                                    
1 - Adicionar tarefa
2 - Remover tarefa
3 - Listar tarefas
4 - Sair
                                    
"""))
        if opcao_escolhida == 1:
            restaurante_adicao = input("Digite a tarefa a ser adicionada: ")
            programa_1.adicionar(restaurante_adicao)
        elif opcao_escolhida == 2:
            restaurante_remocao = input("Digite a tarefa a ser removido: ")
            programa_1.remover(restaurante_remocao)
        elif opcao_escolhida == 3:
            programa_1.listar()
        elif opcao_escolhida == 4:
            print("\nSaindo...")
            break
        else:
            print("Opção inválida. Digite 1, 2, 3 ou 4.")
    except ValueError:
        print("Digite apenas números (1, 2, 3 ou 4).")
    except Exception as e:
        print(f"Erro inesperado: {e}")