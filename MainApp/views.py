from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import csv
import json
f=open('static/files/demo.txt','r')
c=open('static/files/demo.csv','w',newline='')
data=f.readlines()
writer=csv.writer(c)
header=data[0].split(',')
header.insert(0,"ID")
csv.DictWriter(c,fieldnames=header).writeheader()
id=1
for d in data:
    if d.split(',')[0]!="BANKNIFTY":
        lst2=[]
        lst2.append(d.split(','))
        lst2[0][:0]=[id]
        writer.writerows(lst2)
        id=id+1
def read_csv(request):
    return render(request,'demo.csv')    
def make_json(request):
    data = {}
    with open("static/files/demo.csv", encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows['ID']
            data[key] = rows
    #with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    #    jsonf.write(json.dumps(data, indent=4))
    return HttpResponse(json.dumps(data,indent=4),content_type="application/json")


#make_json("C:\\Users\HP\\Downloads\\demo.csv","C:\\Users\HP\\Downloads\\demo.json")

def home(request):
    return HttpResponse("hello")