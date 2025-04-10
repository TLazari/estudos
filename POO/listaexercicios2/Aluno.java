package listaexercicios2;

public class Aluno {
    private String nome;
    private String ra;
    private Curso curso;
    // Construtor
    public Aluno (String nome, String ra, Curso curso){
        this.nome = nome;
        this.ra = ra;
        this.curso = curso;
    }
    public Aluno (){
    }
    
    //Método
    @Override
    public String toString () {
        return nome + " - " + ra + " - " + curso.toString();
    }
    
}


