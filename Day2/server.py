from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('base.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=1111,debug=True)
