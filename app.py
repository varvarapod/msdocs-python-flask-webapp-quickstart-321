import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():

    name = request.form.get('name')
    movies = findsimilar(name)
    if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name, movies = movies)
    else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

def findsimilar(movie):
    # call dania function
    # moviesList =  dania_code.similar(movie)
    moviesList = {'Superman', 'Minions', 'Spider Man', 'IT'}
    moviesList.add(movie)
    moviesList.add('dracula')
    return moviesList

if __name__ == '__main__':
   app.run()
