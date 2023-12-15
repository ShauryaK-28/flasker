from flask import Flask,render_template

#create a flask instance
app= Flask(__name__)

#create a route decorator
@app.route('/')

# def index():
#     return "<h1>Hello World!!</h1>"
# '''
# some filters:
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
# '''
def index():
    first_name="Shaurya"
    stuff= "This is a <strong>Bold</strong> text" #we will use a safe filter to pass this html to our webpage
    favorite_pizza = ["Pepperoni","Cheese","Mushroom",41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"),500


app.run(debug=True)