"""
Métodos auxiliares
"""
def divisao(a,b):
    return a / b

def soma(a,b):
    return a + b

def multiplicacao(a,b):
    return a * b

"""
Bloco do programa principal
"""
if __name__ == '__main__':
    """
    Bloco para definição das variável
    """
    variavel_1 = 10
    variavel_2 = 35
    variavel_3 = 0


    """
    Bloco para execução das rotinas do sistema
    """
    variavel_3 = multiplicacao(divisao(variavel_1,2),soma(variavel_2,5))
    print("O retorno do programa é ",variavel_3)

    """
    Fim do programa
    """
