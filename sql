create view temp as select Showing_idShowing 'showID', count(Customer_idCustomer) 'countAttend' from Attend a right outer join Showing s on a.Showing_idShowing=s.idShowing group by Showing_idShowing;
select idShowing, ShowingDateTime, Capacity,countAttend from temp t left outer join Showing s on t.showID=s.idShowing left outer join TheatreRoom th on s.TheatreRoom_RoomNumber=th. RoomNumber;

