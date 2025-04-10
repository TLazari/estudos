package listaexercicios2;

public class Ponto {
    private String nome;
    private int X;
    private int Y;

    public Ponto(String nome, int X, int Y) {
        this.nome = nome;
        this.X = X;
        this.Y = Y;
    }
    //distancia real entre os dois pontos
    public double calcularDistanciaXY(Ponto a, Ponto b){
        return (float) Math.sqrt ((Math.pow((a.X - b.X),2)) + (Math.pow((a.Y - b.Y),2)));
    }
   //coeficiente angular
    public float calcularCoeficiente(Ponto a, Ponto b){
        return (float) ((b.Y - a.Y)/(b.X - a.X));
    }
}
