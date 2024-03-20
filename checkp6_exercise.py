# Definición clase
class Usuario:
  def __init__(self, username, password):
    self.username = username
    self.password = password

# Creación de objeto instanciado
user1 = Usuario("dr_zoidberg", "anchovy")

# Imprimir atributos
print(user1.username)
print(user1.password)