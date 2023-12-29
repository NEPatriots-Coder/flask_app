from flask import Flask, jsonify, request, url_for, redirect, session
# Initialize the app and configure Debug mode and setting a secretkey for the session.
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
# Defines the index page of the app and removes the 'name' key from the session and returns a fun HTML response.
@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello, World!</h1>'
# Defining a dynamic route and a default route.
# The home function sets the 'name' key in the session and returns a greeting.
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])

def home(name):
    session['name'] = name
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

# Define a json route that returns a json response containing a dictionary and a list.
@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = "NotInSession"

 # We make a query route that retrieves the query parameters(name & location)
 # and returns an HTML response.
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)

@app.route('/theform', methods=['GET', 'POST'])
# A very simple form route. Handles both GET & POST requests.
# GET request returns and HTML form
# POST request; processess the form sets the name in the session and redirects to the home route.
def theform():

    if request.method == 'GET':
        return '''<form method="POST" action="/theform">
                      <input type="text" name="name">
                      <input type="text" name="location">
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        name = request.form['name']
        #location = request.form['location']

        #return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)
        return redirect(url_for('home', name = name))
'''
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)
'''

@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})

if __name__ == '__main__':
    app.run()


