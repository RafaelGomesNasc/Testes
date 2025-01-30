from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
class Funcionario(Pessoa, ABC):

    # Atributo abstrato
    @property
    @abstractmethod
    def matricula(self):
        pass
    @matricula.setter
    def matricula(self, value : int):
        pass
    
    # Métodos abstratos
    @abstractmethod
    def definirSalario(self, value : float):
        pass

    @abstractmethod
    def definirCursoSelecionado(self, nomedocurso : str):
        pass

class Professor(Funcionario):

    _baseId = 0

    @classmethod
    def getNextId(cls):
        id = cls._baseId
        cls._baseId += 1
        return id

    def __init__(self, nome = '', salario = 0, cursoLecionado = ''):
        Pessoa.__init__(self, nome)
        self.id = Professor.getNextId()
        self.matricula = None  # Inicializa a matrícula como None
        self.salario = salario
        self.cursoLecionado = cursoLecionado

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    def definirSalario(self, salario):
        self.salario = salario

    def definirCursoSelecionado(self, curso):
        self.cursoLecionado = curso

    def __str__(self):
        return f"Nome: {self.nome}, Id: {self.id}, Matrícula: {self.matricula}, Curso: {self.cursoLecionado}, Salário: {self.salario}"

class Estudante(Pessoa, ABC):

    @abstractmethod
    def definirMatricula(self, matricula : int):
        pass

    @abstractmethod
    def definirCursoFrequentado(self, curso : str):
        pass

class Aluno(Estudante):

    _baseId = 0

    @classmethod
    def getNextId(cls):
        id = cls._baseId
        cls._baseId += 1
        return id

    def __init__(self, nome = '', matricula = 0, cursoFrequentado = ''):
        Pessoa.__init__(self, nome)
        self.id = Aluno.getNextId()
        self.matricula = matricula
        self.cursoFrequentado = cursoFrequentado

    def definirMatricula(self, matricula : int):
        self.matricula = matricula
    def definirCursoFrequentado(self, curso : str):
        self.cursoFrequentado = curso

    def __str__(self):
        return f"Nome: {self.nome}, Id: {self.id}, Matrícula: {self.matricula}, Curso Frequentado: {self.cursoFrequentado}"

class AssistenteEnsino(Funcionario, Estudante):
    
    _baseId = 0

    @classmethod
    def getNextId(cls):
        id = cls._baseId
        cls._baseId += 1
        return id

    def __init__(self, nome = '', matricula = 0, cursoFrequentado = '', salario = 0, cursoLecionado = ''):
        Pessoa.__init__(self, nome)
        self.id = AssistenteEnsino.getNextId()
        self.matricula = matricula
        Aluno.__init__(self, cursoFrequentado)
        self.salario = salario
        Professor.__init__(self, cursoLecionado)
    
    @property
    def matricula(self):
        return self._matricula
    @matricula.setter
    def matricula(self, value : int):
        self._matricula = value


    def definirSalario(self, valor : float):
        self.salario = valor
    
    def definirCursoSelecionado(self, nomedocurso):
        self.curso = nomedocurso

    def definirCursoFrequentado(self, curso : str):
        self.curso = curso
    
    def definirMatricula(self, matricula : int):
        self.matricula = matricula

    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Curso: {self.curso}, Salário: {self.salario}"

if __name__ == '__main__':
    #--------------------------------#
    # Pessoa
    #--------------------------------#
    try:
        pessoa = Pessoa("João")
        print(pessoa.nome)
    except Exception as e:
        print(e)
    #--------------------------------#
    # Funcionario
    #--------------------------------#
    try:
        funcionario = Funcionario("Maria")
        funcionario.definirSalario(1000)
        funcionario.definirCursoSelecionado("Engenharia")
    except Exception as e:
        print(e)
    #--------------------------------#
    # Professor
    #--------------------------------#
    try:
        professor = Professor("José", 2000, "Matemática")
        professor.matricula = 1234
        professor.definirSalario(3000)
        professor.definirCursoSelecionado("Física")
        professor2 = Professor("Maria", 2500, "Química")
        print(professor.__dict__)
        print(professor2.__dict__)
        print(professor)
        print(professor2)
    except Exception as e:
        print(e)
    #--------------------------------#
    # Estudante
    #--------------------------------#
    try:
        estudante = Estudante("Ana")
    except Exception as e:
        print(e)
    #--------------------------------#
    # Aluno
    #--------------------------------#
    try:
        aluno = Aluno("Carlos", 4321, "Engenharia")
        aluno.definirMatricula(5678)
        aluno.definirCursoFrequentado("Computação")
        print(aluno)
    except Exception as e:
        print(e)
    #--------------------------------#
    # AssistenteEnsino
    #--------------------------------#
    try:
        assistente = AssistenteEnsino("Mariana", 8765, "Computação", 1500, "Física")
        assistente.definirMatricula(9876)
        assistente.definirSalario(2000)
        assistente.definirCursoSelecionado("Química")
        assistente.definirCursoFrequentado("Matemática")
        print(assistente)
    except Exception as e:
        print(e)