import sqlite3

conn = sqlite3.connect('movie.db')      # connecting to database

c=conn.cursor()         # creating a curser

# Creating a table
#c.execute("""CREATE TABLE Movies(
  #  movie_name text,
 #   actor text,
 #   actress text,
 #   year integer,
 #   dir_name text
 #   )""")

# Inserting data into table
#c.execute("INSERT INTO Movies VALUES('Interstellar','Mathew McConaughey','Anna Hathaway','2014','Christopher Nolan')")
#print("Command executed successfully")
#c.execute("INSERT INTO Movies VALUES('John Wick','Keenu Reeves','Bridget Moynahan','2014','Chad Stahelski')")
#c.execute("INSERT INTO Movies VALUES('Inception','Leonardo Dicaprio','Marion','2010','Christopher Nolan')")
#c.execute("INSERT INTO Movies VALUES('Logan','Hugh Jackman','Dafne Keen','2017','James Mangold')")
#c.execute("INSERT INTO Movies VALUES('Edge of Tomorrow','Tom Cruise','Emily Blunt','2014','Doung Liman')")

c.execute("SELECT * FROM Movies")
movie_list = c.fetchall()
for i in movie_list:
    print (i)
print("\n")

f=0
name = input("Enter the actor name to print his movie: ")
name = name.upper()         #to convert every input character to uppercase 
for i in movie_list:
    t=i[1].upper()          #converted to uppercase to check with input name
    if(t==name):
        c.execute("SELECT * FROM Movies WHERE actor='i[1]'")
        mov_list = c.fetchall()
        print(i)
        f=1
if(f==0):
    print("Actor not found in the database!!")

conn.commit()

conn.close()