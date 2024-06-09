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

        string? Nome;
        double? N1, N2, N3, N4, M;

        private void btnLimparLista_Click(object sender, EventArgs e)
        {
            lstAprov.Items.Clear();
            lstReprov.Items.Clear();
            lblAprov.Text = "0";
            lblReprov.Text = "0";

        }

        private void btnLimpar_Click(object sender, EventArgs e)
        {
            txtNome.Text = "";
            txtN1.Text = "";
            txtN2.Text = "";
            txtN3.Text = "";
            txtN4.Text = "";

        }

        public Form1()
        {
            InitializeComponent();
        }

        private void btnSair_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnMedia_Click(object sender, EventArgs e)
        {

            if (txtN1.Text == "" || txtN2.Text == "" || txtN3.Text == "" || txtN4.Text == "" || txtNome.Text == "")
            {
                MessageBox.Show("Valores não preenchidos");
            }
            else
            {
                Nome = txtNome.Text;
                N1 = Convert.ToDouble(txtN1.Text);
                N2 = Convert.ToDouble(txtN2.Text);
                N3 = Convert.ToDouble(txtN3.Text);
                N4 = Convert.ToDouble(txtN4.Text);

                M = (N1 + N2 + N3 + N4) / 4;

                if (M >= 6)
                {
                    lstAprov.Items.Add(Nome + " - " + M);
                    lblAprov.Text = lstAprov.Items.Count.ToString();
                }
                else
                {
                    lstReprov.Items.Add(Nome + " - " + M);
                    lblReprov.Text = lstReprov.Items.Count.ToString();
                }

            }

        }
    }
}
