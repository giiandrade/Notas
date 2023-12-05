# Função para calcular a média aritmética das notas
def calcular_media(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4

# Função principal
def main():
    # Solicitar as notas ao usuário
    n1 = float(input("Digite a nota do primeiro bimestre: "))
    n2 = float(input("Digite a nota do segundo bimestre: "))
    n3 = float(input("Digite a nota do terceiro bimestre: "))
    n4 = float(input("Digite a nota do quarto bimestre: "))

    # Calcular a média
    media = calcular_media(n1, n2, n3, n4)

    # Exibir a média
    print(f"A média aritmética das notas é: {media}")

# Chamar a função principal
if __name__ == "__main__":
    main()