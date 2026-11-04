import math


# Funções para cada operação básica e avançada
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def raiz_quadrada(a):
    if a < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return math.sqrt(a)


def calculadora():
    while True:
        print("\n" + "=" * 25)
        print("   CALCULADORA SIMPLES   ")
        print("=" * 25)
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Raiz Quadrada (√)")
        print("0 - Sair")
        print("=" * 25)

        try:
            opcao = input("Escolha a operação desejada (0-5): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando a calculadora. Até mais!")
            break

        # Opção de saída
        if opcao == "0":
            print("Encerrando a calculadora. Até mais!")
            break

        # Operações binárias (adição, subtração, multiplicação, divisão)
        if opcao in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, insira apenas valores numéricos válidos.")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\nEncerrando a calculadora. Até mais!")
                break

            try:
                if opcao == "1":
                    resultado = somar(num1, num2)
                    print(f"\nResultado: {num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    print(f"\nResultado: {num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"\nResultado: {num1} × {num2} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    print(f"\nResultado: {num1} ÷ {num2} = {resultado}")
            except ZeroDivisionError as e:
                print(f"\nErro: {e}")

        # Operação unária (raiz quadrada)
        elif opcao == "5":
            try:
                num = float(input("Digite o número: "))
            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
                continue
            except (KeyboardInterrupt, EOFError):
                print("\nEncerrando a calculadora. Até mais!")
                break

            try:
                resultado = raiz_quadrada(num)
                print(f"\nResultado: √{num} = {resultado}")
            except ValueError as e:
                print(f"\nErro: {e}")

        else:
            print("Opção inválida! Por favor, escolha um número de 0 a 5.")


# Inicia o programa
if __name__ == "__main__":
    calculadora()
