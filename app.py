import os

from flask import (Flask, jsonify, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

# Sample data (replace with your actual data source)
books = [
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"},
]

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
   name = request.form.get('name') + " response"

   if name:
       print('Request for hello page received with prompt=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no prompt or blank prompt -- redirecting')
       return redirect(url_for('index'))
   


@app.route("/api/books", methods=["GET"])
def get_books():
  """Returns a JSON list of all books"""
  return jsonify(books)



if __name__ == '__main__':
   app.run()
