
package listaexercicios2;
public class Curso {
    String nome;
    String universidade;
    
    
    //Construtor
    public Curso() {
    }
    public Curso(String nome, String universidade){
        this.nome = nome;
        this.universidade = universidade;
    }
    //Métodos

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getUniversidade() {
        return universidade;
    }

    public void setUniversidade(String universidade) {
        this.universidade = universidade;
    }
    
    //metodo
    @Override
    public String toString () {
        return nome + " - " + universidade;
    }
}
    


