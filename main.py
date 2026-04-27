from biblioteca import Biblioteca
from modelos import Livro, Leitor


# Criando o sistema (a estante vazia), aqui temos o OBJETO, é quase fisico

minha_biblioteca = Biblioteca()


# Criando um livro

l1 = Livro("Cálculo 1", "James Stewart", "500")


# Usando o append() atarvés do nosso método

# minha_biblioteca.adicionar_livro(l1)


# Usando o for para imprimir os livros da estante

# minha_biblioteca.listar_livros()


    



# Teste, buscando um livro

resultado = minha_biblioteca.buscar_livro("999")

if resultado:
    print(f"Livro encontrado: {resultado.titulo}")
else:
    print("Livro não encontrado.")
