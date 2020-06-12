
from flask import Flask , render_template , request
app = Flask(__name__) # interface between by server and my application wsgi
import pickle
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/') # bind to an url 
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST']) # bind to an url 
def admin():
    p = request.form["y"]
    t = [[int(p)]]
    y = model.predict(t)
    return render_template("index.html", y = "Water quality index would be: \n\n" + str(y[0]))

@app.route('/user')#url
def user():
    return "hie user"

if __name__ == '__main__' :
    app.run(debug = True)
