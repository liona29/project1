from flask import Flask, render_template, request, flash
from big_char import *
# import psycopg2

app = Flask(__name__)
app.secret_key = "ariariari"

@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("/bigchar", methods=["POST", "GET"])
def bigchar():
    print("bigchar")
    
    str = request.form['name_input']
    ans = biger(str)
    ans = '<html><head><title>'+str+'</title><style>body {background-color: lightblue;}</style></head><body><center><p><pre>' + ans + '</pre></center></p></body></html>'
    outfile = open('./templates/ans.html', 'w')
    outfile.write(ans)
    outfile.close()
    
    return render_template("ans.html")

app.run(host='0.0.0.0', port=8000)