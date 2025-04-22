namespace EventDrivenAlarmGUI
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;
        private System.Windows.Forms.TextBox textBoxTime;
        private System.Windows.Forms.Button buttonStart;
        private System.Windows.Forms.Timer timer1;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
                components.Dispose();
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.textBoxTime = new System.Windows.Forms.TextBox();
            this.buttonStart = new System.Windows.Forms.Button();
            this.timer1 = new System.Windows.Forms.Timer(this.components);

            // Text Box
            this.textBoxTime.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.textBoxTime.Location = new System.Drawing.Point(30, 30);
            this.textBoxTime.Name = "textBoxTime";
            this.textBoxTime.Size = new System.Drawing.Size(200, 29);
            this.textBoxTime.TabIndex = 0;
            this.textBoxTime.PlaceholderText = "Enter time HH:mm:ss";

            // Start Button
            this.buttonStart.Font = new System.Drawing.Font("Segoe UI", 12F);
            this.buttonStart.Location = new System.Drawing.Point(250, 30);
            this.buttonStart.Name = "buttonStart";
            this.buttonStart.Size = new System.Drawing.Size(100, 30);
            this.buttonStart.TabIndex = 1;
            this.buttonStart.Text = "Start";
            this.buttonStart.UseVisualStyleBackColor = true;
            this.buttonStart.Click += new System.EventHandler(this.buttonStart_Click);


            this.ClientSize = new System.Drawing.Size(400, 120);
            this.Controls.Add(this.textBoxTime);
            this.Controls.Add(this.buttonStart);
            this.Name = "Form1";
            this.Text = "Alarm (Color changing background)";
        }
    }
}
