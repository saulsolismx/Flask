from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/home', defaults={'name' : 'Default'})
@app.route('/home/<name>', methods=['POST', 'GET'])
def home(name):
    return '<h1> Hello {}! </h1>'.format(name)

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1> Hi {}. You are from {}. And you are in the query page </h1>'.format(name, location) # http://127.0.0.1:5000/query?name=Saul&location=Florida

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="submit">
              </form> '''

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '<h1> Hello {}, You are from {}. And you have submitted the form successfully!'.format(name, location)

@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result' : 'Success', 'name' : name, 'location': location, "randomkeyinlist" : randomlist[1] })


if __name__ == '__main__':
    app.run(debug=True)