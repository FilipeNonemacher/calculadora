from decimal import Decimal, InvalidOperation, DivisionByZero, localcontext


class Calculadora:
    OPERADORES = ('+', '-', '×', '÷')

    def __init__(self):
        self.limpar_tudo()

    def limpar_tudo(self):
        self.display = '0'
        self.historico = ''
        self.acumulado = None
        self.operador = None
        self.nova_entrada = False
        self.concluido = False
        self.segundo_anterior = None
        self.operador_anterior = None
        self.erro = False

    @staticmethod
    def _numero(texto):
        return Decimal(texto.replace(',', '.'))

    @staticmethod
    def _formatar(numero):
        if not numero.is_finite():
            raise ArithmeticError('Resultado inválido')

        if numero == 0:
            return '0'

        return format(numero.normalize(), 'f').replace('.', ',')

    @staticmethod
    def _calcular(a, operador, b):
        if operador == '+':
            return a + b

        if operador == '-':
            return a - b

        if operador == '×':
            return a * b

        if operador == '÷':
            if b == 0:
                raise ZeroDivisionError('Divisão por zero')
            return a / b

        raise ValueError('Operador desconhecido')

    def _falhar(self):
        self.display = 'Erro'
        self.historico = ''
        self.acumulado = None
        self.operador = None
        self.nova_entrada = True
        self.concluido = False
        self.erro = True

    def pressionar(self, tecla):
        """
        Processa uma tecla e retorna:
        (texto_do_visor, texto_do_historico)
        """

        if tecla == 'C':
            self.limpar_tudo()
            return self.display, self.historico

        if self.erro:
            if tecla not in '0123456789' and tecla != ',':
                return self.display, self.historico

            self.limpar_tudo()

        try:
            with localcontext() as ctx:
                ctx.prec = 28
                self._processar(tecla)

        except (
            ZeroDivisionError,
            DivisionByZero,
            InvalidOperation,
            ArithmeticError,
            OverflowError,
            ValueError
        ):
            self._falhar()

        return self.display, self.historico

    def _processar(self, tecla):

        # LIMPAR ENTRADA ATUAL
        if tecla == 'CE':
            if self.concluido:
                self.limpar_tudo()
            else:
                self.display = '0'
                self.nova_entrada = False
            return

        # APAGAR ÚLTIMO DÍGITO
        if tecla == '⌫':
            if self.nova_entrada or self.concluido:
                return

            self.display = (
                self.display[:-1]
                if len(self.display) > 1
                else '0'
            )

            if self.display in ('', '-'):
                self.display = '0'
            return

        # ENTRADA DE NÚMEROS
        if tecla in '0123456789' and len(tecla) == 1:
            if self.concluido:
                self.limpar_tudo()

            if self.nova_entrada or self.display == '0':
                self.display = tecla
                self.nova_entrada = False

            elif self.display == '-0':
                self.display = '-' + tecla

            else:
                self.display += tecla
            return

        # VÍRGULA DECIMAL
        if tecla == ',':
            if self.concluido:
                self.limpar_tudo()

            if self.nova_entrada:
                self.display = '0'
                self.nova_entrada = False

            if ',' not in self.display:
                self.display += ','
            return

        # OPERAÇÕES BÁSICAS
        if tecla in self.OPERADORES:
            atual = self._numero(self.display)

            if self.operador is not None and not self.nova_entrada:
                self.acumulado = self._calcular(
                    self.acumulado,
                    self.operador,
                    atual
                )

                self.display = self._formatar(self.acumulado)

            elif self.acumulado is None or self.concluido:
                self.acumulado = atual

            self.operador = tecla

            self.historico = (
                f'{self._formatar(self.acumulado)} {tecla}'
            )

            self.nova_entrada = True
            self.concluido = False
            self.operador_anterior = None
            self.segundo_anterior = None
            return

        # RESULTADO
        if tecla == '=':
            if self.operador is not None:
                a = self.acumulado

                b = (
                    a if self.nova_entrada
                    else self._numero(self.display)
                )

                op = self.operador

            elif self.concluido and self.operador_anterior is not None:
                a = self._numero(self.display)
                b = self.segundo_anterior
                op = self.operador_anterior

            else:
                return

            resultado = self._calcular(a, op, b)

            self.historico = (
                f'{self._formatar(a)} '
                f'{op} {self._formatar(b)} ='
            )

            self.display = self._formatar(resultado)

            self.acumulado = None
            self.operador = None
            self.operador_anterior = op
            self.segundo_anterior = b
            self.nova_entrada = True
            self.concluido = True
            return

        # OPERAÇÕES AVANÇADAS
        if tecla in ('+/-', 'x²', '²√x', '1/x', '%'):

            x = self._numero(self.display)
            original = self.display

            # INVERTER SINAL
            if tecla == '+/-':
                resultado = -x

            # ELEVAR AO QUADRADO
            elif tecla == 'x²':
                resultado = x * x

            # RAIZ QUADRADA
            elif tecla == '²√x':
                if x < 0:
                    raise ValueError('Raiz negativa')

                resultado = x.sqrt()

            # INVERSO DO NÚMERO
            elif tecla == '1/x':
                if x == 0:
                    raise ZeroDivisionError('Inverso de zero')

                resultado = Decimal(1) / x

            # PORCENTAGEM
            else:
                if (
                    self.operador in ('+', '-')
                    and self.acumulado is not None
                ):
                    resultado = self.acumulado * x / 100
                else:
                    resultado = x / 100

            self.display = self._formatar(resultado)

            if tecla != '+/-':
                if self.operador is None:
                    self.historico = f'{tecla}({original})'

            self.nova_entrada = False
            self.concluido = False
            return

        raise ValueError(f'Tecla não suportada: {tecla}')
