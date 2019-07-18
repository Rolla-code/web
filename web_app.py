from flask import *
#Flask, render_template, request

app = Flask(__name__)
items=[]

@app.route('/')
def index():
    return render_template("form.html", items=items)

from flask import Flask, render_template
@app.route('/foo')
def foo(name):
    return render_template('form.html')

@app.route('/add_todo')
def add_todo():
    item = request.args.get("item")
    print(item)
    items.append(item)
    return redirect("http://localhost:5000", code=302)

@app.route('/get_todos')
def get_todos():
    resp = Response(json.dumps(items))
    resp.header['Content-Type'] = 'application/json'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')