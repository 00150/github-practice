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

