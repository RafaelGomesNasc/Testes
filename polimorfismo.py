
# Criar uma hieranquia de classes de questões de 3 tipos, enunciado único, enunciado de verdadeiro ou falso e múltipla escolha
# Criar uma função que pode imprimir (__str__) respostas de diversas formas diferentes utilizando polimorfismo e duck typing
    
class Questao:
    def __init__(self, enunciado: str, resposta: str = None, gabarito: str = None):
        self.enunciado = enunciado
        self.resposta = resposta
        self.gabarito = gabarito

    def __str__(self):
        return f'{self.enunciado}'
    def responder(self, resposta: str):
        resposta = input('Digite a resposta: ')
        self.resposta = resposta

    def validarResposta(self):
        if self.resposta == self.gabarito:
            return True
        else:
            return False
    
class QuestaoVF(Questao):
    # args é uma tupla
    def __init__(self, enunciado: str, *args, resposta = None, gabarito = None):
        Questao.__init__(self, enunciado)
        self.args = args
        self.resposta = resposta
        self.gabarito = gabarito

    def __str__(self):
        questao = f'{self.enunciado}\n'
        for opc in self.args:
            questao += f'( ) {opc}\n'
        return questao
    
    def responder(self):
        resposta = []
        for opc in self.args:
            r = f'({input()}) {opc}'
            print(r)
            resposta += r*2
        self.resposta = resposta
        return resposta

    
class QuestaoSE(Questao):
    def __init__(self, enunciado, *args):
        Questao.__init__(self, enunciado)
        self.args = args

    def __str__(self):
        questao = f'{self.enunciado}\n'
        num = 1
        for i in range(len(self.args)):
            questao += f'{num}. {self.args[i]}\n'
            num *= 2
        return questao

class QuestaoME(Questao):
    # kwargs é um dicionário
    def __init__(self, enunciado: str, **kwargs):
        Questao.__init__(self, enunciado)
        self.kwargs = kwargs

    def __str__(self):
        questao = f'{self.enunciado}\n'
        for key, value in self.kwargs.items():
            questao += f'{key}. {value}\n'
        return questao

# Duck typing - Uma mesma função pode ser utilizada para diferentes tipos de objetos
def imprimirQuestao(questao):
    print(questao)

if __name__ == '__main__':
    Questao1 = Questao('Qual a cor do cavalo branco de Napoleão?')
    Questao2 = QuestaoVF('A terra é plana?', 'Verdadeiro', 'Falso')
    Questao3 = QuestaoME('Qual a cor do cavalo branco de Napoleão?', a='Branco', b='Preto', c='Cinza', d='Marrom')
    Questao4 = QuestaoSE('Qual a cor do cavalo branco de Napoleão?', 'Branco', 'Preto', 'Cinza', 'Marrom', 'Fuchsia')

    for q in [Questao1, Questao2, Questao3, Questao4]:
        imprimirQuestao(q)