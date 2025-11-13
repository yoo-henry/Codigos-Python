# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Nome do aluno 
nome_aluno = input("Digite o nome do aluno: ")
# Prova
prova01 = float(input("Digite a nota da primeira prova: "))
prova02 = float(input("Digite a nota da segunda prova: "))
prova03 = float(input("Digite a nota da terceira prova: "))
# Soma
soma = prova01 + prova02 + prova03
# Média 
media = soma / 3
#Se o aluno está aprovado ou não

print("| ______________________________ |")
print("| SISTEMA DE PROVAS")
print("| ______________________________ |")
print(f"| Nome do aluno: {nome_aluno}")
print(f"| Nota da primeira prova: {prova01}")
print(f"| Nota da segunda prova: {prova02}")
print(f"| Nota da terceira prova: {prova03}")
print("| ______________________________ |")
print(f"| Aluno: {nome_aluno} ")
print(f"| Média: {media:.2f}")
if media >= 5: 
    print("| Aluno aprovado")
else:
    print("|Reprovado")
print("| ______________________________ |")