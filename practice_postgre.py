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



