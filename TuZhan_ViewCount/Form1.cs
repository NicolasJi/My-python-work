using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Threading;
using System.Text;
using System.Net;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;
using System.IO;

namespace TuZhan_ViewCount
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public StreamReader streamReader;
        public HttpWebResponse response;
        public HttpWebRequest req;
        public Stream responseStream;
        public String html;
        public string myURL;
        private void URL_Click(object sender, EventArgs e)
        {

            myURL = Interaction.InputBox("请输入页面网址", "输入", "", 100, 100);

            req = (HttpWebRequest)HttpWebRequest.Create(myURL);
            req.Method = "GET";
            response = (HttpWebResponse)req.GetResponse();
            responseStream = response.GetResponseStream();
            streamReader = new StreamReader(responseStream, Encoding.UTF8);
            html = streamReader.ReadToEnd();
            myURL = "http://www.rabbitpre.com/app/viewcount?appid=";
            int pos = html.IndexOf("appid\":\"") + 8;
            while (html[pos] != '\"')
            {
                myURL += html[pos];
                pos += 1;
            }
            label3.Text = "您输入的网址为:" + myURL;

            int times = int.Parse(Interaction.InputBox("请输入次数", "输入", "", 100, 100));


            for (int i = 0; i < times; i++)
            {
                req = (HttpWebRequest)HttpWebRequest.Create(myURL);
                req.Method = "GET";
                response = (HttpWebResponse)req.GetResponse();
                label1.Text = "已访问" + (i + 1).ToString() + "次";
                Thread.Sleep(5);
                Application.DoEvents();
                responseStream = response.GetResponseStream();
                streamReader = new StreamReader(responseStream, Encoding.UTF8);
                html = streamReader.ReadToEnd();
                label1.Text = label1.Text += html;

            }
        }



        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
