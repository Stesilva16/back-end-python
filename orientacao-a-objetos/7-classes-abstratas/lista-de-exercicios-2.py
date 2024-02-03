# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod

# Classe abstrata representando um cliente
class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal
    
    @abstractmethod
    def obter_cheque_especial(self):
        pass
# Subclasse de Cliente para clientes mulheres    
class ClientMulher(Cliente):
    def obter_cheque_especial(self):
        return -self.renda_mensal
    
# Subclasse de Cliente para clientes homens    
class ClienteHomen(Cliente):
    def obter_cheque_especial(self):
        return 0
    
# Classe representando uma conta corrente    
class ContaCorrente:
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []
    
    # Método para realizar depósito na conta    
    def depositar(self,valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito de R$ {valor}')
        
     # Método para realizar saque na conta, considerando o cheque especial para clientes mulheres 
    def sacar(self, valor):
        # Verifica se o saldo pós-saque não ultrapassa o cheque especial disponível para qualquer cliente
        if self.saldo - valor >= min(cliente.obter_cheque_especial() for cliente in self.clientes):
            self.saldo -=valor
            self.operacoes.append(f'Saque de R${valor}')
        else:
            print('Saque não permitido. Saldo insuficiente.')
            
#Exemplo de uso:
cliente_mulher = ClientMulher("Mary", "123456845", 5000)
cliente_homem = ClienteHomen("Juan", "987564622", 6000)

conta = ContaCorrente([cliente_mulher])
conta.depositar(1000)
conta.sacar(3000) #Saque permitido devido ao cheque especial

print(f'Saldo atual: R${conta.saldo}')
print('Operações:', conta.operacoes)