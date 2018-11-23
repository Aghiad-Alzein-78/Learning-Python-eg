    # port.py
fileName="F:/Dropbox/PythonCodes/Packt_Course/portfolio.csv"
total=0.0
with open(fileName,'r') as f:
    header=next(f).strip().split(",")

    print(header)
    for line in f:
        line=line.strip()
        parts=line.split(",")
        parts[0]=parts[0].strip('"')
        parts[1]=parts[1].strip('"')
        parts[2]=int(parts[2])
        parts[3]=float(parts[3])
        total+=parts[2]*parts[3]

        print(parts)
print("Total cost:",total)