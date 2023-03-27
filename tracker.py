#! /opt/miniconda3/bin/python3
'''
This is a simple command line app to track your transactions.
'''
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
            [5] summarize_transactions_by_date
            [6] summarize_transactions_by_month
            [7] summarize_transactions_by_year
            [8] summarize_transactions_by_category
            [9] print_this_menu
            '''
        )


def print_transactions(transactions):
    ''' print the transactions in a nice format'''
    if len(transactions)==0:
        print('No transactions found')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-30s"%('rowid','amount','category','date','description'))
    print('-'*75)
    for item in transactions:
        values = tuple(item.values()) #(rowid,amount, category, date, description)
        print("%-10s %-10s %-10s %-10s %-30s"%values)


def print_date_transactions(transactions):
    ''' print the summary date transactions in a nice format
        author: Haipeng Zhu'''
    if len(transactions)==0:
        print('No transactions found')
        return
    print('\n')
    print("%-10s %-10s"%('date','amount'))
    print('-'*75)
    for item in transactions:
        values = tuple(item.values())
        print("%-10s %-10s"%values)

def print_category_transactions(transactions):
    ''' print the summary category transactions in a nice format
        author: Haipeng Zhu'''
    if len(transactions)==0:
        print('No transactions found')
        return
    print('\n')
    print("%-10s %-10s"%('category','amount'))
    print('-'*75)
    for item in transactions:
        values = tuple(item.values())
        print("%-10s %-10s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    # transaction = Transaction('transaction')
    transaction = Transaction(os.getenv('HOME')+'/transaction.db')
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show_transactions":
        print_transactions(transaction.show_transactions())
    elif arglist[0]=="summarize_transactions_by_date":
        print_date_transactions(transaction.summarize_transactions_by_date())
    elif arglist[0]=="summarize_transactions_by_month":
        print_date_transactions(transaction.summarize_transactions_by_month())
    elif arglist[0]=="summarize_transactions_by_year":
        print_date_transactions(transaction.summarize_transactions_by_year())
    elif arglist[0]=="summarize_transactions_by_category":
        print_category_transactions(transaction.summarize_transactions_by_category())
    elif arglist[0]=='add_transaction':
        if len(arglist)!=5:
            print('Invalid input for add_transaction')
            print_usage()
        else:
            transaction.add_transaction({'amount':arglist[1], 'category':arglist[2]\
                                         , 'date':arglist[3], 'description':arglist[4]})
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
    print_usage()
    args = []
    while args!=['']:
        args = input("command> ").split(' ')
        if args[0]=='add_transaction':
            args = ['add_transaction',args[1],args[2],args[3], ' '.join(args[4:])]
        if args[0]=='quit':
            break
        process_args(args)
        print('-'*75+'\n'*1)

toplevel()
