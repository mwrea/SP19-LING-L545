IN = open('UD_Japanese-GSD/ja_gsd-ud-test.conllu','r')
OUT = open('dict.txt', 'w')

for line in IN:
    if (not line.startswith("#")) and line.strip():
        data=line.split()
        OUT.write(data[1] + '\n')

