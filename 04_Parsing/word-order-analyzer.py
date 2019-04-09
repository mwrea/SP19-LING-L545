import sys
import matplotlib.pyplot as plt


x = []  # proportion of OV
y = []  # proportion of VO

def get_ratios(src):
    IN = open(src)
    vo = 0
    ov = 0
    for line in IN:
        if (not line.startswith("#")) and (line.strip()):
            print(line)
            words = line.split()
            if words[7] == 'obj':
                verb = int(words[6])
                if int(words[0]) > verb:
                    vo+=1
                else:
                    ov+=1
    voRatio = vo/(vo+ov)
    ovRatio = ov/(vo+ov)
    x.append(ovRatio)
    y.append(voRatio)
    print(src)
    print(voRatio)
    print(ovRatio)
#tree-banks and their locations:
zh = 'UD_Chinese-GSD/zh_gsd-ud-dev.conllu'
ja = 'UD_Japanese-GSD/ja_gsd-ud-dev.conllu'
ko = 'UD_Korean-Kaist/ko_kaist-ud-dev.conllu'
yo = 'UD_Yoruba-YTB/yo_ytb-ud-test.conllu'
ar = 'UD_Arabic-PADT/ar_padt-ud-dev.conllu'
sv = 'UD_Swedish-Talbanken/sv_talbanken-ud-dev.conllu'
ru = 'UD_Russian-GSD/ru_gsd-ud-dev.conllu'
sl = 'UD_Slovenian-SSJ/sl_ssj-ud-dev.conllu'
pl = 'UD_Polish-LFG/pl_lfg-ud-dev.conllu'
af = 'UD_Afrikaans-AfriBooms/af_afribooms-ud-dev.conllu'
trees = [zh, ja, ko, yo, ar, sv, ru, sl, pl, af]

for t in trees:
    get_ratios(t)

labels = {0:'zh', 1:'ja', 2:'ko',3:'yo',4:'ar'}
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
plt.savefig('plot')
plt.show()

