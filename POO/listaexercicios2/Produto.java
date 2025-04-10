package listaexercicios2;

public class Produto {
    String nome;
    double preco;
    int qtdEstoque;


//Construtor

    public Produto (String nome, double preco, int qtdEstoque){
    this.nome = nome;
    this.preco = preco;
    this.qtdEstoque = qtdEstoque;
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getQtdEstoque() {
        return qtdEstoque;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void setQtdEstoque(int qtdEstoque) {
        this.qtdEstoque = qtdEstoque;
    }

    public void adicionar(int qtd){
        this.qtdEstoque = this.qtdEstoque + qtd;
    }
    
    public void remover(int qtd){
        this.qtdEstoque = this.qtdEstoque - qtd;
    }
    
    public void mostrarDetalhes(){
        System.out.println("Descricao: " + this.nome +
                " - Preco: " + this.preco +
                " - Quantidade: " + this.qtdEstoque);
    }
}