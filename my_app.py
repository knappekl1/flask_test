from flask import Flask, request, render_template

#Instantiate Flask
app = Flask(__name__)

@app.route("/index")
#Route
@app.route("/")
#Route function
def hello_flask():
    return "Hello Flask"

@app.route("/new/")
#Request string default value in function brackets
def query_string(greeting = "Hello!"):
    #default value passed in assignment as well
    query_val = request.args.get("greeting", greeting)
    return f" <h1>The greeting is {query_val}</h1>"

#Variable in URL
@app.route("/user/")
@app.route("/user/<string:name>") #data type declaration, string by default
#route function with default value (brackets)
def no_query(name="Bobby"):
    return f"<h1>Hello {name} !</h1>"

@app.route("/number")
@app.route("/number/<int:number>")
def number(number = 666):
    return f" Your number is {number + 67}"

@app.route("/add")
@app.route("/add/<float:num1>/<float:num2>")
def add(num1=0,num2=0):
    return f"<h1>The result is {num1 + num2}</h1>"

#using templates
@app.route("/temp")
def temp():
    return render_template("hello.html")

#Jinja tempating
@app.route("/watch")
def top_movies():
    movie_list = ["This is my goal", "More than this", "My stalled engine","You and him"]
    return render_template("movies.html", movies=movie_list, name="Bobby")

#boilerplate
if __name__ == "__main__":
    app.run(debug=True)