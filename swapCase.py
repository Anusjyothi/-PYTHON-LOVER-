

def swapcase(s):
    string=""
    for i in s:
        if i.isupper()==True:
            string+=i.lower()
        else:
            string+=i.upper()
    return string
s=input()
output=swapcase(s)
print(output)