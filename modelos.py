
# Definindo uma classe chamada de Livro

class Livro:                                               
    def __init__(self, titulo, autor, id_livro):            
        self._id_livro = id_livro                          
        self.titulo = titulo                                
        self.autor = autor
        self.disponivel = True                              

# Define um método / função = Retornando em string a saída

    def __str__(self):                                     
        status = 'Disponível' if self.disponivel else 'Emprestado' 
        return f'ID: {self._id_livro}  | Livro: {self.titulo} | Autor: {self.autor} | Status: {status}'


# Instanciando / Criando um objeto dentro da classe Livro

# livro_a = Livro("Pai Rico, Pai Pobre", "Robert Kiyosaki", "001")
# livro_b = Livro("Dom Casmurro", "Machado de Assis", "002")









# Definindo uma classe chamada de Leitor

class Leitor:
    def __init__(self, id, nome):
        self._id = id
        self.nome = nome
        self.livros_emprestados = []          


# Define um método para return do nome

    def __str__(self):
        return f'ID: {self._id} | Nome Cliente: {self.nome} | Livros Emprestados: {len(self.livros_emprestados)}'
    
# Instanciando

# leitor_a = Leitor("001", "Ana")

