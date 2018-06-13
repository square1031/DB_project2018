# *- encoding: utf-8 -*-
import sqlite3
import csv
import os.path
import sys

def load_data(data_path):
    dat = []
    iris = list()
    with open( data_path ,'r') as f:
        dat.append(f.readline().strip('\n').split(','))
        dat.append(f.readline().strip('\n').split(','))
        for line in f.readlines():
            iris.append(line.rstrip('\n').split(','))
    dat.append(iris)
    return dat

def connect_db(path=''):
    conn = sqlite3.connect('project_message.db')
    return conn

def create_table(_cursor):
    _cursor.execute('''CREATE TABLE user
                        ( id           INTEGER   PRIMARY KEY    AUTOINCREMENT,
                          password     TEXT                 NOT NULL,
                          email        TEXT                 UNIQUE,
                          username     TEXT                 NOT NULL);''')
    _cursor.execute('''CREATE TABLE location
                        ( name           TEXT,
                          coordinate     TEXT,
                          PRIMARY KEY (name, coordinate));''')
    _cursor.execute('''CREATE TABLE message
                        ( id           INTEGER   PRIMARY KEY    AUTOINCREMENT,
                          content      TEXT                 NOT NULL,
                          like_num     INTEGER              NOT NULL,
                          dislike_num  INTEGER              NOT NULL,
                          time         TIMESTAMP            NOT NULL,
                          uid          TEXT                 NOT NULL,
                          l_name       TEXT                 NOT NULL,
                          l_coordinate TEXT                 NOT NULL,
                          FOREIGN KEY (l_name) REFERENCES location (name) 
                          ON DELETE CASCADE ON UPDATE NO ACTION,
                          FOREIGN KEY (l_coordinate) REFERENCES location (coordinate) 
                          ON DELETE CASCADE ON UPDATE NO ACTION);''')
    _cursor.execute('''CREATE TABLE comment
                        ( id           INTEGER   PRIMARY KEY    AUTOINCREMENT,
                          content      TEXT                 NOT NULL,
                          time         TIMESTAMP            NOT NULL,
                          uid          TEXT                 NOT NULL,
                          mid          TEXT                 NOT NULL,
                          FOREIGN KEY (uid) REFERENCES user (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION,
                          FOREIGN KEY (mid) REFERENCES message (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION);''')
    _cursor.execute('''CREATE TABLE follows
                        ( uid          TEXT                 NOT NULL,
                          mid          TEXT                 NOT NULL,
                          PRIMARY KEY (uid, mid),
                          FOREIGN KEY (uid) REFERENCES user (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION,
                          FOREIGN KEY (mid) REFERENCES message (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION);''')
    _cursor.execute('''CREATE TABLE like_dislike
                        ( like_dislike TEXT ,
                          uid          TEXT                 NOT NULL,
                          mid          TEXT                 NOT NULL,
                          PRIMARY KEY (uid, mid),
                          FOREIGN KEY (uid) REFERENCES user (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION,
                          FOREIGN KEY (mid) REFERENCES message (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION);''')
    _cursor.execute('''CREATE TABLE mood
                        ( type         TEXT ,
                          mid          TEXT                 PRIMARY KEY,
                          FOREIGN KEY (mid) REFERENCES message (id) 
                          ON DELETE CASCADE ON UPDATE NO ACTION);''')
    pass

def insert_item(table,title,a_type,content, _cursor):
    
    if table == 'user':
      command = "INSERT INTO user (id,password,email,username) VALUES (%d, \'%s\', \'%s\', \'%s\');" % (int(content[0]),content[1],content[2],content[3])
    elif table == 'message':
      command = "INSERT INTO message (id,content,like_num,dislike_num,time,uid,l_name,l_coordinate) VALUES (%d, \'%s\', %d, %d, %d, \'%s\', \'%s\', \'%s\');" % (int(content[0]),content[1],int(content[2]),int(content[3]),int(content[4]),content[5],content[6],content[7])
    elif table == 'comment':
      command = "INSERT INTO comment (id,content,time,uid,mid) VALUES (%d, \'%s\', %d, \'%s\', \'%s\');" % (int(content[0]),content[1],int(content[2]),content[3],content[4])
    elif table == 'follows':
      command = "INSERT INTO follows (uid,mid) VALUES (\'%s\', \'%s\');" % (content[0],content[1])
    elif table == 'like_dislike':
      command = "INSERT INTO like_dislike (like_dislike,uid,mid) VALUES (\'%s\', \'%s\', \'%s\');" % (content[0],content[1],content[2])
    elif table == 'location':
      command = "INSERT INTO location (name,coordinate) VALUES (\'%s\', \'%s\');" % (content[0],content[1])
    elif table == 'mood':
      command = "INSERT INTO mood (type,mid) VALUES (\'%s\', \'%s\');" % (content[0],content[1])

    _cursor.execute(command)

    pass


if __name__=="__main__":
    dd = sys.argv[1]
    print(dd)  
    data = load_data(dd)
    if(os.path.isfile('./project_message.db')):
       conn = connect_db()
    else:
       conn = connect_db()
       create_table(conn.cursor())
    try:
        for items in data[2]:
            insert_item(dd.split('.')[0],data[0],data[1],items,conn.cursor())
    except:
        print('wrong')
        print (items)
    conn.commit()
    conn.close()
    # print(data)   

    
        
    
            
