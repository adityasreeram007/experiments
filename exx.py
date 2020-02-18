import pandas as pd 
import xlsxwriter                                      
def checker(a):
    if(a=='O'):
        return 10
    elif(a=='A+'):
        return 9
    elif(a=='A'):
        return 8
    elif(a=='B+'):
        return 7
    elif(a=='B'):
        return 6
    return
xls=pd.ExcelFile('1reval.xlsx') 
sheetx=xls.parse(0)
n=54
first=list(sheetx['BS8161'])
second=list(sheetx['CY8151'])
third=list(sheetx['GE8151'])
fourth=list(sheetx['GE8152'])
fifth=list(sheetx['GE8161'])
sixth=list(sheetx['HS8151'])
seventh=list(sheetx['MA8151'])
eighth=list(sheetx['PH8151'])
gpa=[]
for i in range(1,47):
    summ=0
    summ+=checker(first[i])*2
    
    summ+=checker(second[i])*3	
    summ+=checker(third[i])*3
    summ+=checker(fourth[i])*4	
    summ+=checker(fifth[i])*2
    summ+=checker(sixth[i])*4	
    summ+=checker(seventh[i])*4	
    summ+=checker(eighth[i])*3
    print(summ)
    gpa.append(summ/25)
workbook = xlsxwriter.Workbook('1reval.xlsx')
worksheet = workbook.add_worksheet() 
worksheet.write('N1','x')
strr='K'
row=2
for i in gpa:
    worksheet.write(strr+str(row),str(i))
    print(i)
    row+=1
#print(gpa)
workbook.close()
    
    	 			   

