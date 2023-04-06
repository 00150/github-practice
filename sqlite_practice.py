#------------------ Part 1. -------------------


# Customer 테이블 생성.
customer_table ="""CREATE TABLE Customer(
    customer_id INTEGER NOT NULL PRIMARY KEY,
    customer_name VARCHAR(32) NOT NULL,
    customer INTEGER);"""


# package 테이블 생성.
package_table = """CREATE TABLE Package(
    package_id INTEGER NOT NULL PRIMARY KEY,
    package_name VARCHAR(32) NOT NULL,
    package_date DATE);"""


# customer_package 테이블 생성.
customer_package = """CREATE TABLE Customer_Package(
cp_id INTEGER NOT NULL PRIMARY KEY,
customer_id INTEGER, 
package_id INTEGER,
FOREIGN KEY(customer_id) REFERENCES Customer(customer_id),
FOREIGN KEY(package_id) REFERENCES Package(package_id));"""


# ------------------- Part 2. -----------------------
# 문제에서 요구하는 것과 달리, '문제에서 요구하는 값을 확인할 수 있게' 쿼리문을 작성함.

q1 = """SELECT a.Title FROM albums As a WHERE a.AlbumId = 31;"""

q2 = """SELECT a.AlbumId, a2.Name 
FROM albums AS a 
LEFT OUTER JOIN artists AS a2  
ON a.ArtistId = a2.ArtistId
WHERE a2.Name LIKE '%the%';"""

q3 = """SELECT i.InvoiceId, i.BillingCity 
FROM invoices AS i 
WHERE i.BillingCity IN ('Stuttgart', 'Oslo', 'Redmond') 
ORDER BY i.InvoiceId;"""

q4 = """SELECT t.Name, t.TrackId 
FROM tracks AS t 
WHERE t.Name LIKE 'the%'; """

q5 = """SELECT c.CustomerId, c.Email 
FROM customers AS c 
WHERE c.Email LIKE  '%gmail.com%';  """

q6 = """SELECT i.InvoiceId, i.CustomerId, i.Total 
FROM invoices AS i 
WHERE i.CustomerId IN (29, 30, 63) 
AND i.Total >=1 AND i.Total <= 3; """

q7 = """SELECT t.TrackId, g.Name,t.Milliseconds 
FROM tracks AS t 
LEFT OUTER JOIN genres AS g 
ON t.GenreId = g.GenreId
WHERE t.Milliseconds >= 300000 AND t.Milliseconds <=400000; """

q8 = """SELECT COUNT(c.FirstName) AS The_Num_of_customers_X_Country, c.Country FROM customers AS c GROUP BY c.Country; """

q9 = """SELECT c.CustomerId
FROM customers c
JOIN invoices i 
ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
HAVING SUM(i.Total)
ORDER BY SUM(i.Total) DESC
LIMIT 5;"""

q10 = """SELECT Name, COUNT(DISTINCT CustomerId)
FROM (SELECT g.Name , i.CustomerId 
from tracks t, invoice_items ii , invoices i , genres g 
WHERE g.GenreId = t.GenreId 
and t.TrackId = ii.TrackId 
and ii.InvoiceId = i.InvoiceId)
GROUP BY Name;"""

#----practice advanced sqlite
n313_q1 ="""SELECT c.CustomerId, UPPER(c.City || ' ' || C.Country) AS CITY_COUNTRY FROM customers AS c; """

n313_q2 ="""SELECT SUBSTRING(c.FirstName,1,4) ||''|| SUBSTRING(c.LastName,1,2) AS alies FROM customers AS c; """

n313_q3 ="""SELECT e.EmployeeId, e.HireDate, e.LastName  FROM employees AS e
WHERE DATE('2020-01-01') - e.HireDate >7
ORDER BY e.LastName ASC;"""

n313_q4 ="""SELECT c.FirstName ||''||c.LastName||''||
(SELECT i.InvoiceId  FROM invoices AS i WHERE  i.CustomerId = c.CustomerId) AS newId
FROM customers AS c;"""

n313_q5 ="""SELECT t.Name FROM tracks AS t 
WHERE t.AlbumId 
IN (SELECT a.AlbumId FROM albums AS a """

# --
n313_part2 = """SELECT *, CASE  
	WHEN t.salary <2900 THEN 'Low'
	WHEN t.salary <=3800 THEN 'Mid'
	ElSE 'High' 
END AS '월급 그룹'
FROM Teacher AS t;"""


n313_part3_1 = """SELECT s.teacher_id, s.student_id, s.ROWID AS '학생순서'
FROM Student AS s;"""

n313_part3_2 = """SELECT s.teacher_id, s.student_id, ROW_NUMBER()
OVER(PARTITION BY s.teacher_id ORDER BY s.student_id) AS '선생님별 학생순서'
FROM Student AS s"""

n313_part3_3 = """
SELECT s.student_id, S.age  AS '중앙값'
FROM Student AS s
ORDER BY s.age 
LIMIT 1
OFFSET (SELECT COUNT(*) FROM Student AS s) / 2; 
"""
#----n314 Part1 : sqlite db 생성 -> DB_API (스키마 홈페이지 참조...) / 이후 데이터 넣기.


# 1. sqlite 패키지 가져오기.
import sqlite3

# 2. DB 연결 위한 connection 객체 생성
conn = sqlite3.connect('DB_API')

# 3. 작업하기 위한 명령, cursor 객체 생성 (connection 안에)
cur = conn.cursor()


# 4. 테이블이 생성되어 있는 상태라면, 미리 테이블을 지워줍시다.
cur.execute("""DROP TABLE Albums_Part1""")



# 5. 테이블 생성 -> DB_API
cur.execute("""CREATE TABLE Albums_Part1(
    AlbumId INTEGER PRIMARY KEY NOT NULL, 
    Title NVARCHAR(160),
    ArtistId INTEGER)""")



# ek

list_data = [
    ["AlbumId","Title","ArtistId"],
    [1,"For Those About To Rock We Salute You",1],
    [2,"Balls to the Wall",2],
    [3,"Restless and Wild",2],
    [4,"Let There Be Rock",1],
    [5,"Big Ones",3],
    [6,"Jagged Little Pill",4],
    [7,"Facelift",5],
    [8,"Warner 25 Anos",6],
    [9,"Plays Metallica By Four Cellos",7],
    [10,"Audioslave",8]
]


# 리스트 안의 데이터를 집어넣는 함수를 작성합시다.
def Insert_values_in_table(list_data):
    insert = "INSERT INTO Albums_Part1 (AlbumId, Title, ArtistId)"
    for i in list_data[1:]:
        cur.execute(f"{insert} VALUES (?,?,?);", i)
    
    conn.commit()
    print('done!')
    
    

# 함수를 실행하여 봅시다.
Insert_values_in_table(list_data)



#----n314 Part2 :  생성된-> DB : DB_API에 TABLE : Albums_Part2 생성 이후 아래의 데이터 집어넣기.


# drop table : Albums_Part2
cur.execute('DROP TABLE Albums_Part2')


# create table : Albums_Part2
cur.execute("""CREATE TABLE Albums_Part2(
    AlbumId INTEGER PRIMARY KEY NOT NULL,
    Title NVARCHAR(160),
    ArtistId INTEGER)""")





dictionary_data = {
		"Columns":["AlbumId", "Title", "ArtistId"],
		"1" : ["For Those About To Rock We Salute You",1],
    	"2" : ["Balls to the Wall",2],
    	"3" : ["Restless and Wild",2],
    	"4" : ["Let There Be Rock",1],
    	"5" : ["Big Ones",3],
    	"6" : ["Jagged Little Pill",4],
    	"7" : ["Facelift",5],
    	"8" : ["Warner 25 Anos",6],
    	"9" : ["Plays Metallica By Four Cellos",7],
    	"10" : ["Audioslave",8]
		}



# method 1 : 잘라내기.
def cut_add_data(dictonary_data):
    copy_data = dictionary_data.copy()
    del copy_data['Columns']
    for key, value in copy_data.items():
        cur.execute("INSERT INTO Albums_Part2 (Title, ArtistId) VALUES (?,?)",value)   
    conn.commit()
    
# 위 함수를 실행 -> cut_add_data(dictionary_data)


# method 2 : 잘라내지 않기.
def not_cut_add_data(dictionary_data):
    
    
    for i in range(1, len(dictionary_data)):
        
        # 키값이 '문자인 숫자'이므로 변환
        key = str(i)
        cur.execute("INSERT INTO Albums_Part2 (AlbumId, Title, ArtistId) VALUES (?,?,?)", 
                    (i, dictionary_data[key][0], dictionary_data[key][1]))
    
    conn.commit()


# 함수실행
not_cut_add_data(dictionary_data)





#----n314 Part3 : sqlite db 생성 -> DB_API (스키마 홈페이지 참조...) / 이후 데이터 넣기.
#----n314 Part3 :  생성된-> DB : DB_API에 TABLE : Albums_Part3 생성 이후 아래의 데이터 집어넣기.


# 테이블 삭제
cur.execute('DROP TABLE Albums_Part3')


# 테이블 생성.
cur.execute("""CREATE TABLE Albums_Part3(
    AlbumId INTEGER PRIMARY KEY NOT NULL, 
    Title NVARCHAR(160),
    ArtistId INTEGER)""")




json_data = {
"DATA": [
	{
		"AlbumId" : 1,
		"Title" : "For Those About To Rock We Salute You",
		"ArtistId" : 1
	},
	{
		"AlbumId" : 2,
		"Title" : "Balls to the Wall",
		"ArtistId" : 2
	},
	{
		"AlbumId" : 3,
		"Title" : "Restless and Wild",
		"ArtistId" : 2
	},
	{
		"AlbumId" : 4,
		"Title" : "Let There Be Rock",
		"ArtistId" : 1
	},
	{
		"AlbumId" : 5,
		"Title" : "Big Ones",
		"ArtistId" : 3
	},
	{
		"AlbumId" : 6,
		"Title" : "Jagged Little Pill",
		"ArtistId" : 4
	},
	{
		"AlbumId" : 7,
		"Title" : "Facelift",
		"ArtistId" : 5
	},
	{
		"AlbumId" : 8,
		"Title" : "Warner 25 Anos",
		"ArtistId" : 6
	},
	{
		"AlbumId" : 9,
		"Title" : "Plays Metallica By Four Cellos",
		"ArtistId" : 7
	},
	{
		"AlbumId" : 10,
		"Title" : "Audioslave",
		"ArtistId" : 8
	}
]}


def add_join(json_data):
    
    # 값만 가져오기.
    data = json_data['DATA']
    for i in range(len(data)):
        cur.execute('INSERT INTO Albums_Part3 VALUES(?,?,?)', 
 	    (data[i]['AlbumId'], data[i]['Title'], data[i]['ArtistId']))
    
    conn.commit()
    
# add_join(json_data)









#----n314 Part4 : sqlite db 생성 -> DB_API (스키마 홈페이지 참조...) / 이후 데이터 넣기.

