package org.example;

import java.util.ArrayList;

public class Vendedor {
    private String id;
    private String nome;
    private String email;
    private ArrayList<Produto> listaProdutos;

    public Vendedor() {
    }

    public Vendedor(String id, String nome, String email, ArrayList<Produto> listaProdutos) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.listaProdutos = listaProdutos;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public ArrayList<Produto> getListaProdutos() {
        return listaProdutos;
    }


    //inserir produtos
    public void inserir(Produto produto) {
        this.listaProdutos.add(produto);
    }

    public void listar() {
        if (!this.listaProdutos.isEmpty()) {
            for (int i = 0; i < this.listaProdutos.size(); i++) {
                System.out.println("Item:" + i + " - Produto: " + this.listaProdutos.get(i).getNome());
            }
        } else {
            System.out.println("lista vazia");
        }
    }

    public void removerlista() {
        if (this.listaProdutos.isEmpty()) {
            System.out.println("Lista vazia");
        } else {
            this.listaProdutos.clear();
            System.out.println("Limpando lista");
        }
    }

    public void removerItemlista(String nome) {
        for (int i = 0; i < this.listaProdutos.size(); i++){
            if (nome.equals(this.listaProdutos.get(i).getNome())){
                this.listaProdutos.remove(i);
                i = 0;
            }
        // implementar rotina caso não exista o item na lista
        }
    }
}
