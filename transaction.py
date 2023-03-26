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
    ''' t is a tuple (rowid, item, amount, category, date, description)'''
    print('t='+str(t))
    transactions = {'rowid': t[0], 'item': t[1], 'amount': t[2],
                    'category': t[3], 'date': t[4], 'description': t[5]}
    return transactions


def tuples_to_dicts(ts):
    return [to_dict(t) for t in ts]


class Transaction():
    def __init__(self, dbname):
        self.dbname = dbname
        self.runQuery(
            '''
        CREATE TABLE IF NOT EXISTS data (
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
        return self.runQuery("SELECT rowid, * FROM data", ())

    def add_transaction(self, item):
        '''insert new transactions into the table'''
        return self.runQuery("INSERT INTO data (item, amount, category, date, description) VALUES (?, ?, ?, ?, ?)", (item['item'], item['amount'], item['category'], item['date'], item['description']))

    def delete_transaction(self, rowid):
        '''delete a transaction of the table'''
        return self.runQuery("DELETE FROM data WHERE rowid = ?", (rowid,))

    def summarize_transactions_by_date(self, date):
        '''summarize the transactions by date'''
        return self.runQuery("SELECT rowid, * FROM data WHERE date = ?", (date,))

    def summarize_transactions_by_month(self, month):
        '''summarize the transactions by month'''
        return self.runQuery("SELECT rowid, * FROM data WHERE strftime('%Y-%m', date(date)) = ?", (month,))

    def summarize_transactions_by_year(self, year):
        '''summarize the transactions by year'''
        return self.runQuery("SELECT rowid, * FROM data WHERE strftime('%Y', date(date)) = ?", (year,))

    def summarize_transactions_by_category(self, category):
        '''summarize the transactions by category'''
        return self.runQuery("SELECT rowid, * FROM data WHERE category = ?", (category,))

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
        return tuples_to_dicts(tuples)




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
transaction_path = 'transaction.db'
con = sqlite3.connect(transaction_path)
cur = con.cursor()
cur.execute('''DROP TABLE IF EXISTS data''')
cur.execute('''CREATE TABLE IF NOT EXISTS data (item TEXT, amount INTEGER, category TEXT, date TEXT, description TEXT)''')
for i in range(len(tuples)):
    cur.execute('''insert into data values(?,?,?,?,?)''', tuples[i])
con.commit()
res = cur.execute('''SELECT * FROM data''')
tr = Transaction(transaction_path)
# print(tr.show_transactions())
print(tr.summarize_transactions_by_date("2021-03-01"))
# print(tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))]))