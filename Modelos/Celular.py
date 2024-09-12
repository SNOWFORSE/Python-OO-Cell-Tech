class Celular:
    def __init__(self, nome, modelo, estado):
        self.nome = nome
        self.modelo = modelo
        self.estado = estado
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.modelo} | {self.estado} | {self.ativo}'
celular_iPhone = Celular('iPhone','14 Pro','Novo' )
celular_Xiaomi = Celular('Redmi', 'Note 13 Pro+', 'Novo')
celular_Samsung = Celular('Samsung Galaxy', 'A55', 'Novo')

Celulares = [celular_iPhone, celular_Xiaomi, celular_Samsung]

print(celular_iPhone)
print(celular_Samsung)
print(celular_Xiaomi)