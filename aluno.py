class Aluno:
    def __init__(self, nome, matricula, curso):
        
        self.__nome = None 
        self.__matricula = None
        self.__notas = []
        self.curso = curso  

        self.set_nome(nome)
        self.set_matricula(matricula)

    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        if nome: 
            self.__nome = nome
        else:
            print("Nome inválido. Por favor, insira um nome válido.")

    def get_matricula(self):
        return self.__matricula


    def set_matricula(self, matricula):
        if matricula.isdigit() and 8 <= len(matricula) <= 10:
            self.__matricula = matricula
        else:
            print("Matrícula inválida. Deve conter entre 8 e 10 dígitos numéricos.")

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.__notas.append(nota)
        else:
            print("Nota inválida!")

    def calcular_media(self): 
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
    
    def mostrar_dados(self):
        print(f"Nome: {self.get_nome()}")
        print(f"Matrícula: {self.get_matricula()}")
        print(f"Média: {self.calcular_media():.2f}")
        print(self.curso.descricao())