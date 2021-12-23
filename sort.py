def cf(string,c):
    count=0
    for i in range(len(string)):
        if(string[i]==c):
            count+=1
    return count
def sorta(string):
    n = len(string)
    vp =[]
    for i in range(n):
        vp.append((cf(string,string[i]),string[i]))
    vp.sort()
    for i in range(len(vp)):
        print(vp[i][1])
print("enter the string")
m = input()
string = m
sorta(string)