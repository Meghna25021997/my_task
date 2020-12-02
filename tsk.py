import pymysql

conn = pymysql.connect(host="localhost", user="root", passwd="", db="my_task")

myCursor = conn.cursor()




#myCursor.execute("INSERT INTO names(id,name,img,summary) VALUES(1,'Harry Potter and the Order of the Phoenix','Harry Potter and Dumbledores warning about the return of Lord Voldemort is not heeded by the wizard authorities who in turn look to undermine Dumbledores authority at Hogwarts and discredit Harry');")
#print(" > Data Inserted!!!")
#myCursor.execute("INSERT INTO names(id,name,img,summary) VALUES(2,'The Lord of the Rings: The Fellowship of the Ring','A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed');")
#print(" > Data Inserted!!!")
#myCursor.execute("INSERT INTO names(id,name,img,summary) VALUES(3,'Avengers: Endgame','Adrift in space with no food or water, Tony Stark sends a message to Pepper Potts as his oxygen supply starts to dwindle. Meanwhile, the remaining Avengers -- Thor, Black Widow, Captain America and Bruce Banner -- must figure out a way to bring back their vanquished allies for an epic showdown with Thanos -- the evil demigod who decimated the planet and the universe.');")
#print(" > Data Inserted!!!")
myCursor.execute("SELECT * FROM table1;")
print(myCursor.fetchall(), end="\n")
conn.commit()
conn.close()