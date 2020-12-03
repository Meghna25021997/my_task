                                       Steps to run code
1)Create Mysql database
-create database project;
Create Table
create table movie_details(
name varchar(50),
img varchar(30),
summary varchar(500)
);
Insert Values into Table
insert into movie_details values
("Harry Potter and the Order of the Phoenix ",
"https://bit.ly/2IcnSwz",
"Harry Potter and Dumbledore's warning about the return of Lord Voldemort is
not heeded by the wizard authorities who in turn look to undermine Dumbledore's
authority at Hogwarts and discredit Harry"
);
insert into movie_details values
("The Lord of the Rings: The Fellowship of the Ring",
"https://bit.ly/2tC1Lcg",
"A young hobbit, Frodo, who has found the One Ring that belongs to the Dark
Lord Sauron, begins his journey with eight companions to Mount Doom, the only
place where it can be destroyed."
);
insert into movie_details values
("Avengers: Endgame",
"https://bit.ly/2Pzczlb",
"Adrift in space with no food or water Tony Stark sends a message to Pepper
Potts as his oxygen supply starts to dwindle. the remaining Avengers Thor, Black
Widow, Captain America and Bruce Banner must figure out a way to bring back
their vanquished allies for an epic showdown with Thanos the evil demigod who
decimated the planet and the universe."
);
2)Install python libraries
a)For Mysql:- pip install pymysql
b)For Flask:- pip install flask
3)Run flask program
Command:- python details.py
4)Copy server link and paste it on browser
Link:- "http://127.0.0.1:5000/result"

