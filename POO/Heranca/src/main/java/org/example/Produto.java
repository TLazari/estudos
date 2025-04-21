package org.example;

public class Produto {
    private String nome;
    private double preco;
    private String descricao;
    private Vendedor idVendedor;

    //public Produto(){}

    public Produto(String nome, double preco, String descricao,
                   Vendedor vendedor) {
        this.idVendedor = vendedor;
        this.nome = nome;
        this.preco = preco;
        this.descricao = descricao;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public void exibirDetalhes(){
        System.out.println("id: " + this.idVendedor.getId() +
                "\n->Nome: " + this.nome +
                "\n->Preco: " + this.preco +
                "\n->Descricao: " + this.descricao);
    }

    public Vendedor getIdVendedor() {
        return idVendedor;
    }

    public void setIdVendedor(Vendedor idVendedor) {
        this.idVendedor = idVendedor;
    }
}
