from flask import  Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)
user = None


@app.route("/")
def main():
    renderMovie()
    return render_template('index.html', user_tag='User')

def renderMovie():
    cnx = mysql.connector.connect(user='root', password='pass', database='MovieTheatre')
    cursor = cnx.cursor()
    query = ("SELECT * FROM Movie")
    cursor.execute(query)
    movies=cursor.fetchall()
    cnx.close()
    return render_template('pages/movie.html', movies=movies)

def renderTheatre():
    pass

def renderUser():
    pass

@app.route('/login', methods=["POST"])
def login():
    cnx = mysql.connector.connect(
        user='root', password='pass', database='MovieTheatre')
    cursor = cnx.cursor(buffered=True)
    email = request.form['email']
    name = request.form['user_name']
    login_query = (
        "SELECT FirstName, LastName FROM Customer WHERE EmailAddress = '" + email + "' "
    )
    cursor.execute(login_query)
    # change the return stuff to list
    user_info = list(sum(cursor.fetchall(), ()))
    if len(user_info) == 0:
        cnx.commit()
        cnx.close()
        error = 'Name and Email does not much.'
        return  render_template('index.html', error=error, user_tag='User')
    else:
        fullname = user_info[0] + ' ' + user_info[1]
        if name != fullname :
            cnx.commit()
            cnx.close()
            error = 'Name and Email does not much.'
            return  render_template('index.html', error=error, user_tag='User')
        else:
            cnx.commit()
            cnx.close()
            return  render_template('index.html', user_tag=name)

@app.route('/user/<username>')
def user(username):
    pass

@app.route('/user/admin')
def admin():
    pass




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
