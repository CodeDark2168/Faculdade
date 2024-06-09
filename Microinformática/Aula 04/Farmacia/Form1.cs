using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Projeto01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void bntSair_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void bntCalcular_Click(object sender, EventArgs e)
        {
            string nome = "";
            double valorCompra = 0;

            if (!double.TryParse(txtValorCompra.Text, out valorCompra))
            {
                MessageBox.Show("Informe um valor válido", "Atenção", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            double descontoFaixa = 0;

            if (rbtn1.Checked)
            {
                descontoFaixa = 0;
            }
            else if (rbtn2.Checked)
            {
                descontoFaixa = 0.05;
            }
            else if (rbtn3.Checked)
            {
                descontoFaixa = 0.07;
            }
            else
            {
                MessageBox.Show("Marque uma faixa etária", "Atenção", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            double descontoCartao = 0;

            if (chkCartao.Checked)
            {
                descontoCartao = 0.05; 
            }

            double valorDescontoIdade = valorCompra * descontoFaixa;
            double valorDescontoCartao = valorCompra * descontoCartao;
            double valorFinal = valorCompra - valorDescontoIdade - valorDescontoCartao;

            lblValorFinal.Text = "Valor da compra: R$" + Math.Round(valorCompra, 2) + "\nDesconto Faixa: R$" + Math.Round(valorDescontoIdade, 2) + "\nDesconto Cartão: R$" + Math.Round(valorDescontoCartao, 2) + "\nValor Final: R$" + Math.Round(valorFinal, 2);
        }

        private void bntLimpar_Click(object sender, EventArgs e)
        {
            txtNome.Text = "";
            txtValorCompra.Text = "";
            lblValorFinal.Text = "";
            chkCartao.Checked = false;
            rbtn1.Checked = false;
            rbtn2.Checked = false;
            rbtn3.Checked = false;
        }
    }
}
