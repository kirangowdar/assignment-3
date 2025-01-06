#WAP to find the total number of people above the age of 18
d={ "kiran":20,
    "manu":19,
    "keerthi":13,
    "nagu":28,
    "harish":31,
    "ammu":15,
    "dhanu":25,
    "gowri":30,}
print(d)
l=d.values()
e=[]
for i in l:
    if i>18:
        e.append(i)
n=len(e)
print('number of peoples,age above 18:-',n)