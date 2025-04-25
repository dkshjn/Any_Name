using System;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;

namespace EventDrivenAlarmGUI
{
    public partial class Form1 : Form
    {
        private string targetTime;
        private Random random = new Random();

        public Form1()
        {
            InitializeComponent();
            timer1.Interval = 1000; // 1 second
            timer1.Tick += timer1_Tick;
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            // Check time format
            if (!DateTime.TryParseExact(textBoxTime.Text, "HH:mm:ss", CultureInfo.InvariantCulture,
                                        DateTimeStyles.None, out _))
            {
                MessageBox.Show("Invalid time format. Please enter valid 24-Hour HH:MM:SS time.");
                return;
            }

            targetTime = textBoxTime.Text;
            timer1.Start();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string currentTime = DateTime.Now.ToString("HH:mm:ss");

            if (currentTime == targetTime)
            {
                timer1.Stop();
                MessageBox.Show("Alarm!!! Time matched. Please wake up.");
            }
            else
            {
                // Change background color
                this.BackColor = Color.FromArgb(random.Next(256), random.Next(256), random.Next(256));
            }
        }
    }
}
