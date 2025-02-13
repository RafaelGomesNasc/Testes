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
        # Se for passado um valor para args, ele atualiza o valor de self.args
        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args
        # Se não for passado um valor para args, ele pega o valor de self.args
        else:
            args = self.args
        # Retorna o valor lógico da operação AND de todas as entradas
        return all(args)

class OR(PORT):
    def __init__(self, *args):
        for a in args:
            if not isinstance(a, (bool, int)):
                raise TypeError("Entrada deve ser um valor booleano ou inteiro")
            if isinstance(a, int) and a not in (0, 1):
                raise ValueError("Entrada deve ser 0 ou 1")
        self.args = args

    def eval(self, *args):
        # Se for passado um valor para args, ele atualiza o valor de self.args
        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args
        # Se não for passado um valor para args, ele pega o valor de self.args
        else:
            args = self.args
        # Retorna o valor lógico da operação OR de todas as entradas
        return any(args)


class XOR(PORT):
    def __init__(self, *args):
        for a in args:
            if not isinstance(a, (bool, int)):
                raise TypeError("Entrada deve ser um valor booleano ou inteiro")
            if isinstance(a, int) and a not in (0, 1):
                raise ValueError("Entrada deve ser 0 ou 1")
        self.args = args

    def eval(self, *args):
        # Se for passado um valor para args, ele atualiza o valor de self.args
        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args
        # Se não for passado um valor para args, ele pega o valor de self.args
        else:
            args = self.args
        # Retorna o valor lógico da operação XOR de todas as entradas
        return sum(args) == 1


class NAND(PORT):
    def __init__(self, *args):
        for a in args:
            if not isinstance(a, (bool, int)):
                raise TypeError("Entrada deve ser um valor booleano ou inteiro")
            if isinstance(a, int) and a not in (0, 1):
                raise ValueError("Entrada deve ser 0 ou 1")
        self.args = args

    def eval(self, *args):
        # Se for passado um valor para args, ele atualiza o valor de self.args
        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args
        # Se não for passado um valor para args, ele pega o valor de self.args
        else:
            args = self.args
        # Retorna o valor lógico da operação NAND de todas as entradas
        return not all(args)
    

class NOR(PORT):
    def __init__(self, *args):
        for a in args:
            if not isinstance(a, (bool, int)):
                raise TypeError("Entrada deve ser um valor booleano ou inteiro")
            if isinstance(a, int) and a not in (0, 1):
                raise ValueError("Entrada deve ser 0 ou 1")
        self.args = args

    def eval(self, *args):
        # Se for passado um valor para args, ele atualiza o valor de self.args
        if len(args) >= 2:
            for a in args:
                if not isinstance(a, (bool, int)):
                    raise TypeError("Entrada deve ser um valor booleano ou inteiro")
                if isinstance(a, int) and a not in (0, 1):
                    raise ValueError("Entrada deve ser 0 ou 1")
            self.args = args
        # Se não for passado um valor para args, ele pega o valor de self.args
        else:
            args = self.args
        # Retorna o valor lógico da operação NOR de todas as entradas
        return not any(args)


if __name__ == "__main__":
    #-------------------------------------#
    # PORT
    #-------------------------------------#
    try:
        port = PORT()
        print(port.eval())
    except Exception as e:
        print(e)
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
    try:
        or1 = OR(0, 0)
        print(or1.eval())
    except Exception as e:
        print(e)
    try:
        or2 = OR(0, 1, 0)
        print(or2.eval())
    except Exception as e:
        print(e)
    #-------------------------------------#
    # XOR
    #-------------------------------------#
    try:
        xor1 = XOR(1, 1)
        print(xor1.eval())
    except Exception as e:
        print(e)
    try:
        xor2 = XOR(1, 0, 1)
        print(xor2.eval())
    except Exception as e:
        print(e)
    #-------------------------------------#
    # NAND
    #-------------------------------------#
    try:
        nand1 = NAND(1, 1)
        print(nand1.eval())
    except Exception as e:
        print(e)
    try:
        nand2 = NAND(1, 0, 1)
        print(nand2.eval())
    except Exception as e:
        print(e)
    #-------------------------------------#
    # NOR
    #-------------------------------------#
    try:
        nor1 = NOR(0, 0)
        print(nor1.eval())
    except Exception as e:
        print(e)
    try:
        nor2 = NOR(0, 1, 0)
        print(nor2.eval())
    except Exception as e:
        print(e)
