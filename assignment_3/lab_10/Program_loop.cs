using System;

class tasks
{
    // Print numbers from 1 to 10
    public void PrintNumbers()
    {
        Console.WriteLine("Printing numbers from 1 to 10:");
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(i);
        }
    }

    // Ask user for input until exit and echo the input back
    public void InputUntilExit()
    {
        Console.WriteLine("\nEnter any text (type 'exit' to stop):");
        string input = "";
        while (true)
        {
            Console.Write("Input: ");
            input = Console.ReadLine();
            if (input.ToLower() == "exit")
            {
                Console.WriteLine("Exiting input loop.");
                break;
            }
            else
            {
                Console.WriteLine(input);
            }
        }
    }

    // Calculate factorial of a number
    public int CalculateFactorial(int n)
    {
        if (n < 0)
        {
            throw new ArgumentException("Factorial is not defined for negative numbers.");
        }

        int result = 1;
        for (int i = 2; i <= n; i++)
        {
            result *= i;
        }
        return result;
    }

    // Ask user for input to calculate its factorial
    public void FactorialInteraction()
    {
        Console.Write("\nEnter a number to calculate its factorial: ");
        string input = Console.ReadLine();

        if (int.TryParse(input, out int number))
        {
            try
            {
                int factorial = CalculateFactorial(number);
                Console.WriteLine($"Factorial of {number} is: {factorial}");
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid integer.");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        tasks task1 = new tasks();

        task1.PrintNumbers();
        task1.InputUntilExit();
        task1.FactorialInteraction();

    }
}
