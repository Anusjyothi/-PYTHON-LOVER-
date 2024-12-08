import textwrap
def textWrap (string , max_width):
    return textwrap.fill(string, max_width)
string, max_width= input(), int(input())
result=textWrap(string, max_width)
print(result)