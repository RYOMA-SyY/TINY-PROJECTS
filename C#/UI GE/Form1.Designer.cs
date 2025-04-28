namespace UI_GE
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            groupBox1 = new GroupBox();
            dateTimePicker1 = new DateTimePicker();
            Ignore = new Button();
            Save = new Button();
            Niveau = new TextBox();
            label10 = new Label();
            label8 = new Label();
            Prenom = new TextBox();
            label6 = new Label();
            Nom = new TextBox();
            label4 = new Label();
            CM = new TextBox();
            label1 = new Label();
            groupBox1.SuspendLayout();
            SuspendLayout();
            // 
            // groupBox1
            // 
            groupBox1.BackColor = SystemColors.MenuHighlight;
            groupBox1.Controls.Add(dateTimePicker1);
            groupBox1.Controls.Add(Ignore);
            groupBox1.Controls.Add(Save);
            groupBox1.Controls.Add(Niveau);
            groupBox1.Controls.Add(label10);
            groupBox1.Controls.Add(label8);
            groupBox1.Controls.Add(Prenom);
            groupBox1.Controls.Add(label6);
            groupBox1.Controls.Add(Nom);
            groupBox1.Controls.Add(label4);
            groupBox1.Controls.Add(CM);
            groupBox1.Controls.Add(label1);
            groupBox1.Location = new Point(12, 12);
            groupBox1.Name = "groupBox1";
            groupBox1.Size = new Size(736, 454);
            groupBox1.TabIndex = 0;
            groupBox1.TabStop = false;
            groupBox1.Text = "Gestion Etudiant";
            groupBox1.Enter += groupBox1_Enter;
            // 
            // dateTimePicker1
            // 
            dateTimePicker1.Location = new Point(268, 246);
            dateTimePicker1.Name = "dateTimePicker1";
            dateTimePicker1.Size = new Size(250, 27);
            dateTimePicker1.TabIndex = 17;
            // 
            // Ignore
            // 
            Ignore.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            Ignore.ForeColor = Color.Firebrick;
            Ignore.Location = new Point(572, 386);
            Ignore.Name = "Ignore";
            Ignore.Size = new Size(128, 62);
            Ignore.TabIndex = 16;
            Ignore.Text = "Ignore";
            Ignore.UseVisualStyleBackColor = true;
            // 
            // Save
            // 
            Save.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            Save.ForeColor = Color.Green;
            Save.Location = new Point(417, 386);
            Save.Name = "Save";
            Save.Size = new Size(128, 62);
            Save.TabIndex = 15;
            Save.Text = "Save";
            Save.TextImageRelation = TextImageRelation.TextBeforeImage;
            Save.UseVisualStyleBackColor = true;
            // 
            // Niveau
            // 
            Niveau.Location = new Point(268, 305);
            Niveau.Name = "Niveau";
            Niveau.Size = new Size(250, 27);
            Niveau.TabIndex = 13;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label10.Location = new Point(31, 305);
            label10.Name = "label10";
            label10.Size = new Size(96, 28);
            label10.TabIndex = 12;
            label10.Text = "Niveau : ";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label8.Location = new Point(31, 239);
            label8.Name = "label8";
            label8.Size = new Size(207, 28);
            label8.TabIndex = 9;
            label8.Text = "Date De Naissance : ";
            // 
            // Prenom
            // 
            Prenom.Location = new Point(268, 181);
            Prenom.Name = "Prenom";
            Prenom.Size = new Size(250, 27);
            Prenom.TabIndex = 7;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label6.Location = new Point(31, 181);
            label6.Name = "label6";
            label6.Size = new Size(102, 28);
            label6.TabIndex = 6;
            label6.Text = "Prénom : ";
            // 
            // Nom
            // 
            Nom.Location = new Point(268, 125);
            Nom.Name = "Nom";
            Nom.Size = new Size(250, 27);
            Nom.TabIndex = 4;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label4.Location = new Point(31, 125);
            label4.Name = "label4";
            label4.Size = new Size(75, 28);
            label4.TabIndex = 3;
            label4.Text = "Nom : ";
            // 
            // CM
            // 
            CM.Location = new Point(268, 73);
            CM.Name = "CM";
            CM.Size = new Size(250, 27);
            CM.TabIndex = 1;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.Location = new Point(31, 73);
            label1.Name = "label1";
            label1.Size = new Size(143, 28);
            label1.TabIndex = 0;
            label1.Text = "Code Massar :";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1081, 654);
            Controls.Add(groupBox1);
            Name = "Form1";
            Text = "Form1";
            groupBox1.ResumeLayout(false);
            groupBox1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private GroupBox groupBox1;
        private Label label1;
        private Button Ignore;
        private Button Save;
        private TextBox Niveau;
        private Label label10;
        private Label label8;
        private TextBox Prenom;
        private Label label6;
        private TextBox Nom;
        private Label label4;
        private TextBox CM;
        private DateTimePicker dateTimePicker1;
    }
}
