T=int(input())
for i in range(0,T):
    try:
        a, b= map(int, input().split())
        c=int(a//b)
        print(c)
    except Exception as e:
        print("Error Code: ",e)