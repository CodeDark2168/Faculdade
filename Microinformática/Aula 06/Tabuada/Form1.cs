using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Tabuada
{
    public partial class Form1 : Form
    {
        int i, n;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            AcceptButton = btnCalcular;
        }

        private void btnCalcular_Click(object sender, EventArgs e)
        {
            try
            {
                n = int.Parse(txtValor.Text);

                for(i=1; i<=10; i++)
                {
                    lstTabuada.Items.Add($"{n} x {i} = {n * i}");
                }
            }

            catch (FormatException)
            {
                MessageBox.Show("Informe o valor", "Tabuada", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception erro)
            {
                MessageBox.Show($"Occorreu um erro:{erro.Message}", "Tabuada", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
