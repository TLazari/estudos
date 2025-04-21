package org.example;

public class Vestuario extends Produto {
    private String marca;
    private double tamanho;
    private String cor;

    public Vestuario(String nome, double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
    }

    public Vestuario(String marca, double tamanho, String cor,
                     String nome, double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
        this.marca = marca;
        this.tamanho = tamanho;
        this.cor = cor;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public double getTamanho() {
        return tamanho;
    }

    public void setTamanho(double tamanho) {
        this.tamanho = tamanho;
    }

    @Override
    public void exibirDetalhes(){
        super.exibirDetalhes();
        System.out.println("->Marca: " + this.marca +
                "\n->Tamanho: " + this.tamanho +
                "\n->Cor: " + this.cor + "\n");
    }
}
