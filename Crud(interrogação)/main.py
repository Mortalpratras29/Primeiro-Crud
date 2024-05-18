import os
import json
from menus import cipal

alunos = []


# sistema de busca de aluno
def google(matricula):
    for aluno in alunos:
        if aluno["Matricula"] == matricula:
            return aluno


while True:
    # menu principal
    print(cipal)
    C = int(input())

    if C == 1:
        os.system("cls")
        ID = int(input("Matricula do Aluno: "))
        Nome = input("Nome do Aluno: ")
        Nota = float(input("Nota do Aluno: "))
        print("Aluno cadastrado com suscesso")
        Aluno = {"Matricula": ID, "Nome": Nome, "Nota": Nota}
        alunos.append(Aluno)
    elif C == 2:
        os.system("cls")
        for aluno in alunos:
            print(aluno)
    elif C == 3:
        os.system("cls")
        ID = int(input("Matricula do aluno: "))
        aluno = google(ID)
        if aluno:
            print(f"Notas atuais: {alunos}")
            aluno["Nota"] = int(input("Digite a nova nota aqui: "))
            print("Nota Atualizada com suscesso")
    elif C == 4:
        os.system("cls")
        ID = int(input("Matricula do aluno: "))
        aluno = google(ID)
        if aluno:
            alunos.remove(aluno)
            print("Aluno excluido com suscesso")
        else:
            print("Aluno não encontrado")
    elif C == 5:
        os.system("cls")
        print("Saindo...")
        break
    else:
        print("Escolha invalida")
