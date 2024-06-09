using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exercicio01
{
    class Program
    {
        static void Main(string[] args)
        {
            double n1 = 0, n2 = 0, r = 0;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Informe o primero valor:");
            n1 = Convert.ToDouble(Console.ReadLine());
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("Informe o segundo valor:");
            n2 = Convert.ToDouble(Console.ReadLine());
            r = n1 + n2;
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("O resultado da operação é:");
            Console.Write(n1+" + "+n2+" = "+r.ToString());
            Console.ReadKey();
        }
    }
}
