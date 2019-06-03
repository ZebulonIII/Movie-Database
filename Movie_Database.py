
import os
import sqlite3

def create_connection(filename):
	""" create a database connection to the SQLite database specified by db_file """
	try:
		conn = sqlite3.connect(filename)
		return conn
	except Error as e:
		print(e)
	return None

def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement """
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def create_insert_sql(values):
	string = 'INSERT INTO movies VALUES('
	for value in values:
		string += value + ', '
	string = string[0:len(string)-3]
	string += ');'
	return string

def insert_movies(conn, insert_sql):
	try:
		c = conn.cursor()
		c.execute(insert_sql)
	except Error as e:
		print(e)

def main():
	db_file = 'movies.db'
	create_table_sql = """ CREATE TABLE IF NOT EXISTS movies (
	name TEXT PRIMARY KEY,
	format TEXT,
	source TEXT,
	size TEXT,
	created TEXT,
	length TEXT); """
	
	conn = create_connection(db_file)
	if conn is not None:
		create_table(conn, create_table_sql)
		for file in folder:
			values = []
			insert_movies(conn, create_insert_sql(values))

if __name__ == '__main__':
    main()