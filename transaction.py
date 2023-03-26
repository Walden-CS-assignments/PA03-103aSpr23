'''
transaction.py is an Object Relational Mapping to the transaction database

to Python Dictionaries as follows:

'item #',
'amount',
'category',
'date',
'description'

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transaction.db

'''
import sqlite3

def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))
    transactions = {'item':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    # transactions = {'amount':t[0], 'category':t[1], 'date':t[2], 'description':t[3]}
    return transactions

class Transaction():
    def __init__(self, dbname):
        self.dbname = dbname
        self.runQuery(
        '''
        CREATE TABLE IF NOT EXISTS transactions (
            item INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            category TEXT,
            date TEXT,
            description TEXT
        );
        ''',
        ())
        
    def show_transactions(self):
        '''return all the transactions inside the table'''
        return self.runQuery("SELECT * FROM transactions", ())
    
    def add_transaction(self, amount, category, date, description):
        '''insert new transactions into the table'''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)", (amount, category, date, description))


    # def add_transaction(self,  amount, category, date, description):
    #     '''insert new transactions into the table'''
    #     return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)", (amount, category, date, description))
    
    def delete_transaction(self, item):
        '''delete a transaction of the table'''
        return self.runQuery("DELETE FROM transactions WHERE item = ?", (item,)) 
    
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
        return [
            '[1] quit',
            '[2] show_transactions',
            '[3] add_transaction  [YOUR_ITEM] [AMOUNT] [CATEGORY] [DATE] [DESCRIPTION]',
            '[4] delete_transaction [YOUR_ITEM]',
            '[5] summarize_transactions by date',
            '[6] summarize_transactions by month',
            '[7] summarize_transactions by year',
            '[8] summarize_transactions by category',
            '[9] print_this_menu'
        ]
            
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(self.dbname)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]