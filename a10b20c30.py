s=input()
if(s[-2].isdigit()==False):
    s=s+'@@'
st=''
i=0
while(i<=len(s)-1):
    num=''
    index1=s.index(s[i])+1
    index2=s.index(s[i])+2
    num=num+s[index1]
    try:
        if(s[index2].isdigit()):
            num=num+s[index2]
            st=st+(s[i]*int(num))
            i=i+3
        else:
            st=st+(s[i]*int(num))
            i=i+2
    except IndexError:
        break
print(st)
