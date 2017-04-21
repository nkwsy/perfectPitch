import psycopg2

def postgresConnect():
    #Define our connection string 
    conn_string = "postgres://hjnhakqcsbigpc:TniHiEUPkI1ZWHtRn_q06yxfAf@ec2-107-20-178-83.compute-1.amazonaws.com:5432/d13h9rm9pegmbm"
    # print the connection string we will use to connect
    print "Connecting to database\n   ->%s" % (conn_string)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    return conn





### TODO change to another identity structure

#user = input('Enter your name: ')



### One account


# Some way user selects mode, practice(no saved data) and training(saved data, progress reports), 
# possibly through an app.    updateScore1(1, '3')
# updateScore(1, 6, 2, lv1right, lv1wrong)


###### find way to append lv1right to the appropriate level

def updateScore(id2, right, wrong, lvright, lvwrong):
	conn = postgresConnect()
	cur = conn.cursor()
	cur.execute("""UPDATE users
					SET lv1right= %(right)s, lv1wrong = %(wrong)s
					WHERE id = %(id)s """, {'id': id2, 'right': right, 'wrong' : wrong, 'lvright' : lvright, 'lvwrong': lvwrong})
	conn.commit()

# def updateScore(id2, cscore):
# 	conn = postgresConnect()
# 	cur = conn.cursor()
# 	cur.execute("""UPDATE users
# 					SET correct = %(cscore)s
# 					WHERE id = %(id)s """, {'id': id2, 'cscore': cscore})
# 	conn.commit()