using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace projeto01
{
    public partial class Form1 : Form
    {

        double? N1, N2, R;

        private void btnSub_Click(object sender, EventArgs e)
        {

            if (txtN1.Text == "" || txtN2.Text == "")
            {
                lblResult.Text = "Campo não preenchido";
            }
            else
            {
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);

                R = N1 - N2;
                lblResult.Text = "Resultado: " + R.ToString();
            }

        }

        private void btnMult_Click(object sender, EventArgs e)
        {
            if (txtN1.Text == "" || txtN2.Text == "")
            {
                lblResult.Text = "Campo não preenchido";
            }
            else
            {
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);

                R = N1 * N2;
                lblResult.Text = "Resultado: " + R.ToString();
            }

        }

        private void btnDiv_Click(object sender, EventArgs e)
        {
            if (txtN1.Text == "" || txtN2.Text == "")
            {
                lblResult.Text = "Campo não preenchido";
            }
            else
            {
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);

                if (N2 == 0)
                {
                    lblResult.Text = "Não existe divisão por 0";
                }
                else
                {
                    R = N1 / N2;
                    lblResult.Text = "Resultado: " + R.ToString();
                }
            }

        }


        private void btnResto_Click(object sender, EventArgs e)
        {
            if (txtN1.Text == "" || txtN2.Text == "")
            {
                lblResult.Text = "Campo não preenchido";
            }
            else
            {
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);

                R = N1 % N2;
                lblResult.Text = "Resultado: " + R.ToString();
            }

        }

        private void btnLimpar_Click(object sender, EventArgs e)
        {

            txtN1.Text = "";
            txtN2.Text = "";
            lblResult.Text = "Resultado: ";

        }

        private void btnSair_Click(object sender, EventArgs e)
        {

            Close();

        }

        public Form1()
        {
            InitializeComponent();

        }

        private void btnAdc_Click(object sender, EventArgs e)
        {

            if (txtN1.Text == "" || txtN2.Text == "")
            {
                lblResult.Text = "Campo não preenchido";
            }
            else
            {
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);

                R = N1 + N2;
                lblResult.Text = "Resultado: " + R.ToString();
            }

        }
    }
}
