from flask import Flask, jsonify, render_template, request, redirect, flash
import sqlite3

  
app = Flask(__name__)


@app.route('/')
def hello():    
    return "Hello World!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search_table')
def search_table():
    return render_template('search_table.html')

@app.route('/show_table',methods=['POST'])
def show_table():
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        #conn = sqlite3.connect('./data.sqlite')
        conn = sqlite3.connect('./../database/project_message.db')
        cursor = conn.cursor()
        #insecure
        #result = cursor.execute('SELECT * FROM %s' % (table_name,))
        print(table_name)
        sql_result = cursor.execute( 'SELECT * FROM {}'.format(table_name))
        final_result = sql_result.fetchall()
        cursor.close()
        conn.close()
        return jsonify(final_result)
   
###########################################################################   
###########################################################################   
@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/modify', methods=['POST'])
def modify():
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        operation = request.form.get('operation')
        #conn = sqlite3.connect('./data.sqlite')
        conn = sqlite3.connect('./../database/project_message.db')
        
        print(conn)
        cursor = conn.cursor()
        if operation == 'INSERT':
            if table_name == 'message':
                content = request.form.get('content')
                like_num = request.form.get('like_num')
                dislike_num = request.form.get('like_num')
                time = request.form.get('time')
                uid = request.form.get('uid')
                l_name = request.form.get('l_name')
                l_coordinate = request.form.get('l_coordinate')
                #insecure
                #sql = cursor.execute('INSERT INTO WORKS_ON (PNAME, PNNUMBER, PLOCATION, DNUM) VALUES (%s, %s, %s);' % (PNAME, PNUMBER, PLOCATION, DNUM))
                sql = 'INSERT INTO message (content, like_num, dislike_num, time, uid, l_name, l_coordinate) VALUES (?, ?, ?, ?, ?, ?, ?);'
                #print((message_id))
                #print(type(message_id))
                cursor.execute(sql, (content, like_num, dislike_num, time, uid, l_name, l_coordinate))

            elif table_name == 'user':
                password = request.form.get('password')
                email = request.form.get('email')
                username = request.form.get('username')
                sql = 'INSERT INTO user (password, email, username) VALUES (?, ?, ?);'
                cursor.execute(sql, (password, email,username))
           
           #problem: uid,mid
            elif table_name == 'comment':
                content = request.form.get('content')
                time = request.form.get('time')
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                print(content,time,uid,mid)
                #exit()
                sql = 'INSERT INTO comment (content, time, uid, mid) VALUES (?, ?, ?, ?);'
                cursor.execute(sql, (content, time, uid, mid))

            elif table_name == 'follows':
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                sql = 'INSERT INTO follows (uid, mid) VALUES (?, ?);'
                cursor.execute(sql, (uid, mid))

            elif table_name == 'like_dislike':
                like_dislike = request.form.get('like_dislike')
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                sql = 'INSERT INTO like_dislike (like_dislike, uid, mid) VALUES (?, ?, ?);'
                cursor.execute(sql, (like_dislike, uid, mid))
       
            elif table_name == 'location':
                name = request.form.get('name')
                coordinate = request.form.get('coordinate')
                sql = 'INSERT INTO location (name, coordinate) VALUES (?, ?);'
                cursor.execute(sql, (name, coordinate))

            elif table_name == 'mood':
                _type = request.form.get('type')
                mid = request.form.get('mid')
                sql = 'INSERT INTO mood (type, mid) VALUES (?, ?);'
                cursor.execute(sql, (uid, mid))

        '''
        elif operation == 'DELETE':
            if table_name == 'message':
                content = request.form.get('content')
                like_num = request.form.get('like_num')
                time = request.form.get('time')
                uid = request.form.get('uid')
                l_name = request.form.get('l_name')
                l_coordinate = request.form.get('l_coordinate')
                #insecure
                #sql = cursor.execute('INSERT INTO WORKS_ON (PNAME, PNNUMBER, PLOCATION, DNUM) VALUES (%s, %s, %s);' % (PNAME, PNUMBER, PLOCATION, DNUM))
                sql = 'INSERT INTO message (content, like_num, time, uid, l_name, l_coordinate) VALUES (?, ?, ?, ?, ?, ?);'
                cursor.execute(sql, (content, like_num, time, uid, l_name, l_coordinate))
            
            elif table_name == 'user':
                password = request.form.get('password')
                email = request.form.get('email')
                username = request.form.get('username')
                sql = 'INSERT INTO user (password, email, username) VALUES (?, ?, ?);'
                cursor.execute(sql, (password, email,username))
           
            elif table_name == 'comment':
                time = request.form.get('time')
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                sql = 'INSERT INTO comment (time, uid, mid) VALUES (?, ?, ?);'
                cursor.execute(sql, (time, uid, mid))

            elif table_name == 'follows':
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                sql = 'INSERT INTO comment (uid, mid) VALUES (?, ?);'
                cursor.execute(sql, (uid, mid))

            elif table_name == 'like_dislike':
                like_dislike = request.form.get('like_dislike')
                uid = request.form.get('uid')
                mid = request.form.get('mid')
                sql = 'INSERT INTO comment (like_dislike, uid, mid) VALUES (?, ?, ?);'
                cursor.execute(sql, (like_dislike, uid, mid))
       
            elif table_name == 'location':
                name = request.form.get('name')
                coordinate = request.form.get('coordinate')
                sql = 'INSERT INTO comment (name, coordinate) VALUES (?, ?);'
                cursor.execute(sql, (name, coordinate))

            elif table_name == 'mood':
                _type = request.form.get('type')
                mid = request.form.get('mid')
                sql = 'INSERT INTO comment (type, mid) VALUES (?, ?);'
                cursor.execute(sql, (_type ,mid))
        '''

        cursor.close()
        conn.commit()
        conn.close()
    return redirect('/data')
    

###########################################################################   
###########################################################################   
@app.route('/data_update')
def data_update():
    return render_template('data_update.html')

@app.route('/update', methods=['POST'])
def update():
    
    if request.method == 'POST':
        table_name = request.form.get('table_name')
        operation = request.form.get('operation')
        #conn = sqlite3.connect('./data.sqlite')
        conn = sqlite3.connect('./../database/project_message.db')
        cursor = conn.cursor()

        #######################################################
        #######################################################
        #redesign
        if table_name == 'message':
            #Add title : use title search
            username = request.form.get('username')
            password = request.form.get('password')
            
            _id = request.form.get('id') #=>change to title
            #print(username,password)
            ##wrong
            sql_result = cursor.execute('SELECT * FROM user, message WHERE user.username=? AND user.password=? AND message.id=?',(username,password,_id))
            #sql_result = cursor.execute('SELECT * FROM user WHERE username=? AND password=?',(username,password))
            
            final_result = sql_result.fetchall()
            #print(final_result) #content
            #check premession
            if len(final_result)==0:
                print("You can not edit this airticle")
            else:
                content_reset = request.form.get('content')
                #print(content_reset)
                cursor.execute('UPDATE message SET content=? WHERE id=?', (content_reset,_id))

        elif table_name == 'user':
            username = request.form.get('username')
            password = request.form.get('password')
            
            username_reset = request.form.get('username_reset')
            email_reset = request.form.get('email_reset')
            password_reset = request.form.get('password_reset')
            
            sql_result = cursor.execute('SELECT * FROM user WHERE username=? AND password=?',(username,password))
            final_result = sql_result.fetchall()
            #print(final_result)
            if len(final_result)==0:
                print("No this password or user")
            else:
                _id=final_result[0][0]
                #print(username_reset,email_reset,password_reset)
                cursor.execute('UPDATE user SET username=?,email=?,password=? WHERE id=?', (username_reset,email_reset,password_reset,_id))
        

        elif table_name == 'comment':
            #?can not get userbane and password??
            username = request.form.get('username')
            password = request.form.get('password')
            uid = request.form.get('uid')
            mid = request.form.get('mid')
            content = request.form.get('content')
            #can not show username,password
            print(username,password,uid,mid,content)
            sql_result = cursor.execute('SELECT comment.id FROM user, comment, message WHERE user.username=? AND user.password=? AND user.id=? AND message.id=?',(username,password,uid,mid))
            final_result = sql_result.fetchall()

            if len(final_result)==0:
                print("You have no premession to edit")
            else:
                _id=final_result[0][0]
                print(_id)
                cursor.execute('UPDATE comment SET content WHERE id=?', (content,_id))
                

            

        ''' 
        elif table_name == 'follows':
            uid = request.form.get('uid')
            mid = request.form.get('mid')
            sql = 'INSERT INTO comment (uid, mid) VALUES (?, ?);'
            cursor.execute(sql, (uid, mid))

        elif table_name == 'like_dislike':
            like_dislike = request.form.get('like_dislike')
            uid = request.form.get('uid')
            mid = request.form.get('mid')
            sql = 'INSERT INTO comment (like_dislike, uid, mid) VALUES (?, ?, ?);'
            cursor.execute(sql, (like_dislike, uid, mid))
   
        elif table_name == 'location':
            name = request.form.get('name')
            coordinate = request.form.get('coordinate')
            sql = 'INSERT INTO comment (name, coordinate) VALUES (?, ?);'
            cursor.execute(sql, (name, coordinate))

        elif table_name == 'mood':
        #if table_name == 'mood':
            _type = request.form.get('type')
            mid = request.form.get('mid')
            get_mid = request.form.get('get_mid')
            sql = 'UPDATE comment SET type=?,uid=? WHERE get_mid'
            cursor.execute(sql, (_type,mid))
        '''
        
        #######################################################
        #######################################################
        
    cursor.close()
    conn.commit()
    conn.close()    
    return redirect('/data_update')

if __name__=='__main__':
    app.run(debug=True)
