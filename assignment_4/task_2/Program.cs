using System;
using System.Windows.Forms;
using EventDrivenAlarmGUI;

namespace EventDrivenAlarmGUI
{
    internal static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}