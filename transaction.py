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


def to_dict(t):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    print('t='+str(t))
    transactions = {'rowid': t[0], 'amount': t[1],
                    'category': t[2], 'date': t[3], 'description': t[4]}
    return transactions


def summary_date_to_dict(t):
    ''' t is a tuple (rowid, amount, category, date, description), it is called when summarize by date is called'''
    print('t='+str(t))
    transactions = {'date': t[0], 'amount': t[1]}
    return transactions


def summary_category_to_dict(t):
    ''' t is a tuple (rowid, item, amount, category, date, description), it is called when summarize
      by category is called'''
    print('t='+str(t))
    transactions = {'category': t[0], 'amount': t[1]}
    return transactions


def tuples_to_dicts(ts):
    ''' ts is a list of tuples, convert to list of dicts '''
    return [to_dict(t) for t in ts]


class Transaction():
    ''' Transaction is an Object Relational Mapping to the transaction database '''

    def __init__(self, dbname):
        self.dbname = dbname
        self.run_query(
            '''
        CREATE TABLE IF NOT EXISTS transactions (
            amount INTEGER,
            category TEXT,
            date TEXT,
            description TEXT
        );
        ''',
            ())

    def show_transactions(self):
        '''return all the transactions inside the table'''
        return self.run_query("SELECT rowid, * FROM transactions", ())

    def add_transaction(self, item):
        '''insert new transactions into the table'''
        return self.run_query("INSERT INTO transactions (amount, category, date, description) \
                             VALUES (?, ?, ?, ?)", (item['amount'], item['category']\
                                                    , item['date'], item['description']))

    def delete_transaction(self, rowid):
        '''delete a transaction of the table'''
        return self.run_query("DELETE FROM transactions WHERE rowid = ?", (rowid,))

    def summarize_transactions_by_date(self):
        '''summarize the transactions by date'''
        return self.run_summary_date_query("SELECT date, SUM(amount)\
                                            FROM transactions GROUP BY date", ())

    def summarize_transactions_by_month(self):
        '''summarize the transactions by month'''
        return self.run_summary_date_query("SELECT strftime('%Y-%m', date(date))\
                                           , SUM(amount) FROM transactions GROUP BY \
                                           strftime('%Y-%m', date(date))", ())

    def summarize_transactions_by_year(self):
        '''summarize the transactions by year'''
        return self.run_summary_date_query("SELECT strftime('%Y', date(date)), \
                                           SUM(amount) FROM transactions GROUP BY \
                                           strftime('%Y', date(date))", ())

    def summarize_transactions_by_category(self):
        '''summarize the transactions by category'''
        return self.run_summary_category_query("SELECT category, SUM(amount) \
                                               FROM transactions GROUP BY category", ())

    def print_this_menu(self):
        '''print the menu'''
        return [
            '[1] quit',
            '[2] show_transactions',
            '[3] add_transaction [AMOUNT] [CATEGORY] [DATE] [DESCRIPTION]',
            '[4] delete_transaction [rowid]',
            '[5] summarize_transactions by date',
            '[6] summarize_transactions by month',
            '[7] summarize_transactions by year',
            '[8] summarize_transactions by category',
            '[9] print_this_menu'
        ]

    def run_query(self, query, tuple):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return tuples_to_dicts(tuples)

    def run_summary_date_query(self, query, tuple):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summary_date_to_dict(t) for t in tuples]

    def run_summary_category_query(self, query, tuple):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbname)
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [summary_category_to_dict(t) for t in tuples]
