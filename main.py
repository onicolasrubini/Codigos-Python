from divisao import divida
from NotaDeAlunos import MediaNota
from FaranaiteToCelcios import ConvertToCelcius
from adicao import adicionar
from resto import resto
from metroToCentimetro import metroCentimetro
from parOuImpar import ParOuImpar
from subtracao import subtra
from lanchonete import mostrar_cardapios, obter_preco, mostrar_opcoes

def calculadora():
    while True:
        print("Bem vindo à Calculadora:")
        print("Digite 1 para Adição | 2 para Divisão | 3 para Par ou Ímpar | 4 para Resto | 5 para Converter Fahrenheit | 6 para Nota dos Alunos | 7 para Converter Metros para Centímetros | 8 para Subtração")
        opcao = input("Digite um número (ou 'sair' para sair): ")

        if opcao == "sair":
            break

        switcher = {
            "1": adicionar,
            "2": divida,
            "3": ParOuImpar,
            "4": resto,
            "5": ConvertToCelcius,
            "6": MediaNota,
            "7": metroCentimetro,
            "8": subtra,
        }

        acao = switcher.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")

        print()
def lanchonete():
    mostrar_cardapios()
    cardapio = int(input("Digite o número do cardápio: "))
    mostrar_opcoes(cardapio)
    item = int(input("Digite o número do item: "))
    
    preco = obter_preco(cardapio, item)
    if preco is not None:
        print(f"O preço do item escolhido é R${preco:.2f}")
    else:
        print("Opção inválida.")
    
def main():
    while True:
        print("Bem vindo ao programa da Fábrica de Software 108. Digite o programa que gostaria de usar!")
        print("Digite 1 para Calculadora | 2 Lanchonete")
        opcao = input("Digite um número (ou 'sair' para sair): ")

        if opcao == "sair":
            print("Saindo do programa...")
            break

        
        switcher = {
            "1": calculadora,
            "2": lanchonete,
        }

       
        acao = switcher.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")

        print()

main()
