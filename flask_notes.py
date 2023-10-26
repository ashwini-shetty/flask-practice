from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

if __name__=="__main__":
    app.run()





from flask import Flask
app=Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello %s!" %name

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run()





from flask import Flask
app=Flask(__name__)

@app.route("/blog/<int:postID>")
def show_blog(postID):
    return 'Blog number is %s' %postID

@app.route("/rev/<float:revNo>")
def revision(revNo):
    return 'Revision number  is %s' %revNo

@app.route("/name/<usrName>")
def show_name(usrName):
    return "User name given is: %s" %usrName

@app.route("/")
def hello():
    return "Hello World!"


if __name__=="__main__":
    app.run()





from flask import Flask
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return 'Hello Admin!'

@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello, %s you logged in as a guest user" % guest

@app.route("/usr/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
    app.run(debug = True)





from flask import Flask
app=Flask(__name__)

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" %name

@app.route("/login", method = ["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form("nm")
        return redirect(url_for('success',name = user))
    else:
        user=request.arg.get("nm")
        return redirect(url_for("success",name=user))

if __name__=="__main__":
    app.run()