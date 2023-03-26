#! /opt/miniconda3/bin/python3
'''
tracker is an app that maintains a todo list
just as with the todo code in this folder.

but it also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, TodoList, will map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->

{rowid:5,
 title:'commute',
 desc:'drive to work',
 completed:false)
 }

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists

'''
import sys
import datetime
import os
from transaction import Transaction


# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''Enter your command and arguments (if any):
            [1] quit
            [2] show_transactions
            [3] add_transaction [AMOUNT] [CATEGORY] [DATE] [DESCRIPTION]
            [4] delete_transaction [YOUR_ITEM]
            [5] summarize_transactions by date
            [6] summarize_transactions by month
            [7] summarize_transactions by year
            [8] summarize_transactions by category
            [9] print_this_menu
            '''
          )

# def print_transactions(transactions):
#     ''' print the transactions items '''
#     if not transactions:
#         print('no transactions to print')
#         return
#     print('\n')
#     if transactions[0] != '[1] quit':   # if called method is print_this_menu(), ignore table header
#         print("%-10s %-10s %-20s %-20s %-30s"%('item','amount','category','date','description'))
#     print('-'*40)
#     for item in transactions:
#         if isinstance(item, str):
#             print(item)
#         else:
#             values = tuple(item.values()) #(item #,amount,category,date,description)
#             print("%-10s %-10s %-20s %-20s %-30s"%values)


def print_transactions(transactions):
    ''' print the transactions items '''
    if not transactions:
        print('no transactions to print')
        return
    print('\n')
    # if called method is print_this_menu(), ignore table header
    if transactions[0] != '[1] quit':
        print("%-10s %-10s %-20s %-20s %-30s" %
              ('item', 'amount', 'category', 'date', 'description'))
    print('-'*75)
    for item in transactions:
        if isinstance(item, str):
            print(item)
        else:
            # (item, amount, category, date, description)
            values = tuple(item.values())
            print("%-10s %-10s %-20s %-20s %-30s" % values)


def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    # transaction = Transaction('transaction')
    transaction = Transaction(os.getenv('HOME')+'/transaction.db')
    if arglist == []:
        print_usage()
    elif arglist[0] == "show_transactions":
        print_transactions(transaction.show_transactions())
    elif arglist[0] == "summarize_transactions_by_date":
        print_transactions(transaction.summarize_transactions_by_date())
    elif arglist[0] == "summarize_transactions_by_month":
        print_transactions(transaction.summarize_transactions_by_month())
    elif arglist[0] == "summarize_transactions_by_year":
        print_transactions(transaction.summarize_transactions_by_year())
    elif arglist[0] == "summarize_transactions_by_category":
        print_transactions(transaction.summarize_transactions_by_category())
    elif arglist[0] == 'add_transaction':
        if len(arglist) != 5:
            print('Invalid input for add_transaction')
            print_usage()
        else:
            transaction.add_transaction(
                arglist[1], arglist[2], arglist[3],  ' '.join(arglist[4:]))
    elif arglist[0] == 'print_this_menu':
        print_transactions(transaction.print_this_menu())
    elif arglist[0] == 'delete_transaction':
        if len(arglist) != 2:
            print_usage()
        else:
            transaction.delete_transaction(arglist[1])  # delete by id
    elif arglist[0] == 'quit':
        return
    else:
        print(arglist, "is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv) == 1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("command> ").split(' ')
            if args[0] == 'add':
                # join everyting after the name as a string
                # args = ['add',args[1]," ".join(args[2:])]
                args = ['add', args[1], args[2], args[3], ' '.join(args[3:])]
            process_args(args)
            print('-'*75+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*75+'\n'*3)


toplevel()
