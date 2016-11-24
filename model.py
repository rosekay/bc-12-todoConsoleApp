"""

Usage:
    
    my_program (-i | --interactive)
    my_program (-h | --help | --version)
    my_program todo <create>
    my_program todo_open <todo>
    my_program todo_list_all <todo>
    my_program todo_item_add <todo>
    my_program todo_list_items <todo>
    my_program quit 


Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    
"""
import sys
import cmd
from docopt import docopt, DocoptExit
import sqlite3 as sq3
from main import Todo

var = Todo()
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class Todo(cmd.Cmd):
    intro = "\t********************************************** \n" \
            "\t      ***  To Do Application *** \n"\
            "\t********************************************** \n" \
            'Create, Open, Add items and View' \
        + ' (type help for a list of commands.)'
    prompt = '(Todo Console) '
    file = None


    @docopt_cmd
    def do_todo(self, arg):
    	"""Usage: todo <create> """
        var.todo_create()
    
    def do_todo_open(self, arg):
        """Usage: todo <open> """
        var.todo_open()

    def do_todo_item_add(self, arg):
        """Usage: todo <add> <item> """
        var.todo_item_add() 

    def do_todo_list_all(self, arg):
        """Usage: todo <list>"""
        var.todo_list_all()
    
    def do_todo_list_items(self, arg):
        """Usage: todo  """
        var.todo_list_items()
           
    
    
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('\nBye Bye! See you soon!\n')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if __name__ == '__main__':
    Todo().cmdloop()

print(opt)