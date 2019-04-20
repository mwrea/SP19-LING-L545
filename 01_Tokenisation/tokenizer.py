import nltk.tokenize.punkt

tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
tokenizer.tokenize('wiki.txt')
