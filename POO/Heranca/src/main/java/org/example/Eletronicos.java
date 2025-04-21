package org.example;

public class Eletronicos extends Produto {
    private String marca;
    private String modelo;


    public Eletronicos(String nome, double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
    }

    public Eletronicos(String marca, String modelo, String nome,
                       double preco, String descricao, Vendedor vendedor) {
        super(nome, preco, descricao, vendedor);
        this.marca = marca;
        this.modelo = modelo;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public void exibirDetalhes(){
        super.exibirDetalhes();
        System.out.println("->Marca: " + this.marca +
                "\n->Modelo: " + this.modelo + "\n");
    }

}
