from flask import Flask, render_template
app = Flask (__name__)
app.secret_key= "your_secret_key"
def create_db():
    conn = sqlite.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTERGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL ,usertitle TEXT NOT NULL UNIQUE,password TEXT NOT NULL)')
    conn.commit()
    conn.close
# homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")
if __name__ == "__main__":
    app.run()

# signup-page
@app.route("/signup",methods = ['GET','POST'])
def signup():
    return render_template ("signup.html")
if request.method == "POST":
    username = request.form['username']
    usertitle = request.form['usertitle']
    password = request.form['password']


    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username,usertitle,password,)VALUES(,?,?,?,)'(username,usertitle,password))
        conn.commit
        print('signup succesfull')
        return (url_for('login'))
    except sqlite3.IntergrityError:
        flash ('user exist')
        conn.close
        return (url_for('signup'))
        


#login-page
@app.route("/login", methods = ['GET','POST'])
def login():
    render_template ('login.html')
    if request.method == 'post':
        usertitle = request.form['usertitle']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * WHERE usertitle = ?',(usertitle,))
        user = cursor.fetchone()
        if user and check_password(user[2],password):
            session['usertitle'] = usertitle
            flash('success')
            return redirect(url_for('dashboard'))
        else:
            flash ('fail')
        con.close()
    return render_template ('login.html')


        
