#!/bin/python3



# Complete the solve function below.
def solve(s):
    output=s.split(' ')
    finalOutput=(i.capitalize() for i in output)
    return ' '.join(finalOutput)
        
    
s = input()

result = solve(s)
print(result)