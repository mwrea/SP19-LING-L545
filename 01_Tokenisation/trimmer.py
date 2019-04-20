IN = open('wiki.txt', 'r')
OUT = open('trimmedwiki.txt', 'w')
for line in IN:
    if line.startswith('[1-9]'):
        pass
    else:
        OUT.write(line)
IN.close()
OUT.close()
