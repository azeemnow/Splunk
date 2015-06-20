# #Read data from a file named “DataList.txt” which contains a horizontal list of data (i.e. IPs, Domains, etc.)
# and save them in Splunk friendly format in a new file called “FormatedDataList.txt”. The format of the new file
# will be: “data” OR “data” OR “data” OR ….
#
# The logical operator of OR could easily be replaced with another operator (i.e. AND) by making the
# switch on line 17 in the program.

file = open("FormatedDataList.txt", "w") #create a new file

IOCs = []

with open("DataList.txt", "r") as f: #read data from a file named: DataList
    for line in f:
        line = line.strip()
        IOCs.append(line)

s = ' OR ' #change the logical operator here
s.join(IOCs)

def quote(ip):
    quotedip = '"{}"'.format(ip)
    return quotedip

list(map(quote,IOCs))

s.join(map(quote,IOCs))

print(s.join(map(quote,IOCs)))

with open("FormatedDataList.txt", "w") as f:
    f.write(s.join(map(quote,IOCs)))


#Thank you. @azeemnow