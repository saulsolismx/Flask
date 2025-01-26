from flask import Flask, request, jsonify, url_for, redirect, session, render_template

app = Flask(__name__)

# Puedes anadir configuraciones a tu app de Flask asi:

app.config['DEBUG'] = True

#Para trabajar con sesiones usamos lo siguiente:

app.config['SECRET_KEY'] = 'ThisIsASecret!'


@app.route('/')
def index():
    name = session['name']
    return '<h1> Hello World, this is Index and this is the session {} </h1>'.format(name)


@app.route('/home', defaults={'name' : 'Default'})
@app.route('/home/<name>', methods=['POST', 'GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name = name) # Asi se hace render de un html template con variable

@app.route('/query')
def query():
    name = request.args.get('name')   
    location = request.args.get('location')
    return '<h1> Hi {}. You are from {}. And you are in the query page </h1>'.format(name, location) # http://127.0.0.1:5000/query?name=Saul&location=Florida

@app.route('/theform')
def theform():
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '<h1> Hello {}, You are from {}. And you have submitted the form successfully!'.format(name, location)

@app.route('/processjson', methods=['POST']) # Esto lo puedes hacer validar en postman
def processjson():
# Asi lo mandas en POSTMAN    
# {
#    "name" : "Saul",
#    "location" : "Mexico",
#    "randomlist" : ["one","two","three","four"]
# }
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result' : 'Success', 'name' : name, 'location': location, "randomkeyinlist" : randomlist[1] })

@app.route('/theNewform', methods=['POST','GET'])
def theNewform():
    if request.method == 'GET':
        return '''<form method="POST" action="/theNewform">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" value="submit">
                </form> '''
    else:
        name = request.form['name']
        location = request.form['location']
        return '<h1> Hello {}, You are from {}. And you have submitted the form successfully!'.format(name, location)


@app.route('/redireccionar', methods=['POST','GET'])
def redireccionar():
    if request.method == "GET":
        return '''
                <form method="POST" action="/redireccionar">
                <input type="text" name="name">
                <input type="submit" value="Redirect">
                </form>
               '''
    else:
        name = request.form['name']
        return redirect(url_for('home', name = name))


if __name__ == '__main__':
    app.run(debug=True)