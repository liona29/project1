from flask import Flask, render_template, request, flash
from big_char import *
import psycopg2


app = Flask(__name__)
app.secret_key = "ariariari"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/bigchar", methods=["POST", "GET"])
def bigchar():
    print("###bigchar###")
    conn = psycopg2.connect(
        database="postgresdb",
        user="postgres",
        password="root",
        host="postgres"
        )
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE bigchar (str VARCHAR, ans TEXT)")
        print("CREATE TABLE bigchar")
    except:
        print("TABLE bigchar")
    print("bigchar")
    sh = "INSERT INTO "+'"bigchar"'+" (str, bigstr) VALUES (%s, %s)"
    str = request.form['name_input']
    ans = biger(str)
    val = (str, ans)
    cur.execute(sh,val)
    ans = '<html><head><title>'+str+'</title><style>body {background-color: lightblue;}</style></head><body><center><p><pre>' + ans + '</pre></center></p></body></html>'
    outfile = open('/templates/ans.html', 'w')
    outfile.write(ans)
    outfile.close()
    
    return render_template("ans.html")

@app.route("/historibigchar", methods=["POST", "GET"])
def historibigchar():
    print("####history works###")
    conn = psycopg2.connect(
        database="postgresdb",
        user="postgres",
        password="root",
        host="postgres"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+'"bigchar"') 
    ans = cur.fetchall()
    outfile = open('/templates/history.html', 'w')
    html = '<html><head><title>history</title><style>body {background-color: lightblue;}</style></head><body><center><p><pre>' + ans[0][1] + '<br><br></pre></center></p>'
    for str in ans:
        html += '<center><p><pre>' + str[1] + '<br><br></pre></center></p>'
    html += '</body></html>'
    outfile.write(html)
    return render_template("history.html")


app.run(host='0.0.0.0', port=8000)