from flask import Flask,redirect,render_template,url_for,request

app=Flask(__name__)
users={}
@app.route("/")
def welcome():
   return render_template("index.html")  
   
@app.route("/form",methods=["POST"])
def register():   
    users[request.form["name"]]={
        "name":request.form["name"],
        "age":request.form["age"],
        "place":request.form["place"]
    }
    return f"<h1>Registration Successfull</h1>"

@app.route("/alluser")
def display():
    return f'<h1>List of Users</h1> {users}'

@app.route("/<name>")
def login(name):
    return users[name]
app.run()