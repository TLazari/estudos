package org.example;

public class Livro extends Produto {
    private String autor;
    private int numPaginas;
    private Vendedor idVendedor;

    public Livro(String nome, double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
    }

    public Livro(String autor, int numPaginas, String nome,
                 double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
        this.autor = autor;
        this.numPaginas = numPaginas;
    }

    public int getNumPaginas() {
        return numPaginas;
    }

    public void setNumPaginas(int numPaginas) {
        this.numPaginas = numPaginas;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    @Override
    public void exibirDetalhes() {
        super.exibirDetalhes();
        System.out.println("->Autor: " + this.autor +
                "\n->Num.Paginas: " + this.numPaginas + "\n");
    }

}
