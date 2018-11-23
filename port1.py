import csv

fileName="F:/Dropbox/PythonCodes/Packt_Course/portfolio.csv"
total=0
with open(fileName,'r') as f:
    rows=csv.reader(f)
    header=next(rows)
    for row in rows:
        row[2]=int(row[2])
        row[3]=float(row[3])
        total+=row[2]*row[3]

print("Total Cost =",total)
        