#5) Escreva um programa que inverta os caracteres de um string.
# Evitar usar funções prontas, como; reverse

def inverte(string):
    string_vazia = ''
    for i in range(len(string) -1, -1, -1):
        string_vazia += string[i]

    return string_vazia

def main():
    string = input('Digite a string que deseja inverter: ')
    result = inverte(string)
    print(f'{string} invertida fica: {result}')

main()