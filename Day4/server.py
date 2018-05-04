from flask import Flask , g, render_template, request, jsonify
import sqlite3, json
from flask import Flask
app = Flask(__name__)
db_location = 'sqlite3.db'

def get_db():
    db = getattr(g, 'db', None )
    if db is None :
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr (g, 'db', None )
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save",methods=['GET','POST'])
def save():
    print('Saving Music Album', request.method)
    error = ''
    if request.method == 'POST':
        try:
            print(request.form)
            title = request.form['title']
            artist = request.form['artist']
            media = request.form['media']
        except ValueError:
            error = 'data input error'
            return render_template("index.html", error = error)
        try:
            with sqlite3.connect("sqlite3.db") as con:
                cur = con.cursor()
                cur.execute("insert into albums(title, artist, media_type) values(?,?,?)",(title,artist,media))
                con.commit()
                msg = "saving"
        except:
            con.rollback()
        return render_template("index.html",error=error)

@app.route("/allAlbum")
def show():
    error = ''
    con = sqlite3.connect("sqlite3.db")
    cur = con.cursor()
    cur.execute("select * from albums")
    rows = cur.fetchall()
    print(rows)
    return json.dumps(rows)

if __name__ == "__main__":
    app.run( host ="0.0.0.0", debug = True )
