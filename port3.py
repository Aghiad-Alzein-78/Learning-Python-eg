import csv,json
from pprint import pprint
import os
fileName="f:/Dropbox/PythonCodes/Packt_Course/portfolio.csv"
target="f:/Dropbox/PythonCodes/Packt_Course/data.json"

def cls():
    os.system('cls')

def read_portfolio(filename,*,errors='warn'):
    if errors not in {"warn","raise","silent"}:
        raise ValueError("Errors must be blas blas blas")
    portfolio=[]
    with open(filename,'r') as f:
        rows=csv.reader(f)
        for ind,row in enumerate(rows,start=1):
            try:
                row[2]=int(row[2])
                row[3]=float(row[3])
            except ValueError as err:
                if errors=="warn":
                    print(f"In row {ind} there is a {err}")
                    print(f"row {ind}={row}")
                elif errors=='raise':
                    raise
                else:
                    pass
                continue
            record={
                'name':row[0],
                'date':row[1],
                'shares':row[2],
                'price':row[3]
            }
            portfolio.append(record)
    return portfolio
        
def convertToJson(dic):
    with open(target,'w') as f:
        data=json.dumps(dic)
        f.write(data)
        print("DONE")

def convertFromJson(filename):
    with open(target,'r') as f:
        dataJson=f.read()
        data=json.loads(dataJson)
    return data

portfolio=read_portfolio(fileName,errors='silent')
total=0
# more100=[]
# for holding in portfolio:
#     if holding['shares']>100:
#         more100.append(holding)
# pprint(more100)

total=sum([holding['shares']*holding['price'] for holding in portfolio])
print(total)

more100=[holding for holding in portfolio if holding['shares']>100]
pprint(more100)
names={holding['name'] for holding in portfolio }
print(names)

 










# total=0
# for record in portfolio:
#     total+=record['shares']*record['price']
# data=convertFromJson(target)
# print(data)
# print("="*25)
# print(type(data))
# print(f"Total={total}")
# convertToJson(portfolio)
          
