import re, json
from flask import Flask, request, render_template, redirect, url_for, make_response, Response
app = Flask(__name__)

@app.route("/sum.html")
def route_sum():
    return render_template("sum.html")

@app.route("/data")
def summation(number="lackofparameter"):
    number = request.args.get("number", number)
    try:
        number = int(number)
        msg = "n = {}, \u03a3 = {}".format(number, str(int((1+number)*number/2)))
    except:
        if number == "lackofparameter":
            msg = "Lack of parameter"
        else:
            msg =  "Wrong Parameter"
    return render_template("sum.html", msg=msg)

#--------------------------------------------------------------------------------

def get_saved_data():
    try:
        data = json.loads(request.cookies.get("user"))
    except TypeError:
        data = {}
    return data

@app.route('/myName')
def route_myName():
    data = get_saved_data()
    return render_template('myName.html', saved=data)

@app.route('/trackName', methods = ['POST'])
def trackName(name=""):
    name = request.args.get("name", name) # define the route with "/trackName?<name>"
    resp = make_response(redirect(url_for("route_myName"))) # redirect to myName page
    data = get_saved_data() # gen a dict with or without content
    data.update(dict(request.form.items())) # update it
    resp.set_cookie('user', json.dumps(data)) # set cookie and named 'user'
    return resp

# @app.route('/del')
# def del_cookie():
#     res = Response('delete cookies')
#     res.set_cookie(key='user', value='', expires=0)
#     return res

app.run(debug=True, port=3000, host="localhost")
