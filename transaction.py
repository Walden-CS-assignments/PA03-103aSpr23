


class Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS todo
                    (amount int, category text, date text, description text)''',())
        
    # def show_categories(self):
        
    #     return 

    # def add_category(self):
        
    #     return

    # def modify_category(self):
       
    #     return 

    def show_transactions(self):
       
        return 
    
    def add_transaction(self,item):
       
        return 
    
    def delete_transaction(self):
       
        return 
    
    def summarize_transactions_by_date(self):
       
        return 
    
    def summarize_transactions_by_month(self):
        
        return 
    
    def summarize_transactions_by_year(self):
        
        return 
    
    def summarize_transactions_by_category(self):
        
        return 
    
    def print_this_menu(self):
       
        return 
    
    
    # def runQuery(self,query,tuple):
    #     ''' return all of the uncompleted tasks as a list of dicts.'''
    #     con= sqlite3.connect(os.getenv('HOME')+'/todo.db')
    #     cur = con.cursor() 
    #     cur.execute(query,tuple)
    #     tuples = cur.fetchall()
    #     con.commit()
    #     con.close()
    #     return [toDict(t) for t in tuples]