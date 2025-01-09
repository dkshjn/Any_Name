"""
This script demonstrates basic operations on a list of numbers.
"""
def find_average(numbers):
    """
    Calculate the average of a list of numbers.
    """
    total = sum(numbers)
    return total / len(numbers)

def filter_even(numbers):
    """
    Filter and return a list of even numbers from the input list.
    """
    even = []
    for num in numbers:
        if num%2==0:
            even.append(num)
    return even

def main():
    """
    Main function to demonstrate basic operations on a list of numbers.
    """
    print("Hello. We will be learning some basic functions today.\n")

    # Input: List of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display original numbers
    print("Original numbers:")
    print(numbers)

    # Calculate and display the average
    avg = find_average(numbers)
    print(f"\nAverage of numbers: {avg}")

    # Filter and display even numbers
    even_numbers = filter_even(numbers)
    print("\nEven numbers:")
    print(even_numbers)

if __name__ == "__main__":
    main()
