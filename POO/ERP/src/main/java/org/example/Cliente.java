package org.example;

/**
 *
 * @author andre
 */
public class Cliente {
    int id;
    private String nome;
    private String email;
    private String telefone;
    private String endereço;
    private String CPF;

    public Cliente(){
        id = "05";
        nome = "Andre";
        email = "andre.samouilian2016@gmail.com";
        telefone = "12997684501";
        endereço = "ruajosedecampos";
        CPF = "45382955824";
    }

    public Cliente(int id, String nome, String email, String telefone, String endereço, String CPF) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.telefone = telefone;
        this.endereço = endereço;
        this.CPF = CPF;
    }

    /**
     *
     * @return
     */
    public int getid () {
        return id;
    }
    public String getnome () {
        return nome;
    }
    public String getemail() {
        return email;
    }
    public String gettelefone() {
        return telefone;

    }
    public String getendereço() {
        return endereço;
    }
    public String getCPF () {
        return CPF;
    }

    public void setid(int id) {
        this.id = id;
    }

    public void setnome (String nome) {
        this.nome = nome;


    }

    public void setemail(String email) {
        this.email = email;

    }

    public void settelefone(String telefone) {
        this.telefone = telefone;
    }

    public void setendereço (String endereço){
        this.endereço = endereço;

    }
    public void setCPF (String CPF) {
        this.CPF = CPF;

    }
    public void informaçao () {
        System.out.println("id");
        System.out.println("nome");
        System.out.println("email");
        System.out.println("telefone");
        System.out.println("endereço");
        System.out.println("CPF");
    }
    public String informacao () {
        return (id+","+nome+", "+email+", "+telefone+", "+endereço+","+CPF);
    }
}