from flask import Flask

app = Flask(__name__)

#from flask import Flask, render_template
#@app.route('/')
#def index():
#    return render_template('index.html')

from flask import Flask, render_template
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')