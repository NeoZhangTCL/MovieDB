from flask import  Flask, render_template, redirect, url_for, request, render_template_string, g
import mysql.connector

app = Flask(__name__)
user = 'User'

@app.route("/")
@app.route("/login")
def main():
    global user
    user = 'User'
    return render_template('login.html', tag=user)

@app.route('/register')
def registerPage():
    global user
    return render_template('register.html', tag=user)

@app.route('/login', methods=["POST"])
def login():
    global user
    email = request.form['email']
    name = request.form['user_name']
    query = (
        "SELECT FirstName, LastName FROM Customer WHERE EmailAddress = " + email + "; "
    )
    # change the return stuff to list
    user_info = list(sum(sqlprocess(query), ()))
    if len(user_info) == 0:
        error = 'Name and Email does not much.'
        return  render_template('login.html', error=error, tag=user)
    else:
        fullname = user_info[0] + ' ' + user_info[1]
        if name != fullname :
            error = 'Name and Email does not much.'
            return  render_template('login.html', error=error, tag=user)
        else:
            user = fullname
            return  redirect(url_for('userPage', username=user))

@app.route('/register', methods=["POST"])
def register():
    global user
    fName = request.form['first_name']
    lName = request.form['last_name']
    email = request.form['email']
    gender = request.form['gender']
    query = (
        "insert ignore into Customer values(0, '" + fName + "', '" + lName + "', '" + email + "', '" + gender + "');"
    )
    sqlprocess(query)
    return  render_template('user.html', tag=user)

@app.route("/movie")
def moviePage():
    global user
    query = ("SELECT * FROM Movie")
    movies = sqlprocess(query)
    return render_template('movie.html',movies=movies, tag=user)

@app.route("/showing")
def showingPage():
    global user
    query = ("SELECT * FROM Showing s LEFT OUTER JOIN Movie m ON s.Movie_idMovie = m.idMovie;")
    showings=sqlprocess(query)
    return render_template('showing.html',showings=showings, tag=user)

@app.route('/user/<username>')
def userPage(username):
    global user
    return render_template('user.html',fullname=user, tag=user)


@app.route('/user/admin')
def admin():
    pass

@app.route('/movie/<movieKey>', methods=["POST"])
def movieSortBy(movieKey):
    global user
    query =  ("SELECT * FROM Movie ORDER BY " + movieKey + "; ")
    movies = sqlprocess(query)
    return render_template('movie.html',movies=movies, tag=user)

@app.route("/showing/<showingKey>", methods=["POST"])
def showingSortBy(showingKey):
    global user
    query = ("SELECT * FROM Showing s LEFT OUTER JOIN Movie m ON s.Movie_idMovie = m.idMovie ORDER BY " + showingKey + ";")
    print(query)
    showings=sqlprocess(query)
    return render_template('showing.html',showings=showings, tag=user)

def sqlprocess(query):
    cnx = mysql.connector.connect(user='root', password='pass', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    res = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
