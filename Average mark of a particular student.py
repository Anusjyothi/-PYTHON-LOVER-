n=int(input())
student_marks={}
for i in range(0,n):
    name, *line= input().split()
    scores=list(map(float,line))
    student_marks[name]=scores
query_name=input()
l1=list(student_marks[query_name])
addition=sum(l1)
average_marks=addition/len(l1)
print("%.2f"%average_marks)
