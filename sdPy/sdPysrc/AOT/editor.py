import re
with open('numbafunctionssrc.py') as f:
    old=f.read()
with open('numbafunctions.py') as f:
    new=f.read()    

no= re.findall('(.*)\ndef (.*?)\(.*\)+',old)
nn= re.findall('\ndef (.*?)\(.*\)+',new)
print(len(no),len(nn))
# for i,j in zip(no,nn):
#     print(i,j)
func=nn[1]
for func in nn:
    for oldfunc in no:
        if func==oldfunc[1]:
            print(func,oldfunc[1])
            print(re.findall('\ndef '+func,new))
            new=re.sub("\ndef " +func+'(\(.*\))','\n'+oldfunc[0]+'\ndef '+func+r'\1',new)
            no.remove(oldfunc)
            break

with open('finalfile.py','w') as f:
    f.write(new)
# print(set(nn)-set(no))    
   

# %%
