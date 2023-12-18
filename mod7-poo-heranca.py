# 202312 - Python 3.12.0
# 7.6 - Herança Simples - Reutilizando outras classes


# NOTE:
# 7 - Herança multinível:
# Evitar heranças encadeadas de varios niveis pois isso aumenta a complexidade 
# do codigo e dificulta a manutencao e a compreensao das funcionalidades do 
# codigo.


class Camera:
    def __init__(self, marca, megapixels):
        self.marca = marca
        self.megapixels = megapixels

    def tirar_foto(self):
        print(f'1. mãe: Foto tirada com {self.marca}, qualidade {self.megapixels}')

    def ligar_camera(self):
        print(f'1. mãe: Ligando camera {self.marca}')

    def desligar_camera(self):
        print(f'1. mãe: Desligando camera {self.marca}')

# herança 1 nivel
class CameraCelular(Camera):
    def __init__(self, marca, megapixels, quantidade_de_cameras):
        super().__init__(marca, megapixels)
        self.quantidade_de_cameras = quantidade_de_cameras

    # filtro é uma variavel local, por isso nao tem o "self"
    def aplicar_filtro(self, filtro):
        print(f'1. filha: Aplicando filtro {filtro}')

    # alterando método da classe mãe
    def tirar_foto(self, tipo_de_camera):
        print(f'1. filha: Foto tirada com {self.marca}, qualidade {self.megapixels}, tipo de camera {tipo_de_camera}')


# instancia da classe filha
camera_celular = CameraCelular('sony', '25mp', 4)

# metodo da classe mãe
camera_celular.ligar_camera()

# metodo da classe filha
camera_celular.aplicar_filtro('sépia')

# metodo da classe mãe
camera_celular.tirar_foto('grande angular')


print()


# testando somente a classe mãe
camera_full_frame = Camera('canon', '25mp')
camera_full_frame.ligar_camera()
camera_full_frame.tirar_foto()
camera_full_frame.desligar_camera()


print()


# verificando se uma classe filha tem relação com uma classe mãe indicadas
print(f'1. é filha? {issubclass(CameraCelular, Camera)}')
