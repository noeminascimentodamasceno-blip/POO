from curso import Curso
from aluno import Aluno


def cadastrar_cursos():
    cursos = []
    quantidade = int(input("Quantos cursos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\n Cadastro do curso {i+1}")
        nome = input("Nome do curso: ")
        duracao = int(input("DUração (em semestres): "))
        cursos.append(Curso(nome,duracao))

    return cursos 


def cadastrar_alunos(cursos):
    alunos = []
    quantidade = int(input("\nQuantos alunos deja cadastrar?"))

    for i in range(quantidade):
        print(f"\nCadastro do aluno {i+1}")
        nome = input("Matricula (8 a 10 digitos): ")
        matricula = input("Matricula (0 a 8 digitos): ")

        while True:
            escolha = input("Digite o numero do curso: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(cursos):
                curso_escolhido = cursos[int(escolha) - 1]
                break
            else:
                print("Escolha invalida.")

        aluno = Aluno(nome, matricula, curso_escolhido)
        alunos.append(aluno)

        return alunos
    

def adicionar_notas(alunos):
    for aluno in alunos:
        print(f"\nAdicionando notas para {aluno.get_nome()}:")
        for i in range(2):  
            while True:
                entrada = input(
                    f"Digite a nota {i+1} para {aluno.get_nome()}:")
                if entrada.strip() == "":
                    print("Entrada vazia. Digite uma nota valida.")
                    continue
                try:
                    nota = float(entrada)
                    if 0 <=  nota <= 10:
                        aluno.adicionar_nota(nota)
                        break
                    else:
                        print("A nota deve está entre 0 e 10.")
                except ValueError:
                    print("Valor invalido. Digite um numero")

