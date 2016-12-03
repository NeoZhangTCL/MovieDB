select s.idShowing, m.MovieName, s.ShowingDateTime, a.Rating from 
Customer c left outer join Attend a on c.idCustomer = a.Customer_idCustomer 
left outer join Showing s on a.Showing_idShowing=s.idShowing 
left outer join Movie m on s.Movie_idMovie=m.idMovie 
where FirstName='Will' and LastName='Beldman';


find a customer Id from customer name:
select idCustomer from Customer where FirstName = %s ANd LastName = %s

Find a showing id from showing time:
select idShowing from Showing left outer join Attend on idShowing = Showing_idShowing where ShowingDateTime = '2016-02-11 21:00:00';

allow a customer to attend a showing
select their name and any showing, and "buy" a ticket for it (ie. insert a new entry in the Attend table):

insert into Attend (Customer_idCustomer, Showing_idShowing, Rating) values (%s, %s, %s);





Find a showing id from showing time:
select idShowing from Showing left outer join Attend on idShowing = Showing_idShowing where ShowingDateTime = '2016-02-11 21:00:00'; (use %s)

Find a customerId from customer name:
select idCustomer from Customer where FirstName = %s ANd LastName = %s

Rate a showing based on customerId and showingId
insert into Attend (Customer_idCustomer, Showing_idShowing, Rating) values (%s, %s, %s)
