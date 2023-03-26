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
import os
import datetime


def to_dict(t):
    ''' t is a tuple (item, amount, category, date, description)'''
    print('t='+str(t))
    transactions = {'item': t[0], 'amount': t[1],
                    'category': t[2], 'date': t[3], 'description': t[4]}
    return transactions


def tuples_to_dicts(ts):
    return [to_dict(t) for t in ts]


class Transaction():
    def __init__(self, dbname):
        self.dbname = dbname
        self.runQuery(
            '''
        CREATE TABLE IF NOT EXISTS transactions (
            item TEXT,
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

    def add_transaction(self, item_name, amount, category, date, description):
        '''insert new transactions into the table'''
        return self.runQuery("INSERT INTO transactions (item_name, amount, category, date, description) VALUES (?, ?, ?, ?)", (amount, category, date, description))

    def delete_transaction(self, item):
        '''delete a transaction of the table'''
        return self.runQuery("DELETE FROM transactions WHERE item = ?", (item,))

    def summarize_transactions_by_date(self):
        '''summarize the transactions by date'''
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date", ())

    def summarize_transactions_by_month(self):
        '''summarize the transactions by month'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY EXTRACT(MONTH FROM date)", ())

    def summarize_transactions_by_year(self):
        '''summarize the transactions by year'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY EXTRACT(YEAR FROM date)", ())

    def summarize_transactions_by_category(self):
        '''summarize the transactions by category'''
        return self.runQuery("SELECT SUM(amount) FROM transactions GROUP BY category", ())

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

    def runQuery(self, query, tuple):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]




tuples = [("item1", 5, "category1", "2021-03-01", "description1"), 
            ("item2", 6, "category2", "2021-03-01", "description2"),
            ("item3", 7, "category3", "2021-03-01", "description3"),
            ("item1", 7, "category1", "2021-03-02", "description1"),
            ("item2", 76, "category2", "2021-03-02", "description2"),
            ("item3", 24, "category3", "2021-03-02", "description3"),
            ("item1", 74, "category1", "2021-04-02", "description1"),
            ("item2", 6, "category2", "2021-04-02", "description2"),
            ("item3", 4, "category3", "2021-04-02", "description3"),
            ("item1", 55, "category1", "2022-04-02", "description1"),
            ("item2", 36, "category2", "2022-04-02", "description2"),
            ("item3", 46, "category3", "2022-04-02", "description3"),
           ]
transaction_path = os.path.join(os.path.dirname(__file__), 'transaction.db')
con = sqlite3.connect(transaction_path)
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS transaction (item TEXT, amount INTEGER, category TEXT, date TEXT, description TEXT)''')
for i in range(len(tuples)):
    cur.execute('''insert into transaction values(?,?,?,?,?)''', tuples[i])
    # create the transaction database
con.commit()
tr = Transaction(transaction_path)
