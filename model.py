
from termcolor import cprint 


import sqlite3 as sq3

class Todo(object):
	to_do_dict = {}
	choice = ''
	
	

	def __init__(self):
		self._db = sq3.connect('todoData.db')
		self._c = self._db.cursor()
		self._db.execute('''CREATE TABLE IF NOT EXISTS todo_names
				(
					todo_id INTEGER PRIMARY KEY,
					todo_name TEXT NOT NULL
				) ''')	
		self._db.execute('''CREATE TABLE IF NOT EXISTS todo_tasks
				(
					task_id INTEGER PRIMARY KEY,
					todo_id INTEGER,
					task_item TEXT,
					FOREIGN KEY(todo_id) REFERENCES todo_names(todo_id)
				)''')
		self._db.commit()

	def title_bar(self):
		
		print("\t**********************************************")
		print("\t      ***  To Do Application ***")
		print("\t**********************************************")	
		
	
	# def gen_key(self):
	# 	self._db.execute('SELECT todo_id FROM todo_names')
	# 	key = self._c.fetchone()
	
	def todo_create(self, name):
		self._db.execute("INSERT INTO todo_names (todo_name) VALUES (?)", (name,))
		self._db.commit()
		print("\n Created: ") 
		self._c.execute("SELECT todo_name FROM todo_names")
		item_name = self._c.fetchall()
		print ("Todo:") + item_name[-1][0]
	
	def todo_open(self, list_name):
		self._c.execute("SELECT todo_name FROM todo_names ")
		all_names = self._c.fetchall()

		for name in all_names:
			if list_name  == name:
				self._db.execute("SELECT task_item FROM todo_tasks WHERE task_id = todo_id")
				list_opened = self._c.fetchall()
				print list_opened
			return "No such list Created."	

	def todo_item_add(self, task):
		
			self._db.execute("INSERT INTO todo_tasks (task_item) VALUES(?)", (task,))
			self._db.commit()
 
			self._c.execute("SELECT task_item FROM todo_tasks")
			added_item = self._c.fetchall()
			print "Added: " ,added_item[-1][0]
		


	def todo_list_all(self):
			print "List All Todo: \n"
			self._c.execute("SELECT * FROM todo_names")
			listed = self._c.fetchall			
			print listed
	

	def todo_list_items(self):
			print "List Item In Todo"
			self._c.execute("SELECT task_item FROM todo_tasks")
			item_list = self._c.fetchall()
			print item_list




# title = Todo()
# title.title_bar()
# title.todo_create()
# title.todo_open()
# title.todo_item_add()
# title.todo_list_all()
# title.todo_list_items()
# print "Good bye!"
# os.system("clear")
			
			
