# 202312 - Python 3.12.0
# 8.4 - Diferença entre Module e Package(módulo e pacote)


from packages.modulo1 import ola_mundo
from packages.modulo2 import ola_modulo_2
from packages.modulo3 import Mensagem


# variavel do modulo
print(ola_mundo)

# funcao do modulo
ola_modulo_2()

# metodo da classe do modulo
msg = Mensagem()
msg.mensagem_modulo3()



# NOTE:
# um pacote contém modulos que são relacionados entre si