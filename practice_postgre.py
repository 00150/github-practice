# PostgreSQL DB와 연결할 수 있는 패키지를 가져옵니다. (미리 설치되어 있어야 합니다.)
# pip install psycopg2
import psycopg2


# sqlite3 와 마찬가지로 connection 객체를 생성해야 합니다.
# 다만, 이 때 기본적인 설정을 넣어주어야 합니다.

"""
conn = psycopg2.connect(
    host="서버 호스트 주소",
    database="데이터베이스 이름",
    user="유저 이름",
    password="유저 비밀번호")
"""

# postgtresql db와 연결하기 위한 connection 객체 생성, 이후 기본 설정 입력.
conn = psycopg2.connect(
    host = 'ruby.db.elephantsql.com',
    database = 'jgsxmzrp',
    user = 'jgsxmzrp',
    password = 'tqFfsJhbZ6beLfIMwlgPUFeHf0dE2Ays')






# 이후 연결된 객체에 명령을 내릴 수 있는 커서를 생성합니다.
cur = conn.cursor()

# 생성되어 있는 테이블을 지웁니다.
cur.execute("""DROP TABLE onepiece""")

# 이후 위에서 지운 테이블을 다시 생성합니다.
cur.execute("""CREATE TABLE onepiece(Onepiece_Id INTEGER PRIMARY KEY NOT NULL,
            Name VARCHAR(128) NOT NULL,
            Position VARCHAR(128) NOT NULL)""")


# 생성된 테이블에 데이터를 집어넣어봅시다, f-formating을 이용하여 진행합니다.
insert = "INSERT INTO onepiece (Onepiece_Id, Name, Position)" 
query_1 = f"{insert} VALUES (1, 'Luffy', 'Captain')"
query_2 = f"{insert} VALUES (2, 'Zoro', 'Vice Caption')"
query_3 = f"{insert} VALUES (3, 'Nami', 'Mate')"

# 데이터를 추가하기 위해 commit을 날려줍시다. / 이때 commit 연결된 부분에 진행합니다.

cur.execute(query_1)
cur.execute(query_2)
cur.execute(query_3)

conn.commit()

print('done!')



"""
Part 4
클라우드 데이터베이스에 'passenger' 라는 테이블을 생성하고 titanic.csv 에 있는 데이터를 'passenger' 테이블로 옮깁니다.

1. passenger 테이블의 필드를 알맞게 추가합니다 (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Id : INT ( 0부터 시작하고, 테이블의 한 행마다 주여진 INT 형 숫자이며 csv에는 없습니다)
- Survived: INT
- Pclass: INT
- Name: VARCHAR(128)
- Sex: VARCHAR(12)
- Age: FLOAT
- Siblings/Spouses Aboard: INT
- Parents/Children Aboard: INT
- Fare: FLOAT

2. psycopg2.connect 를 이용해 connection 변수가 데이터베이스와 연결할 수 있도록 다음 변수들에 알맞은 정보를 담습니다:
- host: 데이터베이스 호스트 주소를 입력합니다.
- user: 데이터베이스 유저 정보를 입력합니다.
- password: 데이터베이스 비밀번호를 입력합니다.
- database: 데이터베이스 이름을 입력합니다.

3. passenger 테이블에 titanic.csv 에 있는 데이터를 옮깁니다.

"""


# 1. 테이블 삭제.
cur.execute("""DROP TABLE passenger""")


cur.execute("""CREATE TABLE passenger(
    Passenger_Id INTEGER NOT NULL PRIMARY KEY,
    Survived INTEGER,
    Pclass INTEGER,
    Name VARCHAR(128),
    Sex VARCHAR(12),
    Age FLOAT,
    Siblings_Spouses_Aboard INTEGER,
    Parents_Children_Aboard INTEGER,
    Fare FLOAT)""")

conn.commit()


import csv

# 데이터 읽어오기.
f = open('titanic.csv', 'r')
reader = csv.reader(f)

# 데이터 리스트타입으로 변경
data = list(reader)



# 리스트형식으로 변경된 데이터를 슬라이싱합니다.(컬럼명 제거 (0번 idx))
# 함수를 생성합니다.
# 진행상황을 확인할 수 있는 라이브러리를 추가합시다.

from tqdm import tqdm
import time


def insert_data_postgre():
    for idx, row in tqdm(enumerate(data[1:]), desc = '데이터 삽입 진행중'):
        cur.execute("""INSERT INTO passenger (Passenger_Id, Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (idx, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    conn.commit()

insert_data_postgre()