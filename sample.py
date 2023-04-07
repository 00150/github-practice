import csv


f = open('titanic.csv', 'r')
reader = csv.reader(f)


data = list(reader)


for idx, row in enumerate(data[1:]):
    print(idx, row[2])
    

    
