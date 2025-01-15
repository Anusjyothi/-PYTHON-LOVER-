if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort(reverse=True)
    first=l[0]
    
    for i in l:
        if i!=first:
            runnerUpScore=i
            break
    print(runnerUpScore)