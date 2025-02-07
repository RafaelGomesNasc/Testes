from abc import ABC, abstractmethod


class PORT(ABC):
    def __init__(self, entrada = 1):
        self.entrada = entrada

    @abstractmethod
    def eval(self):
        pass


class NOT(PORT):
    def __init__(self, entrada = False):
        # Verificando se a entrada é um valor booleano ou inteiro
        if not isinstance(entrada, (bool, int)):
            raise TypeError("Entrada deve ser um valor booleano ou inteiro")

        # Verificando se a entrada é 0 ou 1
        if isinstance(entrada, int) and entrada not in (0, 1):
            raise ValueError("Entrada deve ser 0 ou 1")
        self.entrada = entrada

    def eval(self, entrada = None):
        # Se entrada for diferente de None, ele atualiza o valor de self.entrada
        if entrada is not None:
            self.entrada = entrada
        
        # Se não for passado um valor para entrada, ele pega o valor de self.entrada
        else:
            entrada = self.entrada

        # Retorna o valor lógico da operação NOT da entrada
        return not entrada


class AND(PORT):
    def __init__(self, *args):
        for a in args:
            if not isinstance(a, (bool, int)):
                raise TypeError("Entrada deve ser um valor booleano ou inteiro")
            if isinstance(a, int) and a not in (0, 1):
                raise ValueError("Entrada deve ser 0 ou 1")
        self.args = args

    def eval(self, *args):

        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args

        else:
            args = self.args

        res = True
        for a in args:
            res = res and a
        return res

class OR(PORT):
    pass


class XOR(PORT):
    pass


class NAND(PORT):
    pass


class NOR(PORT):
    pass


if __name__ == "__main__":
    #-------------------------------------#
    # NOT
    #-------------------------------------#
    try:
        not1 = NOT(1)
        print(not1.eval())
    except Exception as e:
        print(e)
    try:
        not2 = NOT(2)
        print(not2.eval())
    except Exception as e:
        print(e)
    #-------------------------------------#
    # AND
    #-------------------------------------#
    try:
        and1 = AND(1, 1)
        print(and1.eval())
    except Exception as e:
        print(e)
    try:
        and2 = AND(1, 0, 1)
        print(and2.eval())
    except Exception as e:
        print(e)
    #-------------------------------------#
    # OR
    #-------------------------------------#
