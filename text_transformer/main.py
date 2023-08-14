import pypinyin,typing
with open('data.txt','r',encoding='utf-8') as b:
    b=b.readline()
def getPinyin(char:str)->typing.Tuple[str,str,int]:
    pyHead=pypinyin.lazy_pinyin(char,style=pypinyin.Style.INITIALS,\
            strict=False,neutral_tone_with_five=True)[0]
    pyTmp=pypinyin.lazy_pinyin(char,style=pypinyin.Style.FINALS_TONE3,\
            strict=False,neutral_tone_with_five=True)[0]
    pyTail,pyTone=pyTmp[:-1],int(pyTmp[-1])
    return [pyHead,pyTail,pyTone]
c=[getPinyin(i)+[i]for i in b]
ex='，。、；：‘’“”【】《》！？…—\n'
while True:
    d=input()
    ans=''
    for i in d:
        if (i in ex) or i.isascii():ans+=i;continue
        try:head,tail,tone=getPinyin(i)
        except ValueError:ans+=i;continue
        score=0;char=i
        for j in c:
            head2,tail2,tone2,ch=j
            if head==head2 and tail==tail2:
                if score==0:
                    char=ch;score=1
                if tone==tone2:
                    char=ch;score=2;break
        ans+=char
    print(ans)
