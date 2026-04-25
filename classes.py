
# Definindo uma classe chamada de Livro

class Livro:                                                # Define a classe
    def __init__(self, titulo, autor, id_livro):            # Construtor, self significa "este objeto especifico", é como se ele combinasse esses elementos para a existencia do item
        self._id_livro = id_livro                           # O underscore do começo encapsula
        self.titulo = titulo                                # Daqui em diante são as Instâncias
        self.autor = autor
        self.disponivel = True                              # Define o estado inicial

# Define um método / função = Retornando em string a saída

    def __str__(self):                                      # Os dois underscore é um método especial em que ele chama "por debaixo dos panos" e o self é a "autorização" para ele acessar a classe
        status = 'Disponível' if self.disponivel else 'Emprestado' # Aqui ele testa no if o True, e só se não for ele faz o else, esta é uma forma encurtada para : if self.disponivel == True: / status = "Disponível" / else: / status = "Emprestado"
        return f'ID: {self._id_livro}  | Livro: {self.titulo} | Autor: {self.autor} | Status: {status}'


# Instanciando / Criando um objeto dentro da classe Livro

livro_a = Livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", "001")
livro_b = Livro("Dom Casmurro", "Machado de Assis", "002")


# Acessando a classe

print(livro_a)




# Definindo uma classe chamada de Leitor

class Leitor:
    def __init__(self, id, nome):
        self._id = id
        self.nome = nome
        self.livros_emprestados = []            # A lista nasce vazia, ela não esta no init da classe, justamente porque ela nasce vazia


# Define um método para return do nome

    def __str__(self):
        return f'ID: {self._id} | Nome Cliente: {self.nome} | Livros Emprestados: {len(self.livros_emprestados)}'
    
# Instanciando

leitor_a = Leitor("001", "Ana")


print(leitor_a)
