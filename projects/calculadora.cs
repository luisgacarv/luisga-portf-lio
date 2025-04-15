using System;

public class Calculadora {
    public static void Main(string[] args) {
        Console.WriteLine("Digite o primeiro número:");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Digite o operador (+, -, *, /):");
        char operador = Convert.ToChar(Console.ReadLine());

        Console.WriteLine("Digite o segundo número:");
        double num2 = Convert.ToDouble(Console.ReadLine());

        double resultado = 0;

        switch (operador) {
            case '+':
                resultado = num1 + num2;
                break;
            case '-':
                resultado = num1 - num2;
                break;
            case '*':
                resultado = num1 * num2;
                break;
            case '/':
                resultado = num1 / num2;
                break;
            default:
                Console.WriteLine("Operador inválido!");
                return;
        }

        Console.WriteLine($"Resultado: {resultado}");
    }
}
