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
cur.execute("""CREATE TABLE onepiece(Onepiece_Id INTEGER PRIMARY KEY,
            Name VARCHAR(128) NOT NULL,
            Position VARCHAR(128) NOT NULL)""")


# 생성된 테이블에 데이터를 집어넣어봅시다, f-formating을 이용하여 진행합니다.
insert = "INSERT INTO onepiece (Name, Position);" 
query_1 = f"{insert} VALUES (Luffy, Captain)"
query_2 = f"{insert} VALUES (Zoro, Vice Caption)"
query_3 = f"{insert} VALUES (Nami, Mate)"

# 데이터를 추가하기 위해 commit을 날려줍시다. / 이때 commit 연결된 부분에 진행합니다.
conn.commit()

print('done!')