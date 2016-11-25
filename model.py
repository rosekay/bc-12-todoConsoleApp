
from termcolor import cprint 
import sqlite3 as sq3

class Todo(object):
	open_todo = 0 
	
	

	def __init__(self):
		self._db = sq3.connect('todoData.db')
		self._c = self._db.cursor()
		self._db.execute('''CREATE TABLE IF NOT EXISTS todo
				(
					id INTEGER PRIMARY KEY,
					todo_id INTEGER,
					todo_name TEXT NOT NULL,
					task_item TEXT
				) ''')	
		self._db.commit()

	def title_bar(self):
		
		print("\t**********************************************")
		print("\t      ***  To Do Application ***")
		print("\t**********************************************")	
		
	
	
	
	def todo_create(self, name):
		self._db.execute("INSERT INTO todo (todo_name) VALUES (?)", (name,))
		self._db.commit()
		print("Created: " +  name) 
		
	def todo_open(self, list_id):
		var_open = 1
		list_id = int(list_id)
		self._c.execute("SELECT id FROM todo")
		all_id = self._c.fetchall()
		ids = [x[0] for x in all_id ]
		if list_id in ids:
			self.task = list_id
		else:
			print 'Id not available'
		self._db.commit()	 

		 
		
	def item_add(self, item_to_add):

			self._c.execute("SELECT task_item FROM todo WHERE id={}".format(self.task))
			all_id = self._c.fetchall()
			if all_id[0][0] != None:
				tasks = list(all_id[0])
				if len(tasks) > 0:
					tasks.append(item_to_add)
					items = ','.join(tasks)
					self._db.execute("UPDATE todo SET task_item=? WHERE id = ?", (items, self.task))
					self._db.commit()
			else:
				items = item_to_add
				self._db.execute("UPDATE todo SET task_item=? WHERE id=? ", (items, self.task))
				self._db.commit()

	def todo_list(self):
		from prettytable import PrettyTable
		print "List All Todo: \n"
		self._c.execute("SELECT todo_name FROM todo")
		lists = self._c.fetchall()
		todo_table = PrettyTable(['Todo Name'])
		for item in lists:
			todo_table.add_row([str(item[0])])
		 
		print todo_table

	def item_list(self, item_name):
		self._c.execute("SELECT task_item FROM todo")
		list_item = self._c.fetchall()
		if type(item_name) == str:
			print list_item[0][-1]
		elif type(item_name) == int:
			print list_item 	

		for item in list_item:
			if item_id in list_item:
				self._c.execute("SELECT task_item FROM todo_tasks WHERE item_id = task_id ")
				todonames = self._c.fetchall()
				for item in todonames:
					ll = [item[0], [-1]]
				print "List Item In Todo"
			print "Invalid List"	
	




			
