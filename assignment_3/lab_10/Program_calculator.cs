using System;

class Calculator
{
    static void Main()
    {
        PerformOperations();
    }

    static void PerformOperations()
    {
        Console.WriteLine("Enter first number:");
        double num1 = Convert.ToDouble(Console.ReadLine());

        Console.WriteLine("Enter second number:");
        double num2 = Convert.ToDouble(Console.ReadLine());

        double sum = Add(num1, num2);
        double diff = Subtract(num1, num2);
        double prod = Multiply(num1, num2);
        double div = Divide(num1, num2);

        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {diff}");
        Console.WriteLine($"Product: {prod}");

        if (num2 != 0)
            Console.WriteLine($"Quotient: {div}");
        else
            Console.WriteLine("Cannot divide by zero.");

        // Even-Odd (If-Else)
        if (sum % 2 == 0)
        {
            Console.WriteLine("The sum is even.");
        }
        else
        {
            Console.WriteLine("The sum is odd.");
        }
    }

    static double Add(double a, double b)
    {
        return a + b;
    }

    static double Subtract(double a, double b)
    {
        return a - b;
    }

    static double Multiply(double a, double b)
    {
        return a * b;
    }

    static double Divide(double a, double b)
    {
        return b != 0 ? a / b : double.NaN;
    }
}
