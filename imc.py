from random import randint


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False

    return True

def cadastrarpaciente():
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu cpf: ")
    
    if cpf_validate(cpf) == False:
        print("CPF invalido")
        cpf = input("Digite o seu cpf: ")

    rg = input("Digite o seu RG:")
    end = input("Digite o seu endereço:")
    peso = float(input("Digite o seu peso:"))
    telefone = input("Digite o seu telefone:")
    email = input("Digite o seu email:")
    datanasc = input("Digite sua data de nascimento: 13/10/2000: ")
    comorbidade =  input("Digite sim ou nao caso tenha comorbidade: ")
    altura = float(input("Digite a sua altura em m:"))

    IMC = peso / (altura * altura)

    if IMC >= 40:
        situacao = "Obesidade grau III"
    elif IMC >= 35 and IMC < 39.9:
        situacao = "Obesidade grau II"
    elif IMC >= 30 and IMC < 34.9:
        situacao = "Obesidade grau I"
    elif IMC >= 25 and IMC < 29.9:
        situacao = "Sobrepeso"
    elif IMC >= 18.6 and IMC < 24.9:
        situacao = "Normal"
    elif IMC <= 18.5:
        situacao = "Abaixo do Normal"

    ano = datanasc.split("/")
    ano = ano[2]
    idade = 2021-int(ano)
    

    print("O Paciente {} tem {} anos e esta com IMC {}".format(nome,idade,situacao))

def cadastrar_profissional():
    nome = input("Digite o seu nome: ")
    cpf = input("Digite o seu cpf: ")
    
    if cpf_validate(cpf) == False:
        print("CPF invalido")
        cpf = input("Digite o seu cpf: ")

    anos_xp = input("Quantos anos de experiencia? ")
    if anos_xp == 1:
        status = "novato"
    elif anos_xp > 1 and anos_xp <5:
        status = "Treinador"
    else:
        status = "Expert"

cadastrarpaciente()
