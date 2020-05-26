operator=input('输入：')
operator2=''
for i in operator:
    if i==' ':
        pass
    else:
        operator2+=i
print(operator2)
num=''
num_list=[]
symbol=[]
count=0

for i in str(operator2):
    if count>1:
        print('***')
        break
    elif i.isdigit() or i=='.':
        num+=i
        count=0
    elif i=='*' or i=='/' or i=='+' or i=='-':
        num_list.append(float(num))
        num=''
        symbol.append(i)
        count+=1
    else:
        print("***")
        break
num_list.append(float(num))

while symbol:
    while '*' in symbol or '/' in symbol:
        for i in symbol:
            if i=='*':
                j=symbol.index('*')
                resault=num_list[j]*num_list[j+1]
                #print(resault)
                del num_list[j:j+2]
                num_list.insert(j,resault)
                symbol.remove('*')
                break
            elif i=='/':
                j=symbol.index('/')
                resault=num_list[j]/num_list[j+2]
                del num_list[j:j+2]
                num_list.insert(j,resault)
                symbol.remove('/')
                break
    while '+' in symbol or '-' in symbol:
        for i in symbol:
            if i=='+':
                j=symbol.index('+')
                resault=num_list[j]+num_list[j+1]
                del num_list[j:j+2]
                num_list.insert(j,resault)
                symbol.remove('+')
            elif i=='-':
                j=symbol.index('-')
                resault=num_list[j]-resault[j+1]
                del num_list[j:j+2]
                num_list.insert(j,resault)
                symbol.remove('-')
                break
print(resault)