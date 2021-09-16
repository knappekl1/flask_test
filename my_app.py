from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

#Instantiate Flask
app = Flask(__name__)

app.config.update(
    SECRET_KEY="topsecret",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:Liborknappek1+@localhost:5432/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

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

@app.route("/movies")
def movies_plus():
    movies_dict = {"This is my goal":3.09, "More than this":2.5, "My stalled engine":2.2,"You and him":0.8}
    for m in movies_dict.keys():
        print(m)

    return render_template("movies2.html", movies=movies_dict, name="Sally")

@app.route("/filters")   
def filters():
    movies_dict = {"This is my goal":3.09, "More than this":2.5, "My stalled engine":2.2,"You and him":0.8, "Xmas carrol":2.4}
    return render_template("filters.html", name=None, movies=movies_dict, film="Xmas carrol")

@app.route("/macros")
def macros():
    movies_dict = {"This is my goal":3.09, "More than this":2.5, "My stalled engine":2.2,"You and him":0.8}
    return render_template("using_macros.html", movies=movies_dict)


class Publication(db.Model):
    __tablename__="publication"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"The id is: {self.id}, the name is:{self.name}"

#boilerplate
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)