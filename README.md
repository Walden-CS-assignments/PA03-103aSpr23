# PA03-103aSpr23
pylint test_transaction.py
``` python
haipengzhu@Haipengs-MBP PA03-103aSpr23 % pylint test_transaction.py
************* Module test_transaction
test_transaction.py:27:20: W0621: Redefining name 'tuples' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:32:19: W0621: Redefining name 'tuples' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:42:16: W0621: Redefining name 'transaction_path' from outer scope (line 37) (redefined-outer-name)
test_transaction.py:42:33: W0621: Redefining name 'tuples' from outer scope (line 10) (redefined-outer-name)
test_transaction.py:48:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
test_transaction.py:56:27: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:56:39: W0621: Redefining name 'returned_dicts' from outer scope (line 32) (redefined-outer-name)
test_transaction.py:63:25: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:63:37: W0621: Redefining name 'returned_dicts' from outer scope (line 32) (redefined-outer-name)
test_transaction.py:71:28: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:71:40: W0621: Redefining name 'returned_dicts' from outer scope (line 32) (redefined-outer-name)
test_transaction.py:79:40: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:88:41: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:97:40: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)
test_transaction.py:105:44: W0621: Redefining name 'transaction' from outer scope (line 42) (redefined-outer-name)

------------------------------------------------------------------
Your code has been rated at 7.46/10 (previous run: 6.10/10, +1.36)
```

pylint tracker.py
```python
pylint tracker.py
************* Module tracker
tracker.py:33:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:37:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:47:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:51:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:60:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:64:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:66:0: R0912: Too many branches (15/12) (too-many-branches)

-----------------------------------
Your code has been rated at 9.07/10
```

pyline transaction.py
```python
pylint transaction.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.64/10, +0.36)
```

pytest
```python
pytest test_transaction.py
====================================================================================================== test session starts ======================================================================================================
platform darwin -- Python 3.10.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/haipengzhu/Dropbox/brandeis course/cs103/week8/PA03-103aSpr23
plugins: anyio-3.6.2
collected 7 items                                                                                                                                                                                                               

test_transaction.py .......                                                                                                                                                                                               [100%]

======================================================================================================= 7 passed in 0.03s =======================================================================================================
```

tracker.py
```python
Enter your command and arguments (if any):
            [1] quit
            [2] show_transactions
            [3] add_transaction [AMOUNT] [CATEGORY] [DATE] [DESCRIPTION]
            [4] delete_transaction [YOUR_ITEM]
            [5] summarize_transactions_by_date
            [6] summarize_transactions_by_month
            [7] summarize_transactions_by_year
            [8] summarize_transactions_by_category
            [9] print_this_menu
            
command> show_transactions


rowid      amount     category   date       description                   
---------------------------------------------------------------------------
1          5          category1  2021-03-04 description1                  
3          9          category2  2021-03-04 des                           
4          5          cate1      2000-01-01 is                            
5          20         cate1      2022-03-02 dess                          
---------------------------------------------------------------------------

command> add_transaction 9 category2 2022-03-04 ss
---------------------------------------------------------------------------

command> show_transactions


rowid      amount     category   date       description                   
---------------------------------------------------------------------------
1          5          category1  2021-03-04 description1                  
3          9          category2  2021-03-04 des                           
4          5          cate1      2000-01-01 is                            
5          20         cate1      2022-03-02 dess                          
6          9          category2  2022-03-04 ss                            
---------------------------------------------------------------------------

command> delete_transaction 1
---------------------------------------------------------------------------

command> show_transactions


rowid      amount     category   date       description                   
---------------------------------------------------------------------------
3          9          category2  2021-03-04 des                           
4          5          cate1      2000-01-01 is                            
5          20         cate1      2022-03-02 dess                          
6          9          category2  2022-03-04 ss                            
---------------------------------------------------------------------------

command> summarize_transactions_by_date


date       amount    
---------------------------------------------------------------------------
2000-01-01 5         
2021-03-04 9         
2022-03-02 20        
2022-03-04 9         
---------------------------------------------------------------------------

command> summarize_transactions_by_month


date       amount    
---------------------------------------------------------------------------
2000-01    5         
2021-03    9         
2022-03    29        
---------------------------------------------------------------------------

command> summarize_transactions_by_year


date       amount    
---------------------------------------------------------------------------
2000       5         
2021       9         
2022       29        
---------------------------------------------------------------------------

command> summarize_transactions_by_category


category   amount    
---------------------------------------------------------------------------
cate1      25        
category2  18        
---------------------------------------------------------------------------
command> print_this_menu
Enter your command and arguments (if any):
            [1] quit
            [2] show_transactions
            [3] add_transaction [AMOUNT] [CATEGORY] [DATE] [DESCRIPTION]
            [4] delete_transaction [YOUR_ITEM]
            [5] summarize_transactions_by_date
            [6] summarize_transactions_by_month
            [7] summarize_transactions_by_year
            [8] summarize_transactions_by_category
            [9] print_this_menu
            
---------------------------------------------------------------------------

command> quit
```