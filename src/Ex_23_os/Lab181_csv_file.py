import csv

with open ('test.csv', 'r') as csvfile:
    #print(csvfile.read())
    for col in csv.reader(csvfile):
        print(col[0],col[1],sep='|')

