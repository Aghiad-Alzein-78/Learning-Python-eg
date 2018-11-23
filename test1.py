location="F:/Dropbox/PythonCodes/Packt_Course/portfolio.csv"
# fh=open(location,"r")
# data=fh.read()
# print(data)
# fh.close()
with open(location,"r") as fh:
    for line in fh:
        line=(line.strip())
        parts=line.split(",")
        ls=[]
        parts[2]=int(parts[2])
        parts[3]=float(parts[3])
        for part in parts:
            try:
                part=part.strip("\"")
                ls.append(part)
            except:
                ls.append(part)
        print(ls)