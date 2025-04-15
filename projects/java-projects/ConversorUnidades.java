import java.util.Scanner;

public class ConversorUnidades {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Converter de (Celsius/Fahrenheit/Metros/Kilometros):");
        String deUnidade = scanner.nextLine();
        System.out.println("Converter para (Celsius/Fahrenheit/Metros/Kilometros):");
        String paraUnidade = scanner.nextLine();
        System.out.println("Valor a converter:");
        double valor = scanner.nextDouble();

        double resultado = 0;
        if (deUnidade.equalsIgnoreCase("Celsius") && paraUnidade.equalsIgnoreCase("Fahrenheit")) {
            resultado = (valor * 9/5) + 32;
        } else if (deUnidade.equalsIgnoreCase("Fahrenheit") && paraUnidade.equalsIgnoreCase("Celsius")) {
            resultado = (valor - 32) * 5/9;
        }else if(deUnidade.equalsIgnoreCase("Metros") && paraUnidade.equalsIgnoreCase("Kilometros")) {
            resultado = valor / 1000;
        }else if(deUnidade.equalsIgnoreCase("Kilometros") && paraUnidade.equalsIgnoreCase("Metros")){
            resultado = valor * 1000;
        }

        System.out.println(valor + " " + deUnidade + " = " + resultado + " " + paraUnidade);
        scanner.close();
    }
}
