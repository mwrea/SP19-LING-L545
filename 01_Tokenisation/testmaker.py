import fileinput
IN = open('UD_Japanese-GSD/ja_gsd-ud-test.conllu')
OUT = open('test.txt', 'w')
for line in IN:
     if line.startswith('#'):
         sent = line[9:]
         if not 'test' in sent:
             OUT.write(sent)

IN.close()
OUT.close()
