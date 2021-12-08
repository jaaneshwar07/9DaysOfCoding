import re
def remove(string):
    return (re.sub("[aeiouAEIOU]","",string))           

string = "jaaneshwar i am a student in city engineering college"
print( remove(string))
print( "from"+ string)