using System;

class Calculator
{
    static void Main()
    {
        PerformOperations();
    }

    static void PerformOperations()
    {
        double num1 = 0, num2 = 0;

        try
        {
            Console.WriteLine("Enter first number:");
            num1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter second number:");
            num2 = Convert.ToDouble(Console.ReadLine());
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input. Please enter valid input.");
            return;
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error occured: " + ex.Message);
            return;
        }

        double sum = Add(num1, num2);
        double diff = Subtract(num1, num2);
        double prod = Multiply(num1, num2);
        double div = 0;

        try
        {
            div = Divide(num1, num2);
        }
        catch (DivideByZeroException)
        {
            Console.WriteLine("Cannot divide by zero.");
        }

        Console.WriteLine($"Sum: {sum}");
        Console.WriteLine($"Difference: {diff}");
        Console.WriteLine($"Product: {prod}");
        Console.WriteLine($"Quotient: {div}");

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
        if (b == 0)
            throw new DivideByZeroException();
        return a / b;
    }
}
