class Celular:
    celulares = []

    def __init__(self, nome, modelo, estado):
        self.nome = nome
        self.modelo = modelo
        self.estado = estado
        self._ativo = False
        Celular.celulares.append(self)

    def __str__(self):
        return f'{self.nome} | {self.modelo} | {self.estado} | {self.ativo}'
    
    def listar_celulares():
        print(''' 
▒█▀▀█ █▀▀ █░░ █░░ 　 ▀▀█▀▀ █▀▀ █▀▀ █░░█ 　 ▒█▀▀▀ █░░ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀▄ ░▀░ █▀▀ █▀▀█ █▀▀ 
▒█░░░ █▀▀ █░░ █░░ 　 ░▒█░░ █▀▀ █░░ █▀▀█ 　 ▒█▀▀▀ █░░ █▀▀ ░░█░░ █▄▄▀ █░░█ █░░█ ▀█▀ █░░ █░░█ ▀▀█ 
▒█▄▄█ ▀▀▀ ▀▀▀ ▀▀▀ 　 ░▒█░░ ▀▀▀ ▀▀▀ ▀░░▀ 　 ▒█▄▄▄ ▀▀▀ ▀▀▀ ░░▀░░ ▀░▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀
''')
        print(f'{"Nome do Celular".ljust(18)} | {"Modelo do Celular".ljust(18)} | {"Estado do Celular".ljust(18)} | {"Ativo"}')
        print('--------------------------------------------------------------------------------------------')
        for celular in Celular.celulares:
            print(f'{celular.nome.ljust(18)} | {celular.modelo.ljust(18)} | {celular.estado.ljust(18)} | {celular.ativo}')
        print('--------------------------------------------------------------------------------------------')

    @property
    def ativo(self):
        return '☑ O celular está ativo' if self._ativo else '☒ O celular não está ativado'

celular_iPhone = Celular('iPhone','14 Pro','Novo')
celular_Xiaomi = Celular('Redmi', 'Note 13 Pro+', 'Novo')
celular_Samsung = Celular('Samsung Galaxy', 'A55', 'Novo')

Celular.listar_celulares()
