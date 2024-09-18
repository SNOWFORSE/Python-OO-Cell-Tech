from Modelos.recondicionamento import Recondicionamento

class Celular:
    celulares = []

    def __init__(self, nome, modelo, estado):
        self._nome = nome.upper()
        self._modelo = modelo.title()
        self.estado = estado
        self._ativo = False
        self._recondicionamento = []
        self._estado = []
        self._porcentagem = []
        Celular.celulares.append(self)

    def __str__(self):
        return f'{self._nome} | {self._modelo} | {self.estado} | {self.ativo}'
    
    @classmethod
    def listar_celulares(cls):
        print(''' 
▒█▀▀█ █▀▀ █░░ █░░ 　 ▀▀█▀▀ █▀▀ █▀▀ █░░█ 　 ▒█▀▀▀ █░░ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ ░▀░ █▀▀ █▀▀█ █▀▀ 
▒█░░░ █▀▀ █░░ █░░ 　 ░▒█░░ █▀▀ █░░ █▀▀█ 　 ▒█▀▀▀ █░░ █▀▀ ░░█░░ █▄▄▀ █░░█ █░░█ ▀█▀ █░░ █░░█ ▀▀█ 
▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░▒█░░ ▀▀▀ ▀▀▀ ▀░░▀ 　 ▒█▄▄▄ ▀▀▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀
''')
        print(f'{"Nome do Celular".ljust(18)} | {"Modelo do Celular".ljust(18)} | {"Estado do Celular".ljust(18)} | {"Ativo".ljust(18)}')
        print('----------------------------------------------------------------------------------------------------------------')
        for celular in cls.celulares:
            print(f'{celular._nome.ljust(18)} | {celular._modelo.ljust(18)} | {celular.estado.ljust(18)} | {celular.ativo.ljust(40)} | {str(celular.media_porcentagem).ljust(18)}')
        print('----------------------------------------------------------------------------------------------------------------')

    @property
    def ativo(self):
        return '☑ O celular está ativo' if self._ativo else '☒ O celular não está ativado'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_recondionamento(self, estado, porcentagem):
        recondicionamento = Recondicionamento(estado, porcentagem)
        self._recondicionamento.append(recondicionamento)

    @property
    def media_porcentagem(self):
        if not self._recondicionamento:
            return 0 
        soma_das_porcentagens = sum(recondicionamento._porcentagem for recondicionamento in self._recondicionamento)
        quantidade_celular = len(self._recondicionamento)
        media = round(soma_das_porcentagens/quantidade_celular, 1)
        return media 