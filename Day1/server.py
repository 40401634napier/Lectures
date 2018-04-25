from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def Hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/inherits/')
def Inherits():
    return render_template('base.html')

@app.route('/inherits_one/')
def Inherits_one():
    return render_template('inherit1.html')

@app.route('/inherits_two/')
def Inherits_two():
    return render_template('inherit2.html')

@app.route('/users/')
def Users():
    names=["simon",'thomas','lee','jamie','sylvester']
    return render_template('loop.html',names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1000,debug=True)
