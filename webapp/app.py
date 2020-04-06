from flask import Flask, render_template

app = Flask(__name__)

@app.route('/smart-alerts')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('pasteries.html') 

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
