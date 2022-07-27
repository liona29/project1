from flask import Flask, render_template, request, flash
from big-app import *
import psycopg2

app = Flask(__name__)


@app.route("/")
def index():
	flash("what's your name?")
	return render_template("index.html")

@app.route("greet", methods=["POST", "GET"])
def greet():
    print("greet")
    str = request.form['name_input']
    ans = big_char_app.main(str)
    # flash(ans)
    # # request.form['name_input']
    ans = '<html><head><title>'+str+'</title></head><body><p><pre>' + ans + '</pre></p></body></html>'
    outfile = open('./templates/anser.html', 'w')
    outfile.write(ans)
    outfile.close()
    f = open('./templates/anser.html', 'r')
    # return render_template("index.html")
    return render_template("ans.html")

app.run(host='127.0.0.1', port=5005)