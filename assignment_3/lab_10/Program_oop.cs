using System;

class Student
{
    // Properties
    public string Name { get; set; }
    public int ID { get; set; }
    public double Marks { get; set; }

    // Constructor
    public Student(string name, int id, double marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    // Copy Constructor
    public Student(Student other)
    {
        Name = other.Name;
        ID = other.ID;
        Marks = other.Marks;
    }

    // Get Grade
    public string GetGrade()
    {
        if (Marks >= 85) return "A";
        else if (Marks >= 70) return "B";
        else if (Marks >= 55) return "C";
        else return "D";
    }

    // Main method
    public static void Main()
    {
        Student s1 = new Student("Daksh", 22110066, 88.5);
        Console.WriteLine("Student 1 Details:");
        Console.WriteLine($"Name: {s1.Name}, ID: {s1.ID}, Marks: {s1.Marks}, Grade: {s1.GetGrade()}");

        // Using copy constructor
        Student s2 = new Student(s1);
        Console.WriteLine("\nCopied Student:");
        Console.WriteLine($"Name: {s2.Name}, ID: {s2.ID}, Marks: {s2.Marks}, Grade: {s2.GetGrade()}");
    }
}

// Sub-class
class StudentIITGN : Student
{
    // Additional Property
    public string Hostel_Name_IITGN { get; set; }

    // Constructor
    public StudentIITGN(string name, int id, double marks, string hostel) : base(name, id, marks)
    {
        Hostel_Name_IITGN = hostel;
    }

    //Own Main method
    public static void Main()
    {
        StudentIITGN s3 = new StudentIITGN("Raj", 22110489, 37, "Emiet Hostel");
        Console.WriteLine("IITGN Student Details:");
        Console.WriteLine($"Name: {s3.Name}, ID: {s3.ID}, Marks: {s3.Marks}, Grade: {s3.GetGrade()}, Hostel: {s3.Hostel_Name_IITGN}");
    }
}
