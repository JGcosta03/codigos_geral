# Cadastrar novo paciente
class Paciente:
  def __init__(self, nome, cpf, endereco):
      self.nome = nome
      self.cpf = cpf
      self.endereco = endereco

  def __str__(self):
      return f"Paciente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"

# Sistema para gerenciar os pacientes 
class GerenciadorPacientes:
  def __init__(self):
      self.pacientes = []

  def cadastrar_paciente(self, nome, cpf, endereco):
      paciente = Paciente(nome, cpf, endereco)
      self.pacientes.append(paciente)

  def listar_pacientes(self):
      return self.pacientes

  def buscar_paciente_por_cpf(self, cpf):
      for paciente in self.pacientes:
          if paciente.cpf == cpf:
              return paciente
      return None

def menu():
  gerenciador = GerenciadorPacientes()
  while True:
      print("\nMenu:")
      print("1. Cadastrar Paciente")
      print("2. Listar Pacientes")
      print("3. Buscar Paciente por CPF")
      print("4. Sair")

      opcao = input("Escolha uma opção: ")

      try:
          if opcao == '1':
              nome = input("Nome do paciente: ")
              cpf = input("CPF do paciente: ")
              endereco = input("Endereço do paciente: ")
              gerenciador.cadastrar_paciente(nome, cpf, endereco)
          elif opcao == '2':
              pacientes = gerenciador.listar_pacientes()
              for paciente in pacientes:
                  print(paciente)
          elif opcao == '3':
              cpf = input("CPF do paciente: ")
              paciente = gerenciador.buscar_paciente_por_cpf(cpf)
              if paciente:
                  print(paciente)
              else:
                  print("Paciente não encontrado.")
          elif opcao == '4':
              print("Saindo...")
              break
          else:
              print("Opção inválida.")
      except ValueError as e:
          print(e)


if __name__ == "__main__":
  menu()
