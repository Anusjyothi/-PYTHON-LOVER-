if __name__ == '__main__':
    N = int(input())
    l=[]

for i in range(N):
    command=input().split(" ")
    operation=command[0]
    if operation=="insert":
        index,value=int(command[1]),int(command[2])
        l.insert(index,value)
    elif operation=="print":
        print(l)
    elif operation=="remove":
        value=int(command[1])
        l.remove(value)
    elif operation=="append":
        value=int(command[1])
        l.append(value)
    elif operation=="sort":
        l.sort()
    elif operation=="pop":
        l.pop()
    elif operation=="reverse":
        l.reverse()
