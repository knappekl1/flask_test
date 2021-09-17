from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


#Instantiate Flask
app = Flask(__name__)

app.config.update(
    SECRET_KEY="topsecret",
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:Liborknappek1+@localhost:5432/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

class Publication(db.Model):
    __tablename__="publication"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return f"The publisher name is:{self.name}"


class Book(db.Model):
    '''
    avg_rating = rating, float
    format = publishing format (ebook, hardcover, paperback), str
    image = link to book image, str 
    num_pages = number of pages, int
    pub_id = id of the publisher, int
    '''
    __tablename__="book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    #relationship
    pub_id = db.Column(db.Integer, db.ForeignKey("publication.id"))

    def __init__(self, title,author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id
    
    def __repr__(self):
        return f"{self.title} by {self.author}"

class Store(db.Model):
    __tablename__="store"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"))

    def __init__(self, name, inventory, book_id):
        self.name = name
        self.inventory = inventory
        self.book_id = book_id
    
    def __repr__(self):
        return f"Store {self.name} inventory is {self.inventory}"


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
    # pub = Publication(105,"Python Publishing Inc.")
    # db.session.add(pub)
    # db.session.commit()   
    return render_template("using_macros.html", movies=movies_dict)




#boilerplate
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)