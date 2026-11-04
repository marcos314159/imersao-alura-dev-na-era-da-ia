# Funções para cada operação básica
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def calculadora():
    while True:
        print("\n" + "=" * 25)
        print("   CALCULADORA SIMPLES   ")
        print("=" * 25)
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("0 - Sair")
        print("=" * 25)

        opcao = input("Escolha a operação desejada (0-4): ").strip()

        # Opção de saída
        if opcao == "0":
            print("Encerrando a calculadora. Até mais!")
            break

        # Verifica se a opção é válida
        if opcao in ("1", "2", "3", "4"):
            try:
                # Entrada dos números
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, insira apenas valores numéricos válidos.")
                continue

            # Executa a operação correspondente
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
        else:
            print("Opção inválida! Por favor, escolha um número de 0 a 4.")

# Inicia o programa
if __name__ == "__main__":
    calculadora()