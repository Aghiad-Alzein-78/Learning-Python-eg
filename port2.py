import csv
fileName="f:/Dropbox/PythonCodes/Packt_Course/missing.csv"

def portfolio_cost(filename,*,errors="warn"): 
    """
        computes total shares*price in a CSV file with
        name , date , shares , price  Data 
    """
    if errors not in {"raise","warn","silent"}:
        raise ValueError("errors must be 'raise' , 'warn' or 'silent")
    total=0
    with open(filename,'r') as f:
        rows=csv.reader(f)
        header=next(rows)
        for rownum,row in enumerate(rows,start=1):
            rownum+=1
            try:
                row[2]=int(row[2])
                 row[3]=float(row[3])
            except ValueError as err:
                if errors=='warn':
                    print("Bad row :",row)
                    print("Reason :",err,f"at row number {rownum}")
                elif errors=="raise":
                    raise
                else:
                    pass

                continue
            total+=row[2]*row[3]

    return total

print(portfolio_cost(fileName,errors='silent'))
