from Modelos.Celular import Celular
celular_iPhone = Celular('Apple iPhone','14 Pro','Novo')
celular_Xiaomi = Celular('Redmi', 'Note 13 Pro+', 'Novo')
celular_Samsung = Celular('Samsung Galaxy', 'A55', 'Novo')

celular_iPhone.alterar_estado()
celular_Samsung.receber_recondionamento('Paraguai', 200)
celular_Samsung.receber_recondionamento('Brasil', 1.000)
celular_Samsung.receber_recondionamento('Argentina', 192.498)

def main():
    Celular.listar_celulares()

if __name__ =='__main__':
    main()