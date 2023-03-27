#! /opt/miniconda3/bin/python3
'''
This is a simple command line app to track your transactions.
'''

from transaction import Transaction
import sys
import os


# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''Enter your command and arguments (if any):
            [1] quit
            [2] show_transactions
            [3] add_transaction [AMOUNT] [CATEGORY] [DATE(e.g. 2021-03-02)] [DESCRIPTION]
            [4] delete_transaction [YOUR_ITEM]
            [5] summarize_transactions_by_date
            [6] summarize_transactions_by_month
            [7] summarize_transactions_by_year
            [8] summarize_transactions_by_category
            [9] print_this_menu
            '''
        )


def print_transactions(transactions):
    ''' print the transactions items '''
    if not transactions:
        print('no transactions to print')
        return
    print('\n')
    if transactions[0] != '[1] quit':   # if called method is print_this_menu(), ignore table header
        print("%-10s %-10s %-20s %-20s %-30s"%('rowid', 'amount', 'category', 'date', 'description'))
    print('-'*75)
    for item in transactions:
        if isinstance(item, str):
            print(item)
        else:
            values = tuple(item.values()) #(rowid, amount, category, date, description)
            print("%-10s %-10s %-20s %-20s %-30s"%values)
            

def print_transactions_by_date(transactions):
    ''' print the todo items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-20s %-10s"%('date','amount'))
    print('-'*40)
    for item in transactions:
        values = tuple(item.values()) #(date, amount)
        print("%-20s %-10s"%values)

def print_transactions_by_category(transactions):
    ''' print the todo items '''
    if len(transactions)==0:
        print('no transactions to print')
        return
    print('\n')
    print("%-20s %-10s"%('category','amount'))
    print('-'*40)
    for item in transactions:
        values = tuple(item.values()) #(category, amount)
        print("%-20s %-10s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    # transaction = Transaction('transaction')
    transaction = Transaction(os.getenv('HOME')+'/transaction.db')
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show_transactions":
        print_transactions(transaction.show_transactions())
    elif arglist[0]=="summarize_transactions_by_date":
        print_transactions_by_date(transaction.summarize_transactions_by_date())
    elif arglist[0]=="summarize_transactions_by_month":
        print_transactions_by_date(transaction.summarize_transactions_by_month())
    elif arglist[0]=="summarize_transactions_by_year":
        print_transactions_by_date(transaction.summarize_transactions_by_year())
    elif arglist[0]=="summarize_transactions_by_category":
        print_transactions_by_category(transaction.summarize_transactions_by_category())
    elif arglist[0]=='add_transaction':
        if len(arglist)!=5:
            print('Invalid input for add_transaction')
            print_usage()
        else:
            transaction.add_transaction({'amount':arglist[1], 'category':arglist[2], 'date':arglist[3], 'description':arglist[4]})
    elif arglist[0]=='print_this_menu':
        print_transactions(transaction.print_this_menu())
    elif arglist[0]=='delete_transaction':
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete_transaction(arglist[1]) # delete by id
    elif arglist[0]=='quit':
        return
    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0] == 'quit':
                return
            
            if args[0]=='add_transaction':
                args = ['add_transaction',args[1],args[2],args[3], ' '.join(args[3:])]
            process_args(args)
            print('-'*75+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*75+'\n'*3)

toplevel()

