class Celular:
    nome = ''
    modelo = ''
    estado = ''
    ativo = False

celular_iPhone = Celular()
celular_Xiaomi = Celular()


celular_iPhone.nome = 'iPhone'
celular_iPhone.modelo = '13 Mini'

Celulares = [celular_iPhone, celular_Xiaomi]

print(Celulares, \n)
print(celular_iPhone , \n)
print(dir(celular_iPhone))