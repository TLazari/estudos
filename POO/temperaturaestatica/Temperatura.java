package temperaturaestatica;
public class Temperatura {
    public static double calculaFahreinheit(double celsius){
        return (celsius * 9/5) + 32;
    }
    
    public static double calculaKelvin(double celsius){
        return celsius + 273.15;
    }
}
