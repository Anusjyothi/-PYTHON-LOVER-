import re
n=int(input("Enter the no of mobile numbers: "))
for i in range(0,n):
    if re.match(r'[789]\d{9}$', input()):
        print('YES')
    else:
        print('NO')
    
