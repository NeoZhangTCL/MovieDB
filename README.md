# MovieBox

##Prerequest
 * python3
 * python3-pip: sudo apt install python3-pip
 * virtualenv: sudo pip3 install virtualenv
 * mysql-server: sudo apt install mysql-server

##Run
 1. activate the virtualenv: sudo ./env/bin/activate
 2. install the enviroment: sudo pip3 install -r /path/to/requirements.txt
 3. import the db.sql: mysql -u root -p --verbose < /path/to/prject/folder/db.sql
 4. execute "python3 app.py" to run the website
 5. ctrl+d to quit and deactivate to quite virtualenv

##Note
 * in app.py, there exists at the bottom sqlGetter, sqlSetter, sqlGetter1, sqlSetter1 methods which current have:<br>
        user: "root"<br>
        password: "pass"<br>
        database: "MovieTheatre"<br>
They can be changed to the desired value for access to the database.

 * PLEASE REGISTER AN SUPER USER (STAFF) IN THE USER TAB USING THE FOLLOWING ATTRIBUTE:<br>
        First Name: Super<br>
        Last Name: User<br>
        Email: \<anything\><br>
        Gender: \<anything\><br>

## Meet
The staff who work at a theatre must be able to:

    Movies  
        Upon entering the website, movies can be added, removed, or modified by clicking the movie tab on the navigation bar and going to the side bar on the right. Movies are displayed in database order initially, however, can be sorted by ID, Movie Name or Released Year by clicking on the tag. 
    Genres:
        Genres are displayed in the Genre tab and are already sorted in alphabetical order using Genre.
    Rooms:
        A list of rooms along with their capacity can be seen when logged onto the Super User by clicking on the Room tab on the navigation bar.
    Showings
        Same as Movies tab.
    Customer
         A list of customers can be seen when logged onto Super User account, the attributes can also be sorted by clicking on the column header. On the right side, the super user can add, remove, or modify customers. 
    Attend
         A list of attendances can be seen when logged onto Super User account, the attributes can also be sorted by clicking on the column header. 
Part 2: The Front End (45%):

The customers of the theatre must be able to:

NOTE: PLEASE REGISTER A NORMAL USER WITH THE DESIRED ATTRIBUTES

    allow a customer to search all the showings by searching (give a warning if there are no seats left for a showing):
        Upon logging into the customer's account, the customer will can click on the showing tab in navigation bar and on the right side bar, click search to perform a search based on Genre, Start and End Date, as well as Movie name and Availability.

    allow a customer to attend a showing
        Same as above, however, click on Buy Ticket on the right side bar instead. Select the Showing, Name, and confirm the price of the showing to purchase
    allow a customer to rate a showing
        Click their name on the navigation bar and select Rating on the right side bar. The user will be able to select all the existing showings they have attended and give a rating to it.
    allow a customer to select their name and see all the movie titles and ratings for the movies he/she has viewed
        Log in to the customer's account and click the customer's name on the navigation bar to see all the showings the particular customer have seen.
    allow a customer to select their name and see his/her profile (all the info about the customer)
        Log in to the customer's account and click the customer's name on the navigation bar to see the particular customer's profile.

Vulnerable
        Vulnerability can be shown by doing on running the second python file named vulnerability.py. Select search on the right side bar and enter 'or 1=1 # as the movie name and click search. This will display all of the movies in the database despite the filters. This is an SQL injection attack.
