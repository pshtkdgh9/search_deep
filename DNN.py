import pymongo
import csv


myclient = pymongo.MongoClient('mongodb://203.255.92.141:27017/')
mydb = myclient['ID']
mycol = mydb['test']


data_dic= mycol.find({"keyId" : 810})
data_list = ['name','inst','ntisQual','remainQual','lct','acc','coop','qunt','qual']
cnt = 0
f = open('socialdata.csv','w', newline='',encoding = "utf-8-sig")
wr = csv.writer(f)
wr.writerow(data_list)
for data in data_dic:
    name = data['name']
    inst = data['inst']
    ntisQual = data['factor']['ntisQual']
    remainQual= data['factor']['remainQual']
    lct= data['factor']['lct']
    acc= data['factor']['acc']
    coop= data['factor']['coop']
    qunt= data['factor']['qunt']
    qual= data['factor']['qual']
    wr.writerow([name,inst,ntisQual,remainQual,lct,acc,coop,qunt,qual])
    #data_list.append({"name" : data['name'],"inst" : data['inst'] , "factor" : data['factor']})
    cnt += 1
print(cnt)
f.close()
