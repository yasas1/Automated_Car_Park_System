using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;


namespace ParkingSystem
{
    public partial class FormParking : Form
    {
        public FormParking()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            int typeid = 0;

            string numberplate = "wpBXX-1414";

            int lenth = numberplate.Length;

            

            if (lenth == 10)
            {
                char type;
                type = numberplate[2];

                if (type == 'C' || type == 'K' || type == 'J') 
                    typeid = 1;           
                else if (type == 'B')
                    typeid = 2;
                else if (type == 'A')
                    typeid = 3;
                else
                    MessageBox.Show("Invalid vehicle Type");
                MessageBox.Show("typeid is "+typeid.ToString());
            }
            else
                MessageBox.Show("Wrong number plate detection");

            if (typeid != 0)
            {

                string conString = "server=localhost;user id=root;persistsecurityinfo=True;database=carpark";
                MySqlConnection con = new MySqlConnection(conString);
                MySqlCommand command = con.CreateCommand();             

                command.CommandText = "SELECT locationid FROM location WHERE free=1 AND vtypeid='" + typeid + "' LIMIT 1";

                try
                {
                    con.Open();
                    
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }

                MySqlDataReader reader = command.ExecuteReader();

                int loc = 0;
                 
                try {
                    reader.Read();
                    loc = Int32.Parse(reader[0].ToString());
                } catch (Exception ex)
                {
                    MessageBox.Show(ex.ToString());
                }
                con.Close();
                DateTime now = DateTime.Now;
                string stime = now.ToString("HH:mm:ss");
                string date = now.Date.ToString("yyyy-MM-dd");

                MessageBox.Show(loc.ToString());
            
                try
                {
                    command.CommandText = "insert into parking (numberplate,date,stime,locationid) values('" + numberplate + "','" + date + "','" + stime + "','" + loc + "')";
                    con.Open();
                    command.ExecuteNonQuery();
                    con.Close();
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
                
            } 
                
        }
    }
}
