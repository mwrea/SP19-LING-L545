all:
	hfst-lexc chv.lexc -o chv.lexc.hfst
	hfst-twolc chv.twol -o chv.twol.hfst
	hfst-compose-intersect -1 chv.lexc.hfst -2 chv.twol.hfst -o chv.gen.hfst
	hfst-lexc ava.lexc -o ava.lexc.hfst
	hfst-twolc ava.twoc -o ava.twoc.hfst
	hfst-invert ava.lexc.hfst | hfst-compose-intersect -1 - -2 ava.twoc.hfst | hfst-invert -o ava.gen.hfst
	hfst-lexc fin.lexc -o fin.lexc.hfst
