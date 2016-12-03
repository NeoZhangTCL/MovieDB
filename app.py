from flask import Flask, render_template, redirect, url_for, request, render_template_string, g
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
        "SELECT FirstName, LastName FROM Customer WHERE EmailAddress = '" + email + "'; "
    )
    # change the return stuff to list
    user_info = list(sum(sqlGetter(query), ()))
    if len(user_info) == 0:
        error = 'Name and Email does not much.'
        return render_template('login.html', error=error, tag=user)
    else:
        fullname = user_info[0] + ' ' + user_info[1]
        if name != fullname:
            error = 'Name and Email does not much.'
            return render_template('login.html', error=error, tag=user)
        else:
            user = fullname
            return redirect(url_for('userPage', username=user))


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
    print(query)
    sqlSetter(query)
    user = fName + ' ' + lName
    return redirect(url_for('userPage', username=user))


###################################################


@app.route('/user/admin')
def admin():
    64337909


@app.route("/movie")
def moviePage():
    global user
    query = ("SELECT * FROM Movie")
    print("in")
    movies = sqlGetter(query)
    return render_template('movie.html', movies=movies, tag=user)


@app.route('/movie/<movieKey>', methods=["POST"])
def movieSortBy(movieKey):
    global user
    query = ("SELECT * FROM Movie ORDER BY " + movieKey + "; ")
    movies = sqlGetter(query)
    return render_template('movie.html', movies=movies, tag=user)


@app.route('/movie/addMovie', methods=["POST"])
def movieAdd():
    mName = request.form['movieName']
    mYear = request.form['relaseYear']
    query = (
        "INSERT IGNORE INTO Movie VALUES (0,'" + mName + "'," + mYear + ");"
    )
    sqlSetter(query)
    return redirect(url_for('moviePage'))


@app.route('/movie/removeMovie', methods=["POST"])
def movieRemove():
    mName = request.form['movieName']
    mID = request.form['movieID']
    query = (
        "DELETE FROM Movie WHERE idMovie=" + mID + " AND MovieName='" + mName + "';"
    )
    sqlSetter(query)
    return redirect(url_for('moviePage', username=mName))


@app.route('/movie/editMovie', methods=["POST"])
def movieEdit():
    mName = request.form['movieName']
    mID = request.form['movieID']
    mYear = request.form['relaseYear']
    query = (
        "UPDATE Movie SET MovieYear=" + mYear + ", MovieName='" +
            mName + "' WHERE idMovie = '" + mID + "';"
    )
    sqlSetter(query)
    return redirect(url_for('moviePage',username=mName))

###################################################


@app.route("/showing")
def showingPage():
    global user
    query = ("SELECT * FROM Showing s LEFT OUTER JOIN Movie m ON s.Movie_idMovie = m.idMovie;")
    showings = sqlGetter(query)
    query = ("SELECT DISTINCT Genre FROM Genre")
    genres = sqlGetter(query)
    query = ("SELECT DISTINCT ShowingDateTime FROM Showing ORDER BY ShowingDateTime")
    dates = sqlGetter(query)
    return render_template('showing.html', showings=showings, tag=user, genres=genres, dates=dates)


@app.route("/showing/<showingKey>", methods=["POST"])
def showingSortBy(showingKey):
    global user
    query = ("SELECT * FROM Showing s LEFT OUTER JOIN Movie m ON s.Movie_idMovie = m.idMovie ORDER BY " + showingKey + ";")
    showings = sqlGetter(query)
    query = ("SELECT DISTINCT Genre FROM Genre")
    genres = sqlGetter(query)
    query = ("SELECT DISTINCT ShowingDateTime FROM Showing ORDER BY ShowingDateTime")
    dates = sqlGetter(query)
    return render_template('showing.html', showings=showings, tag=user, genres=genres, dates=dates)

@app.route('/showing/search', methods=["POST"])
def showingSearch():
    global user
    query = (
        "SELECT * FROM Showing "
        "LEFT OUTER JOIN Movie "
        "ON Movie_idMovie = idMovie "
        "LEFT OUTER JOIN Genre "
        "ON idMovie = Genre.Movie_idMovie "
        "WHERE Genre = %s "
        "AND ShowingDateTime > %s "
        "AND ShowingDateTime < %s "
        "AND MovieName = %s"
    )
    data = (request.form['genre'], request.form['startDate'], request.form['endDate'], request.form['movieName'])
    showings = sqlGetter1(query, data)
    query = ("SELECT DISTINCT Genre FROM Genre")
    genres = sqlGetter(query)
    query = ("SELECT DISTINCT ShowingDateTime FROM Showing ORDER BY ShowingDateTime")
    dates = sqlGetter(query)
    return render_template('showing.html', showings=showings, tag=user, genres=genres, dates=dates)



@app.route('/showing/addShow', methods=["POST"])
def showingAdd():
    mName = request.form['movieName']
    sTime = request.form['showingTime']
    sRoom = request.form['showingRoom']
    sPrice = request.form['showingPrice']
    query = ("SELECT idMovie FROM Movie WHERE MovieName='" + mName + "';")
    mID = str(list(sum(sqlGetter(query), ()))[0])
    print(mID)
    print(type(mID))
    query = ("INSERT IGNORE INTO Showing VALUES (0, '" + sTime +
             "', " + mID + ", " + sRoom + ", " + sPrice + ");")
    print(query)
    sqlSetter(query)
    return redirect(url_for('showingPage'))


@app.route('/showing/removeShow', methods=["POST"])
def showingRemove():
    mName = request.form['movieName']
    sID = request.form['showingID']
    query = ("SELECT idMovie FROM Movie WHERE MovieName='" + mName + "';")
    mID = str(list(sum(sqlGetter(query), ()))[0])
    query = (
        "DELETE FROM Showing WHERE Movie_idMovie=" + mID + " AND idShowing=" + sID + ";"
    )
    sqlSetter(query)
    return redirect(url_for('showingPage'))


@app.route('/showing/editShow', methods=["POST"])
def showingShow():
    mName = request.form['movieName']
    query = ("SELECT idMovie FROM Movie WHERE MovieName='" + mName + "';")
    mID = sqlGetter(query)
    if (len(mID) == 0):
        return redirect(url_for('showingPage'))
    else:
        mID = str(list(sum(mID, ()))[0])
        print(mID)
        print(type(mID))
        query = (
            "UPDATE Showing SET ShowingDateTime=%s, Movie_idMovie=%s, TheatreRoom_RoomNumber=%s, TicketPrice=%s WHERE idShowing=%s"
        )
        data = (request.form['showingTime'], mID, request.form['showingRoom'], request.form['showingPrice'], request.form['showingID'])
        sqlSetter1(query, data)
        return redirect(url_for('showingPage'))

###################################################

@app.route('/<username>')
def userPage(username):
    global user
    nList = user.split(' ')
    data = (nList[0], nList[1])
    query = (
        "SELECT * FROM Customer WHERE FirstName=%s AND LastName=%s"
    )
    profile = sqlGetter1(query, data)
    sex = list(sum(profile, ()))[4].decode("utf-8")
    print(sex)
    query = (
        "select s.idShowing, m.MovieName, s.ShowingDateTime, a.Rating from "
        "Customer c left outer join Attend a on c.idCustomer = a.Customer_idCustomer "
        "left outer join Showing s on a.Showing_idShowing=s.idShowing "
        "left outer join Movie m on s.Movie_idMovie=m.idMovie "
        "where FirstName=%s and LastName=%s"
    )
    history = sqlGetter1(query, data)
    return render_template('user.html', fullname=user, tag=user, profile=profile, sex=sex, history=history)

###################################################

def isAdmin():
    global user, isAdmin
    fName = user.split(' ')[0]
    lName = user.split(' ')[1]
    query = ("SELECT isAdmin FROM Customer WHERE FirstName='" + fName + "' AND LastName='" + lName + "';")
    boo = list(sum( sqlGetter(query), ()))[0]
    isAdmin = (boo == True)
    print(isAdmin)
    return (boo == True)

def sqlGetter(query):
    cnx = mysql.connector.connect(user='jeremy', password='64337909', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    res = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return res

def sqlSetter(query):
    cnx = mysql.connector.connect(user='jeremy', password='64337909', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query)
    cnx.commit()
    cnx.close()

def sqlGetter1(query, data):
    cnx = mysql.connector.connect(user='jeremy', password='64337909', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query, data)
    res = cursor.fetchall()
    cnx.commit()
    cnx.close()
    return res

def sqlSetter1(query, data):
    cnx = mysql.connector.connect(user='jeremy', password='64337909', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    cursor.execute(query, data)
    cnx.commit()
    cnx.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
