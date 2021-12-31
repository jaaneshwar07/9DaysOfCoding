def min (string):
    rohanv = 0
    rahulc = 0
    vowels = ['AaEeIiOou']
    for i in range(len(string)):
        if string[i] in vowels:
            rohanv = rohanv + len(string)-i
        else :
            rahulc = rahulc +len(string)-i
        if rohanv > rahulc :
            print("rohan",rohanv)
        elif rohanv == rahulc:
            print("draw")
        else:
            print("rahul",rahulc)
    print((string))
  
    

print("enter ang string ")
string = input()
min(string)


