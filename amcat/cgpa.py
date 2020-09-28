def gradetomark(c):
    if c=='O':
        return 10
    elif c=='A+':
        return 9
    elif c=='A':
        return 8
    elif c=='B+':
        return 7
    elif c=='B':
        return 6
    else:
        return None
    
import pandas as pd
data=pd.read_csv('sem6.csv')
lab1=list(data['lab1'])
lab2=list(data['lab2'])
r1=list(data['r1'])
r2=list(data['r2'])
r3=list(data['r3'])
r4=list(data['r4'])
eng=list(data['eng'])
ai=list(data['ai'])
mini=list(data['mini'])
cd=list(data['cd'])
#
for i in range(len(lab1)):
    summ=0
    if (gradetomark(lab1[i])!=None and gradetomark(lab2[i])!=None and gradetomark(r1[i])!=None and gradetomark(r2[i])!=None and gradetomark(r3[i])!=None and gradetomark(r4[i])!=None and gradetomark(eng[i])!=None ):
       
        summ=(gradetomark(ai[i])*3)+(gradetomark(mini[i])*2)+(gradetomark(lab1[i])*2)+(gradetomark(lab2[i])*2)+(gradetomark(r1[i])*3)+(gradetomark(r2[i])*3)+(gradetomark(r3[i])*3)+(gradetomark(cd[i])*4)+(gradetomark(eng[i])*1)+(gradetomark(r4[i])*3)
        
        print(summ/26)
    else:
        print(-1)
        
#15+4+2+2+2+1

import pandas as pd
data=pd.read_csv('cseIV_cgpa.csv')
one=list(data['sem1_gpa'])
two=list(data['sem2_gpa'])
three=list(data['sem3_gpa'])
four=list(data['sem4_gpa'])
five=list(data['sem5_gpa'])
six=list(data['sem6_gpa'])

for i in  range(len(one)):
    sumx=0
    try:
        sumx=float(one[i])+float(two[i])+float(three[i])+float(four[i])+float(five[i])+float(six[i])
    except:
        print('NIL')
        continue
    print(str(sumx/6))