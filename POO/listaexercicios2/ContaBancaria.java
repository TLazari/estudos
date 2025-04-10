package listaexercicios2;

public class ContaBancaria {
    private int numeroConta;
    private String nomeTitular;
    private double saldo;

    //Construtor
    public ContaBancaria (){}
    
    public ContaBancaria (int numeroConta, String nomeTitular, double saldo){
        this.numeroConta = numeroConta;
        this.nomeTitular = nomeTitular;
        this.saldo = saldo;
    }
    
    // Métodos
    
    public void depositar(double valor){
        this.saldo = this.saldo + valor;
    }
    public void sacar(double valor){
        if (valor < this.saldo) {
            this.saldo = this.saldo - valor;
        }else {
            System.out.println("Tentando sacar: "+ valor +"\nSaldo invalido");
        }
    }
    public double getSaldo() {
        return this.saldo;
    }
    public void getInfo() {
        System.out.println("Titular: " + nomeTitular 
                + "\nConta: " + numeroConta
                + "\nSaldo: " + saldo);
    }
    
}