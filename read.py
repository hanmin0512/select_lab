import pandas as pd
import math

class Person:
    def __init__(self, name, score, sel1,sel2, sel3, sel4):
        self.name = name
        self.score = score
        self.sel1 = sel1
        self.sel2 = sel2
        self.sel3 = sel3
        self.sel4 = sel4

def percent1(P):
    pivot = math.ceil(len(P) * (60/100))
    P1 = P[0:pivot]
    P2 = P[pivot::]
    sel2(P2)
    return P1

def percent2(P):
    pivot = math.ceil(len(P) * (60/100))
    P1 = P[0:pivot]
    P2 = P[pivot::]
    sel3(P2)
    return P1

def percent3(P):
    pivot = math.ceil(len(P) * (60/100))
    P1 = P[0:pivot]
    P2 = P[pivot::]
    sel4(P2)
    return P1

def sel1(sorted_people):
    global park_giseok1, park_sohyun1, oh1, do1, no
    for person in sorted_people:
        #print(person.name)
        if person.sel1 == '박기석':
            park_giseok1.append(person)#([person.name, person.score])
        elif person.sel1 == '오승현':
            oh1.append(person)#([person.name, person.score])
        elif person.sel1 == '도재수':
            do1.append(person)#([person.name, person.score])
        elif person.sel1 == '박소현':
            park_sohyun1.append(person)#([person.name, person.score]) 
        else:
            no.append(person)
    
    park_giseok1 = sorting(park_giseok1)
    oh1 = sorting(oh1)
    do1 = sorting(do1)
    park_sohyun1 = sorting(park_sohyun1)
    

def sel2(sorted_people):
    global park_giseok2, oh2, do2, park_sohyun2
    for person in sorted_people:
        #print(person.name)
        if person.sel2 == '박기석':
            park_giseok2.append(person)#([person.name, person.score])
        elif person.sel2 == '오승현':
            oh2.append(person)#([person.name, person.score])
        elif person.sel2 == '도재수':
            do2.append(person)#([person.name, person.score])
        elif person.sel2 == '박소현':
            park_sohyun2.append(person)#([person.name, person.score]) 

    park_giseok2 = sorting(park_giseok2)
    park_sohyun2 = sorting(park_sohyun2)
    oh2 = sorting(oh2)
    do2 = sorting(do2)
    
    park_giseok2 = percent2(park_giseok2)
    park_sohyun2 = percent2(park_sohyun2)
    oh2 = percent2(oh2)
    do2 = percent2(do2)

def sel3(sorted_people):
    global park_giseok3, oh3, do3, park_sohyun3
    for person in sorted_people:
    #print(person.name)
        if person.sel3 == '박기석':
            park_giseok3.append(person)#([person.name, person.score])
        elif person.sel3 == '오승현':
            oh3.append(person)#([person.name, person.score])
        elif person.sel3 == '도재수':
            do3.append(person)#([person.name, person.score])
        elif person.sel3 == '박소현':
            park_sohyun3.append(person)#([person.name, person.score]) 
    park_giseok3 = sorting(park_giseok3)
    park_sohyun3 = sorting(park_sohyun3)
    oh3 = sorting(oh3)
    do3 = sorting(do3)
    
    park_giseok3 = percent3(park_giseok3)
    park_sohyun3 = percent3(park_sohyun3)
    oh3 = percent3(oh3)
    do3 = percent3(do3)



def sel4(sorted_people):
    global park_giseok4, oh4, do4, park_sohyun4
     
    for person in sorted_people:
    #print(person.name)
        if person.sel4 == '박기석':
            park_giseok4.append(person)#([person.name, person.score])
        elif person.sel4 == '오승현':
            oh4.append(person)#([person.name, person.score])
        elif person.sel4 == '도재수':
            do4.append(person)#([person.name, person.score])
        elif person.sel4 == '박소현':
            park_sohyun4.append(person)#([person.name, person.score]) 

    park_giseok4 = sorting(park_giseok4)
    park_sohyun4 = sorting(park_sohyun4)
    oh4 = sorting(oh4)
    do4 = sorting(do4)

def printP(P):
    for i in range(len(P)):
        print(P[i].name, end=' ')
    print()

def sorting(P):
    sorted_P = sorted(P, key=lambda p: p.score, reverse=True)
    return sorted_P

def write_excel(P, professor):
    xls_name = professor +".xlsx"
    data = {
        'name' : [],
        'score' : []
    }
    for i in range(len(P)):
        data['name'].append(P[i].name)#print(P[i].name)
        data['score'].append(P[i].score)#print(P[i].score)    
    #print(data)
    dw = pd.DataFrame(data)
    dw.to_excel(xls_name, index=True)
    
    print(xls_name, total_score(P))
# Excel 파일 읽기
df = pd.read_excel('example.xlsx')

def no_sel(P):
    global no_sel_park_giseok, no_sel_do, no_sel_oh, no_sel_park_sohyun
    P = sorting(P)
    i=0
    for p in P:
        if i % 4 == 0:
            no_sel_park_giseok.append(p)
        elif i%4 == 1:
            no_sel_park_sohyun.append(p)
        elif i%4 == 2:
            no_sel_oh.append(p)
        elif i%4 == 3:
            no_sel_do.append(p)
        i+=1
            
        
def remainder(P):
    global remain
    if len(P) > 20:
        remain.extend(P[20::])
        P = P[:20]
    return P

def isTrue(P):
    return len(P) < 20

def last_sel(P):
    global park_giseok, park_sohyun, oh, do
    i=0
    for p in P:
        if isTrue(park_giseok) and i%4 == 0:
            park_giseok.append(p)
        else:
            i+=1
        if isTrue(park_sohyun) and i%4 ==1:
            park_sohyun.append(p)
        else:
            i+=1
        if isTrue(oh) and i%4 == 2:
            oh.append(p)
        else:
            i+=1
        if isTrue(do) and i%4 ==3:
            do.append(p)
        else:
            i+=1
        i+=1
            
def total_score(P):
    sum =0
    for p in P:
        sum += p.score
    return sum / len(P)
# 데이터프레임 출력
#print(len(df))

name = []
score = []
people =[]

no = []
no_sel_park_giseok = []
no_sel_do = []
no_sel_oh = []
no_sel_park_sohyun = []


park_giseok1 = []
do1 = []
oh1 = []
park_sohyun1 = []

park_giseok2 = []
do2 = []
oh2 = []
park_sohyun2 = []

park_giseok3 = []
do3 = []
oh3 = []
park_sohyun3 = []

park_giseok4 = []
do4 = []
oh4 = []
park_sohyun4 = []

select1 = []
select2 = []
select3 = []
select4 = []

remain = []
for i in range(len(df)):
    name.append(df['이름'][i])
    score.append(df['전체총평점'][i])
    select1.append(df['1지망'][i])
    select2.append(df['2지망'][i])
    select3.append(df['3지망'][i])
    select4.append(df['4지망'][i])
    #hope[name[i]] = [score[i], df.sel1[i], df.sel2[i], df.sel3[i], df.sel4[i]]
    per = Person(name[i], score[i], select1[i], select2[i], select3[i], select4[i])
    people.append(per)
sorted_people = sorted(people, key=lambda p: p.score, reverse=True)

sel1(sorted_people)
no_sel(no)

park_giseok1 = percent1(park_giseok1)
park_sohyun1 = percent1(park_sohyun1)
oh1 = percent1(oh1)
do1 = percent1(do1)

park_giseok = park_giseok1 + park_giseok2 + park_giseok3 + park_giseok4 + no_sel_park_giseok
park_sohyun = park_sohyun1 + park_sohyun2 + park_sohyun3 + park_sohyun4 + no_sel_park_sohyun
oh = oh1 + oh2 + oh3 + oh4 + no_sel_oh
do = do1 + do2 + do3 + do4 + no_sel_do

park_giseok = remainder(park_giseok)
park_sohyun = remainder(park_sohyun)
oh = remainder(oh)
do = remainder(do)

remain = sorting(remain)
last_sel(remain)
write_excel(park_giseok, "박기석")
write_excel(park_sohyun, "박소현")
write_excel(oh, "오승현")
write_excel(do, "도재수")
'''
printP(park_giseok1)
printP(park_sohyun1)
printP(oh1)
printP(do1)
printP(park_giseok2)
printP(park_sohyun2)
printP(oh2)
printP(do2)
printP(park_giseok3)
printP(park_sohyun3)
printP(oh3)
printP(do3)
printP(park_giseok4)
printP(park_sohyun4)
printP(oh4)
printP(do4)
'''