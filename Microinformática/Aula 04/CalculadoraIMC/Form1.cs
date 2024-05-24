using System;
using System.Windows.Forms;

namespace CalculadoraIMC
{
    public partial class Form1 : Form
    {
        double alt, pes, imc;
        string nome, sexo, cat;
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
            txtNome.Text = "";
            txtAltura.Text = "";
            txtPeso.Text = "";
            lstHomens.Items.Clear();
            lstMulheres.Items.Clear();
        }

        private void btnCalcular_Click(object sender, EventArgs e)
        {
            try
            {
                alt = double.Parse(txtAltura.Text);
                pes = double.Parse(txtPeso.Text);
                nome = txtNome.Text;
                sexo = cmbSexo.Text;

                imc = pes / (alt * alt);

                txtNome.Text = sexo;

                if (imc < 18.5)
                {
                    cat = "Abaixo do Peso";
                }
                else if (imc >= 18.5 && imc < 25)
                {
                    cat = "Normal";
                }
                else if (imc >= 25 && imc < 30)
                {
                    cat = "Sobrepeso";
                }
                else
                {
                    cat = "Obesidade";
                }

                if (sexo == "Masculino")
                {
                    lstHomens.Items.Add($"{nome} {imc:F2} - {cat}");
                }

                else if (sexo == "Feminino")
                {
                    lstMulheres.Items.Add($"{nome} {imc:F2} - {cat}");
                }

                else
                {
                    MessageBox.Show("Informe o sexo", "IMC", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (FormatException)
            {
                MessageBox.Show("Informe os valores", "IMC", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception erro)
            {
                MessageBox.Show($"Occorreu um erro:{erro.Message}", "IMC", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
