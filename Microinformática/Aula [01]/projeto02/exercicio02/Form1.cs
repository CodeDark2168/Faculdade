using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace exercicio02
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnSair_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnLimpar_Click(object sender, EventArgs e)
        {
            txtN1.Clear();
            txtN2.Clear();
            lblResultado.Text = "Informe os dados acima";
            txtN1.Focus();
        }

        private void btnCalcular_Click(object sender, EventArgs e)
        {
            double N1 = 0, N2 = 0, R = 0;
            N1 = Convert.ToDouble(txtN1.Text);
            N2 = Convert.ToDouble(txtN2.Text);
            R = N1 + N2;
            lblResultado.Text = "A soma dos números é: " + R.ToString();  
        }
    }
}
