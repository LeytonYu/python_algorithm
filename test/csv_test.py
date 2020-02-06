import csv

headers = ['class','name','sex','height','year']

rows = [
        [1,'xiaoming','male',168,23],
        [1,'xiaohong','female',162,22],
        [2,'xiaozhang','female',163,21],
        [2,'xiaoli','male',158,21]
    ]
def write1():
    with open('test2.csv','w',newline='') as f:
        ff=csv.writer(f)
        ff.writerow(headers)
        ff.writerows(rows)

def read1():
    with open('test2.csv','r') as f:
        ff=csv.reader(f)
        for i in ff:
            print(i)

if __name__=='__main__':
    read1()