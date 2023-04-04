# db : sqlite를 사용하기 위한 파이썬의 패키지 불러오기.  
import sqlite3

# 'CONNECTION' 객체 생성.
# -- db : sqlite에 존재하는 db에 연결하기 위함이다.
# 이 연결은 close() 될 때까지 유지된다.
# 또한 연결하는 db의 이름이 존재하지 않을시 생성되며 접속하며, 존재하는 경우 바로 연결한다.
conn = sqlite3.connect('test.db')

# connect 객체는 바로 db와 소통할 수 없습니다, 소통할 수 있는 객체 Cusor 를 생성합니다.
cur = conn.cursor()


# 테이블이 존재한다면 먼저 삭제를 진행합니다.
cur.execute("""DROP TABLE test_table""")

# 테이블을 생성합니다. : execute -> sql 쿼리문을 바로 넘길 수 있습니다.
cur.execute("""CREATE TABLE test_table(name VARCHAR(32), age INTEGER);""")

#----ver 1. 데이터를 추가합니다.
cur.execute("INSERT INTO test_table(name, age) VALUES('spongebob', 12);")

#----ver 2. 데이터를 추가합니다. (ver1과 다른 방법입니다.)


# 1. 값을 선언합니다.
name = 'banana'
age = 13
cur.execute("INSERT INTO test_table(name, age) VALUES (?, ?)", (name, age)) 


# 데이터를 더 추가합니다.
cur.execute("INSERT INTO test_table (name, age) VALUES ('patrick', 13);")
cur.execute("INSERT INTO test_table (name, age) VALUES ('squidward', 14);")


#----ver 3. 다른 버전 또한 추가합니다.
users = [('lemon', 10), ('apple', 15)]

for user in users :
    cur.execute("INSERT INTO test_table (name, age) VALUES (?,?);", user)

conn.commit()

    
print('done!')

cur.execute("SELECT * FROM test_table AS tt")


# db에 존재하는 값을 각 레코드(행)별로 튜플로 묶은 후, 리스트 안의 값으로 출력됩니다.
#result = cur.fetchall();
#print(result)


result1 = cur.fetchmany();
print(result1)