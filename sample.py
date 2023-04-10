#--1. 테이블 생성.
q1 = """CREATE TABLE User(
id INTEGER PRIMARY KEY,
username VARCHAR(128),
password VARCHAR(128));"""


#--2. 테이블 생성.
q2 ="""CREATE TABLE Product(
id INTEGER PRIMARY KEY,
product_name VARCHAR(128),
product_price INTEGER);"""


#--3. 테이블 생성.
q3 = """CREATE TABLE User_Product(
user_product_id INTEGER PRIMARY KEY,
user_id INTEGER REFERENCES User(id),
product_id INTEGER REFERENCES Product(id));"""



# -- Part 2.
part2_q1 = """SELECT p.ProductName, p.UnitPrice  
FROM Product AS p
ORDER BY p.UnitPrice DESC LIMIT 10;"""


# 여러 방법이 존재하나, 내 경우는 이렇게 두가지를 생각했다.
part2_q2 = """SELECT AVG(e.HireDate - e.BirthDate) AS age
FROM  Employee AS e;"""

another_part2_q2 = """SELECT AVG(DATE(e.HireDate) - DATE(e.BirthDate)) AS age
FROM Employee AS e; """


part2_q3 = """SELECT p.Id, p.ProductName, p.UnitPrice, s.CompanyName  
FROM Product AS p
LEFT OUTER JOIN Supplier AS s ON p.SupplierId = s.Id
ORDER BY p.UnitPrice DESC  LIMIT 10; 
"""


part2_q4 = """SELECT c.CategoryName, COUNT(p.CategoryId)  
FROM Product AS p
LEFT OUTER JOIN Category AS c ON p.CategoryId = c.Id
GROUP BY p.CategoryId 
ORDER BY COUNT(p.CategoryId) DESC LIMIT 2;"""

part2_q5 = """SELECT e.City, AVG(DATE(e.HireDate)-DATE(e.BirthDate))  
FROM  Employee AS e
GROUP BY e.City; """


part2_q6 = """SELECT e.Id, e.LastName, COUNT(t.TerritoryDescription)
FROM Employee AS e
INNER JOIN EmployeeTerritory AS et ON e.Id = et.EmployeeId 
INNER JOIN Territory AS t ON et.TerritoryId = t.Id 
GROUP BY e.LastName  
ORDER BY COUNT(t.TerritoryDescription) DESC;"""
