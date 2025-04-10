package listaexercicios2;

public class ListaExercicios2 {
    public static void main(String[] args) {
        
        // Classe PRODUTO
        // Instanciando p1 
        Produto p1 = new Produto("Banana", 10.00 , 5);
        p1.mostrarDetalhes();
        p1.setNome("Banana Prata");
        p1.adicionar(10);
        p1.remover(5);
        p1.mostrarDetalhes();
        
        
        // Classe CONTA BANCÁRIA
        // Instanciando conta01
        ContaBancaria conta01 = new ContaBancaria(001,"Thiago",0.0);
        conta01.depositar(100.0);
        conta01.sacar(150);
        System.out.println(conta01.getSaldo());
        conta01.sacar(75);
        conta01.getInfo();
        
        // Classe Aluno e Curso
        Curso cc = new Curso("Ciencia da Computacao", "UFBRA");
        Aluno aluno01 = new Aluno("Thiago","RA001",cc);
        System.out.println(aluno01.toString());
        
        
        // Classe Ponto Cartesiano
        Ponto pointA = new Ponto ("ponto A", 2, 5);
        Ponto pointB = new Ponto ("ponto B", 10, 3);
        System.out.println(pointA.calcularDistanciaXY(pointA, pointB));
        System.out.println(pointA.calcularCoeficiente(pointA, pointB));
    }
}
