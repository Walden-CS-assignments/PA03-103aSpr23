'''
simple demo of fixtures for Python program with pytest
use to test the TodoList class 
'''
import sqlite3
import pytest
from transaction import Transaction, to_dict, tuples_to_dicts

@pytest.fixture
def tuples():
    '''create some tuples to put in the database 
        author: Haipeng Zhu'''
    return [(5, "category1", "2021-03-01", "description1"),
            (6, "category2", "2021-03-01", "description2"),
            (7, "category3", "2021-03-01", "description3"),
            (7, "category1", "2021-03-02", "description1"),
            (76, "category2", "2021-03-02", "description2"),
            (24, "category3", "2021-03-02", "description3"),
            (74, "category1", "2021-04-02", "description1"),
            (6, "category2", "2021-04-02", "description2"),
            (4, "category3", "2021-04-02", "description3"),
            (55, "category1", "2022-04-02", "description1"),
            (36, "category2", "2022-04-02", "description2"),
            (46, "category3", "2022-04-02", "description3"),
           ]

@pytest.fixture
def returned_tuples(tuples):
    '''add a rowid to the beginning of each tuple
        author: Haipeng Zhu'''
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    '''add a rowid to the beginning of each tuple
        author: Haipeng Zhu'''
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])

@pytest.fixture
def transaction_path(tmp_path):
    '''return the path to the transaction.db database
        author: Haipeng Zhu'''
    yield tmp_path / 'transaction.db'

@pytest.fixture(autouse=True)
def transaction(transaction_path,tuples):
    '''create and initialize the transaction.db database in /tmp 
    Author: Hang Yu'''
    con= sqlite3.connect(transaction_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (amount \
        INTEGER, category TEXT, date TEXT, description TEXT)''')
    for i in range(len(tuples)):
        cur.execute('''insert into transactions values(?,?,?,?)''',tuples[i])
    con.commit()
    trans = Transaction(transaction_path)
    yield trans
    cur.execute('''drop table transactions''')
    con.commit()

def test_show_transactions(transaction,returned_dicts):
    ''' test the show_transactions method
        Author: Hang Yu'''
    tr = transaction
    results = tr.show_transactions()
    expected = returned_dicts
    assert results == expected

def test_add_transaction(transaction,returned_dicts):
    ''' test the add_transaction method'''
    trans = transaction
    tmp = (len(returned_dicts)+1, 5, "category4", "2021-03-01", "description4")
    trans.add_transaction(to_dict(tmp))
    results = trans.show_transactions()
    assert results[-1] == to_dict(tmp)

def test_delete_transaction(transaction,returned_dicts):
    ''' test the delete_transaction method'''
    trans = transaction
    trans.delete_transaction(1)
    results = trans.show_transactions()
    expected = returned_dicts
    assert results == expected[1:]

def test_summarize_transactions_by_date(transaction):
    ''' test the summarize_transactions_by_date method
        author: Haipeng Zhu'''
    trans = transaction
    results = trans.summarize_transactions_by_date()
    expected = [{'date': '2021-03-01', 'amount': 18}, {'date': '2021-03-02', 'amount': 107},\
                 {'date': '2021-04-02', 'amount': 84}, {'date': '2022-04-02', 'amount': 137}]
    assert results == expected

def test_summarize_transactions_by_month(transaction):
    ''' test the summarize_transactions_by_month method
        author: Haipeng Zhu'''
    trans = transaction
    results = trans.summarize_transactions_by_month()
    expected = [{'date': '2021-03', 'amount': 125}, {'date': '2021-04', 'amount': 84},\
                 {'date': '2022-04', 'amount': 137}]
    assert results == expected

def test_summarize_transactions_by_year(transaction):
    ''' test the summarize_transactions_by_year method
        author: Haipeng Zhu'''
    trans = transaction
    results = trans.summarize_transactions_by_year()
    expected = [{'date': '2021', 'amount': 209}, {'date': '2022', 'amount': 137}]
    assert results == expected

def test_summarize_transactions_by_category(transaction):
    ''' test the summarize_transactions_by_category method
        author: Haipeng Zhu'''
    trans = transaction
    results = trans.summarize_transactions_by_category()
    expected = [{'category': 'category1', 'amount': 141}, {'category': 'category2',\
                                        'amount': 124}, {'category': 'category3', 'amount': 81}]
    assert results == expected
