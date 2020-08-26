from mysql import connector

conn = connector.connect(
    host="localhost",
    user="root",
    passwd="9960551687",
    database="injectsolar")   #CONNECT TO MYSQL

curr = conn.cursor()

def create_table():

    curr.execute("drop table if exists error_log")  #DROPING TABLE TO AVOID ERROR
    curr.execute("CREATE TABLE error_log ( \
                            id INT AUTO_INCREMENT PRIMARY KEY, \
                            device_name VARCHAR(100),  \
                            invertor_name VARCHAR(100), \
                            alarm VARCHAR(100), \
                            occurance_time	 DATETIME, \
                            clearance_time	 DATETIME, \
                            message VARCHAR(100) \
                            )")
create_table()                                      #ERRO_LOG TABLE CREATED

def table(list):
    data = "INSERT INTO error_log ( device_name, invertor_name,alarm, occurance_time, clearance_time, message) VALUES (%s, %s, %s, %s, %s, %s)"
    curr.executemany(data, list)     #INSERT VALUES IN TABLE
    conn.commit()

def fetch(item):
    curr.execute(f"SELECT * FROM {item}")
    curr.fetchall()

    print('done')

