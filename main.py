# import modules as 
from modules import *
import sqlite3
connect = sqlite3.connect("data_base.db")
cursor = connect.cursor()
# print(dir(modules))
create_table(cursor=cursor,table_name='Users')

connect.commit()
connect.close()