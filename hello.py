from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')
# def user(name):
#     return "<h1>{} loves Vinoth</h1>".format(name)
def user(name):
    pizza=["peperoni","cheese",41]
    text="   this is <strong>bold</strong> text    "
    return render_template("user.html", name=name, text=text, pizza=pizza)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")




