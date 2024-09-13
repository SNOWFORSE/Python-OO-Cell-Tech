class Celular:
    celulares = []

    def __init__(self, nome, modelo, estado):
        self.nome = nome
        self.modelo = modelo
        self.estado = estado
        self.ativo = False
        Celular.celulares.append(self)

    def __str__(self):
        return f'{self.nome} | {self.modelo} | {self.estado} | {self.ativo}'
    
    def listar_celulares():
        for celular in Celular.celulares:
            print(f'{celular.nome} | {celular.modelo} | {celular.estado} | {celular.ativo}')

celular_iPhone = Celular('iPhone','14 Pro','Novo')
celular_Xiaomi = Celular('Redmi', 'Note 13 Pro+', 'Novo')
celular_Samsung = Celular('Samsung Galaxy', 'A55', 'Novo')

Celular.listar_celulares()
