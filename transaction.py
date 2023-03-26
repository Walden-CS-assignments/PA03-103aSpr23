'''
transaction.py is an Object Relational Mapping to the transaction database

The ORM will work map SQL rows with the schema
    (rowid,title,desc,completed)
to Python Dictionaries as follows:

(5,'commute','drive to work',false) <-->
{rowid:5,title:'commute',desc:'drive to work',completed:false)

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/todo.db

'''
import sqlite3
import os

def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))
    transactions = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
    return transactions

class Transaction():
    def __init__(self, dbname):
        self.runQuery("CREATE TABLE IF NOT EXISTS transactions (amount int, category text, date text, description text)",())
        
    def show_transactions(self):
        '''return all the transactions inside the table'''
        return self.runQuery("SELECT * FROM transactions", ())
    
    def add_transaction(self,title, desc, completed):
        '''insert new transactions into the table'''
        return self.runQuery("INSERT INTO transactions (title, desc, completed) VALUES (?, ?, ?)", (title, desc, completed))
    
    def delete_transaction(self, rowid):
        '''delete a transaction of the table'''
        return self.runQuery("DELETE FROM transactions WHERE rowid=(?)", (rowid,)) 
    
    def summarize_transactions_by_date(self):
        '''summarize the transactions by date'''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date",())
    
    def summarize_transactions_by_month(self):
        '''summarize the transactions by month'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY EXTRACT(MONTH FROM date)",())
    
    def summarize_transactions_by_year(self):
        '''summarize the transactions by year'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY EXTRACT(YEAR FROM date)",())
    
    def summarize_transactions_by_category(self):
        '''summarize the transactions by category'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY category",())
    
    def print_this_menu(self):
        print(
            '''
            0. quit
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. print this menu
            '''
        )
        return 
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]