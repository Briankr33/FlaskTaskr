import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:

	# get a cursor object to execute sql commands
	c = connection.cursor()

	# create the table
	c.execute("""create table tasks(task_id integer primary key autoincrement, 
		name text not null, due_date text not null, priority integer not null,
		status integer not null)""")

	# insert dummy data into the table
	c.execute('insert into tasks (name , due_date, priority, status)'
		'values ("Finish this tutorial", "03-25-2015", 10, 1)')
	c.execute('INSERT INTO tasks (name, due_date, priority, status)'
		'VALUES("Finish Real Python Course 2", "03/25/2015", 10, 1)')