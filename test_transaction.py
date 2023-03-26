'''
simple demo of fixtures for Python program with pytest
use to test the TodoList class 
'''

import pytest
import sqlite3
from transaction import Transaction, to_dict, tuples_to_dicts

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [("item1", 5, "category1", "2021-03-01", "description1"), 
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

@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])

@pytest.fixture
def transaction_path(tmp_path):
    yield tmp_path / 'transaction.db'

@pytest.fixture(autouse=True)
def transaction(transaction_path,tuples):
    "create and initialize the transaction.db database in /tmp "
    con= sqlite3.connect(transaction_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS data (item TEXT, amount INTEGER, category TEXT, date TEXT, description TEXT)''')
    for i in range(len(tuples)):
        cur.execute('''insert into data values(?,?,?,?,?)''',tuples[i])
    con.commit()
    tr = Transaction(transaction_path)
    yield tr
    cur.execute('''drop table data''')
    con.commit()

def test_show_transactions(transaction,returned_dicts):
    tr = transaction
    results = tr.show_transactions()
    expected = returned_dicts
    assert results == expected

def test_add_transaction(transaction,returned_dicts):
    tr = transaction
    tuple = (len(returned_dicts)+1,'item4', 5, "category4", "2021-03-01", "description4")
    tr.add_transaction(to_dict(tuple))
    results = tr.show_transactions()
    assert results[-1] == to_dict(tuple)

def test_delete_transaction(transaction,returned_dicts):
    tr = transaction
    tr.delete_transaction(1)
    results = tr.show_transactions()
    expected = returned_dicts
    assert results == expected[1:]

def test_summarize_transactions_by_date(transaction,returned_dicts):
    tr = transaction
    results = tr.summarize_transactions_by_date("2021-03-01")
    expected = tuples_to_dicts([(1, "item1", 5, "category1", "2021-03-01", "description1"), 
            (2, "item2", 6, "category2", "2021-03-01", "description2"),
            (3, "item3", 7, "category3", "2021-03-01", "description3"),])
    assert results == expected

def test_summarize_transactions_by_month(transaction,returned_dicts):
    tr = transaction
    results = tr.summarize_transactions_by_month("2021-03")
    expected = tuples_to_dicts([(1, "item1", 5, "category1", "2021-03-01", "description1"), 
            (2,"item2", 6, "category2", "2021-03-01", "description2"),
            (3,"item3", 7, "category3", "2021-03-01", "description3"),
            (4,"item1", 7, "category1", "2021-03-02", "description1"),
            (5,"item2", 76, "category2", "2021-03-02", "description2"),
            (6,"item3", 24, "category3", "2021-03-02", "description3"),])
    assert results == expected

def test_summarize_transactions_by_year(transaction,returned_dicts):
    tr = transaction
    results = tr.summarize_transactions_by_category("category1")
    expected = tuples_to_dicts([(1,"item1", 5, "category1", "2021-03-01", "description1"),
            (4,"item1", 7, "category1", "2021-03-02", "description1"),
            (7,"item1", 74, "category1", "2021-04-02", "description1"),
            (10,"item1", 55, "category1", "2022-04-02", "description1")])
    assert results == expected