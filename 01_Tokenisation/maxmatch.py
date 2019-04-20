import fileinput
jdict = open('dict.txt', 'w')
count=0
current = ''
best = ''
highest=0
#sentence from test
sent = 'これに不快感を示す住民はいましたが,現在,                                            表立って反対や抗議の声を挙げている住民はいないようです'

while not sent==''
    for line in jdict:
        if line == sent[0:x]:
            count+=1
            if count > highest:
                highest=count
                sent[0:x]=current

    if count==0:
        print(best)
    sent=sent[len(best):]
    count=0


