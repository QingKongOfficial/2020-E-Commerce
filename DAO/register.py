from DAO.link_database import *


def close_db_link(conn):
    conn.close()


#注册买家
def register_buyer(name, password, email, address):
    conn = link_mysql()
    cur = conn.cursor()
    cur.execute('INSERT INTO BUYER VALUES (NULL,%s,%s,%s,%s);',(name,password,email,address))
    conn.commit()
    cur.close()
    conn.close()
    print("Successfully INSERT INTO BUYER VALUES (NULL,%s,%s,%s,%s);", (name,password,email,address))

#注册卖家
def register_shop(name, description, password,email):
    conn = link_mysql()
    cur = conn.cursor()
    cur.execute('INSERT INTO SHOP VALUES (NULL,%s,%s,%s,%s);', (name, description, password, email))
    conn.commit()
    cur.close()
    conn.close()
    print('Successfully INSERT INTO SHOP VALUES (NULL,%s,%s,%s,%s);', (name, description, password, email))

#register_buyer('yangjian', '123456', '754032944@qq.com', 'anqing')
#register_shop('yangjian', 'cool', '123456', '754032944@qq.com')




