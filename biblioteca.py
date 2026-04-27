from modelos import Livro, Leitor



# Classe Gerenciadora
# Definindo a classe biblioteca, que terá métodos

class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"Livro '{livro.titulo}' adicionado ao acervo!")

    def listar_livros(self):
        print("\n--- Acervo Atual ---")
        for livro in self.acervo:
            print(livro)

    def buscar_livro(self, id_procurado):
        for livro in self.acervo:
            if livro._id_livro == id_procurado:
                return livro
        return None
