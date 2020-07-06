def main():
    from classes import pai
    """
    Função principal da aplicação
    """
    pai = pai.Pai()

    print(pai.imprime())

    print(pai.nome)

    from classes import filho as f
    filho = f.Filho()

    print(filho.imprime())
    #---------------------------------------------

if __name__ == "__main__":
    main()
