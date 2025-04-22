using System;
using System.Threading;

namespace EventDrivenAlarm
{
    // Publisher - defines and raises an event
    public class AlarmClock
    {
        // Define delegate
        public delegate void AlarmHandler();

        // Declare event
        public event AlarmHandler raiseAlarm;

        // Check system time
        public void Start(string targetTime)
        {
            Console.WriteLine("\nWaiting for alarm time....\n");

            while (true)
            {
                string currentTime = DateTime.Now.ToString("HH:mm:ss");
                Console.WriteLine("Current Time: " + currentTime);

                if (currentTime == targetTime)
                {
                    raiseAlarm?.Invoke(); // Trigger event
                    break;
                }

                Thread.Sleep(1000);
            }
        }

        public void Ring_alarm()
        {
            Console.WriteLine("\nAlarm!!! Time matched. Please wake up.");
        }
    }

    class Program
    {
        static void Main()
        {
            Console.WriteLine("Console Alarm Clock\n");

            Console.Write("Enter target time (HH:MM:SS): ");
            string inputTime = Console.ReadLine();

            // Validate input format
            if (!DateTime.TryParseExact(inputTime, "HH:mm:ss", null, System.Globalization.DateTimeStyles.None, out _))
            {
                Console.WriteLine("Invalid time format. Please enter valid 24-hour HH:MM:SS time.");
                return;
            }

            // AlarmClock instance
            AlarmClock clock = new AlarmClock();

            // Subscribe the Ring_alarm method to the raiseAlarm event
            clock.raiseAlarm += clock.Ring_alarm;

            // Clock Starts
            clock.Start(inputTime);
        }
    }
}
