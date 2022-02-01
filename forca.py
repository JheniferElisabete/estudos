import random

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
def inicializa_letras_acertadas(palavra):
    # define a variavel da palavra secreta
    #Guarda a palavra secreta tudo maiuscula
    #palavra_secreta = "banana".upper()
    # Usa esse caractere para cada letra da minha palavra
    #letras_acertadas = ["_" for letra in palavra_secreta]
    #Deixando a linha mais apresentavel
    return ["_" for letra in palavra]
def pede_chute():
    chute = input("Informe a letra desejada ")
    # remover espaços que o usuario digitou
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    # para cada letra dentro da minha palavra
    for letra in palavra_secreta:
        # para não ocorrer os risco de diferenciar letras maiusculas e minusculas, vamos colocar elas como maiuscula .upper()
        if (chute.upper() == letra.upper()):
            # print("Encontrei a letr a{} na posição {}".format(letra, index))
            letras_acertadas[index] = letra
        index += 1
def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def jogar():
    imprime_mensagem_abertura()
    #Para não dar erro, ao carregar a palavra secreta eu quero que a função inicialize a palavra secreta e retorne a palavra secreta
    palavra_secreta = carrega_palavra_secreta()
    #Coloca um parametro ja que a as funç~es não veem as variaveis das demais funçoes/ nesse caso estão passando o parametro que esta na variavel palavra secreta com o
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    #consultar tipo da variavel type(variavel)
    print("Adivinhe a palavra", letras_acertadas)


    enforcou = False
    acertou = False
    # Conta as tentativas
    tentativas = 0

    #enquanto (não se enforcou E não acertou): vamos jogar
    #enquanto não falso (verdadeiro) executa:
    while (not enforcou and not acertou):

        chute = pede_chute()
        #O chute esta dentro da palavra secreta, se sim execute esse bloco de notas
        if (chute in palavra_secreta):
           marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        #ele não acertou enquanto estiver com o _ dentro das letras acertadas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

def carrega_palavra_secreta():
    #abrir o arquivo (R= ler, A=Adicionar, W=escrita)
    arquivo = open("palavras.txt", "r")

    palavras = []
    #para cada linha dentro do arquivo faça
    for linha in arquivo:
        #remover o /n no final da palavra
        linha = linha.strip()
        #guarda
        palavras.append(linha)

    #Não esquecer de fechar o arquivo
    arquivo.close()

    #importa a palavra aleatoria (De zero ao tamanho da lista)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    #a fujção vai executar e reotnar a pallavra secreta
    return palavra_secreta
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



#min(variavel) -> numero minimo mas(variavel) _> numero maximo len(variavel) -> tamanho da variavel de uma lista
# podemos utilizar o operador in para verificar se um determinado elemento está dentro de uma lista.
#tuple = uma lista imutavel (Não pode ser alterada)
#Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.
#O recurso List Comprehension permite inicializar qualquer lista a partir de outra
#criar função para encapsular as informações
if(__name__ == "__main__"):
    jogar()

